import os
import pickle
import datetime
from typing import List, Dict
from pathlib import Path


class Highscores:
    # PATHS
    BASE_PATH = Path(__file__).parents[1]
    DATA_PATH = BASE_PATH / "data"
    PICKLE_PATH = DATA_PATH / "highscores.pkl"
    BACKUP_PATH = DATA_PATH / "backup_highscores.pkl"

    def __init__(self):
        self.today = datetime.datetime.today()
        self.date = str(self.today.date())

        self._load_data()

    def _exists_pickle(self) -> bool:
        """Returns True if main pickle file exists."""

        return os.path.exists(self.PICKLE_PATH)

    def _exists_backup(self) -> bool:
        """Returns True if backup pickle file exists."""

        return os.path.exists(self.BACKUP_PATH)

    def _load_data(self) -> None:
        """
        Loads pickle data to self.data if a pickle exists, otherwise
        it gives a default value to self.data.
        """

        self.data: Dict

        if self._exists_pickle():
            path = self.PICKLE_PATH
        elif self._exists_backup():
            path = self.BACKUP_PATH
        else:
            self.data = {
                "daily-highscores": [f"{self.date}: 0"],
                "all-time-highscore": f"{self.date}: 0",
            }
            return

        with open(path, "rb") as data_pickle:
            self.data = pickle.load(data_pickle)
            # Add highscore line for current day if one does not exist
            if self.data["daily-highscores"][-1][:10] != str(self.date):
                self.data["daily-highscores"].append(f"{self.date}: 0")

    def _set_stats(self) -> None:
        """Sets current wpm stats from self.data."""

        self.today_wpm = int(self.data["daily-highscores"][-1].split()[-1])
        self.all_time_wpm = int(self.data["all-time-highscore"].split()[-1])

    def _delete_backup(self) -> None:
        """Deletes the backup pickle file, if it exists."""

        if self._exists_backup():
            os.remove(self.BACKUP_PATH)

    def _make_backup(self) -> None:
        """Turns current pickle file into a backup file, and deletes old backup."""

        self._delete_backup()

        os.rename(self.PICKLE_PATH, self.BACKUP_PATH)

    def _save_data(self) -> None:
        """Saves data to a pickle file."""

        if self._exists_pickle():
            self._make_backup()

        with open(self.PICKLE_PATH, "wb") as data_pickle:
            pickle.dump(self.data, data_pickle)

    def _check_all_time_highscore(self, score: int) -> bool:
        """Returns True if highscore provided is greater than the all time highscore."""

        self._set_stats()

        return score > self.all_time_wpm

    def _check_daily_highscore(self, score: int) -> bool:
        """Returns True if highscore provided is greater than today's highscore."""

        self._set_stats()

        return score > self.today_wpm

    def _add_daily_highscore(self, score: int) -> None:
        """Adds a highscore to self.data for today."""

        # Remove old daily highscore
        self.data["daily-highscores"].pop()

        self.data["daily-highscores"].append(f"{self.date}: {score}")

    def _add_all_time_highscore(self, score: int) -> None:
        """Adds a daily and all time highscore to self.data."""
        self._add_daily_highscore(score)

        self.data["all-time-highscore"] = f"{self.date}: {score}"

    # PUBLIC METHODS
    def delete_daily_highscore(self) -> None:
        """Deletes current daily highscore."""

        self._add_daily_highscore(0)
        self._save_data()

    def delete_all_time_highscore(self) -> None:
        """Deletes the current all-time highscore, and also today's highscore."""

        self._add_all_time_highscore(0)
        self._save_data()

    def delete_all_highscores(self) -> None:
        """Deletes all daily highscore and all-time highscore data."""

        self.data["daily-highscores"] = [f"{self.date}: 0"]
        self.delete_all_time_highscore()

    def get_datetime_object(self, date: str) -> datetime.datetime:
        """
        Returns a datetime object from a given string.
        The string must be in the format yyyy-mm-dd.
        """

        # Convert string into a list of integers
        numerical_date: list = list(map(int, date.split("-")))

        return datetime.datetime(
            numerical_date[0], numerical_date[1], numerical_date[2]
        )

    def days_since_set(self) -> int:
        """Returns the number of days since the all-time highscore was set."""

        # Get the date section from the all-time highscore
        # then get a datetime object for that date
        string_date: str = self.data["all-time-highscore"].split(":")[0]
        date_set: datetime.datetime = self.get_datetime_object(string_date)

        # Get a timedelta object representing the time between today and date_set
        difference: datetime.timedelta = self.today - date_set

        return difference.days

    def get_wpm(self) -> tuple:
        """
        Returns the daily and all time highest wpm.

        Used to display wpm scores on main menu.
        """

        self._set_stats()

        return self.today_wpm, self.all_time_wpm

    def update(self, score: int) -> str:
        """Main function, checks if a given score is a highscore then saves that
        value to self.data and to a pickle file.

        Returns string representing whether value was a daily or all time highscore.
        """

        result = "none"

        if self._check_all_time_highscore(score):
            self._add_all_time_highscore(score)
            self._save_data()
            result = "all-time"

        elif self._check_daily_highscore(score):
            self._add_daily_highscore(score)
            self._save_data()
            result = "daily"

        return result

    def get_stats_dailies(self) -> List[str]:
        """
        Returns self.data["daily-highscores"] as raw data to be used
        in the plotting of a graph.
        """

        return self.data["daily-highscores"]


if __name__ == "__main__":
    highscore = Highscores()

    print(highscore.update(1))
    print(highscore.update(2))
    print(highscore.update(1))
