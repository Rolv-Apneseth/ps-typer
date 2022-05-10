from datetime import datetime
from pathlib import Path

import appdirs

# CONSTANTS -----------------------------------------------------------------------------
APP_NAME: str = "ps-typer"

OPTIONS_HIGHSCORES: tuple[str, str, str] = ("none", "today", "all_time")
DATETIME_FORMAT_STRING: str = "%Y-%m-%d"

# Paths
PATH_USER_DATA_DIR: Path = Path(appdirs.user_data_dir(APP_NAME))
PATH_USER_PREFERENCES_JSON: Path = PATH_USER_DATA_DIR / "preferences.json"
PATH_USER_DATA_DB: Path = PATH_USER_DATA_DIR / "user_data.db"
# Ensure directory exists
if not PATH_USER_DATA_DIR.is_dir():
    PATH_USER_DATA_DIR.mkdir(parents=True)

PATH_BASE: Path = Path(__file__).parents[1]
PATH_ASSETS: Path = PATH_BASE / "assets"
PATH_ICONS: Path = PATH_ASSETS / "icon.png"
PATH_FONTS: Path = PATH_ASSETS / "InconsolataBold.ttf"
PATH_SOUNDS: Path = PATH_ASSETS / "sounds"

# Statistics window
GRAPH_MEASUREMENTS: dict[str, int | float] = dict(
    axis_width=1.5,
    curve_width=2.5,
    symbol_width=7,
    grid_alpha=90,
)


# FUNCTIONS -----------------------------------------------------------------------------
def get_today() -> str:
    f"""Get today's date as a string in the format {DATETIME_FORMAT_STRING}"""
    return datetime.today().strftime(DATETIME_FORMAT_STRING)


def get_datetime_from_str(date: str) -> datetime:
    f"""
    Returns datetime object from string supplied in the format {DATETIME_FORMAT_STRING}
    """
    return datetime.strptime(date, DATETIME_FORMAT_STRING)
