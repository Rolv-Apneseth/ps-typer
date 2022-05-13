import json
from dataclasses import dataclass, field, fields
from pathlib import Path

from dataclasses_json import dataclass_json

from ps_typer.data import style
from ps_typer.data.utils import PATH_SOUNDS, PATH_USER_PREFERENCES_JSON

# DEFAULTS ------------------------------------------------------------------------------
DEFAULT_COLOURS = style.get_colours()
DEFAULT_SOUND_FILENAME = "key_1.wav"


# MODEL ---------------------------------------------------------------------------------
@dataclass_json
@dataclass
class Preferences:
    selected_mode: int = 0
    dark_mode: bool = True
    colours: dict[str, dict[str, str]] = field(default_factory=lambda: DEFAULT_COLOURS)

    play_sound: bool = False
    sound_filename: str = DEFAULT_SOUND_FILENAME


# DATA HANDLER --------------------------------------------------------------------------
class UserPreferencesDataHandler:
    def __init__(self) -> None:
        self._load_preferences()

    def _load_preferences(self) -> None:
        self.preferences: Preferences

        # Default values if the json file does not exist
        if not PATH_USER_PREFERENCES_JSON.is_file():
            self.preferences = Preferences()
            return

        with open(PATH_USER_PREFERENCES_JSON, "r") as json_file:
            # https://github.com/lidatong/dataclasses-json/issues/31
            self.preferences = Preferences.from_dict(  # type: ignore
                json.load(json_file)
            )

        self._ensure_exists_sound_file()

    def _save_preferences(self) -> None:
        with open(PATH_USER_PREFERENCES_JSON, "w") as json_file:
            # https://github.com/lidatong/dataclasses-json/issues/31
            json.dump(self.preferences.to_dict(), json_file)  # type: ignore

    def _ensure_exists_sound_file(self) -> None:
        sound_file: Path = PATH_SOUNDS / self.preferences.sound_filename
        if not sound_file.is_file():
            self.preferences.sound_filename = DEFAULT_SOUND_FILENAME

    def get_preferences(self) -> Preferences:
        return self.preferences

    def toggle_dark_mode(self) -> None:
        self.preferences.dark_mode = not self.preferences.dark_mode
        self.preferences.colours = style.get_colours(self.preferences.dark_mode)
        self._save_preferences()

    def set_selected_mode(self, mode: int) -> None:
        self.preferences.selected_mode = mode
        self._save_preferences()

    def toggle_play_sound(self) -> None:
        self.preferences.play_sound = not self.preferences.play_sound
        self._save_preferences()

    def set_sound_filename(self, filename: str) -> None:
        self.preferences.sound_filename = filename
        self._ensure_exists_sound_file()
        self._save_preferences()


if __name__ == "__main__":
    from pprint import pprint

    p = UserPreferencesDataHandler()
    p.toggle_dark_mode()
    pprint(p.get_preferences())
    print(PATH_USER_PREFERENCES_JSON)
