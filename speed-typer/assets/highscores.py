import os
import pickle
import datetime


# CONSTANTS
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
PICKLE_PATH = os.path.join(FILE_PATH, "data.pkl")
BACKUP_PATH = os.path.join(FILE_PATH, "backup_data.pkl")


class Highscores:
    def __init__(self):
        self.date = str(datetime.datetime.today().date())
        self.day = datetime.datetime.today().date().day

        self.load_data()

    def exists_pickle(self):
        """Returns True if main pickle file exists."""

        return os.path.exists(PICKLE_PATH)

    def exists_backup(self):
        """Returns True if backup pickle file exists."""

        return os.path.exists(BACKUP_PATH)

    def load_data(self):
        """Loads pickle data to self.data if a pickle exists, otherwise it gives
        a default value to self.data."""

        if self.exists_pickle():
            path = PICKLE_PATH
        elif self.exists_backup():
            path = BACKUP_PATH
        else:
            self.data = {
                "daily-highscores": [f"{self.date}: 0"],
                "all-time-highscore": f"{self.date}: 0",
            }
            return None

        with open(path, "rb") as data_pickle:
            self.data = pickle.load(data_pickle)
            # Add highscore line for current day if one does not exist
            if self.data["daily-highscores"][-1].split()[0] == str(self.date):
                self.data["daily-highscores"].append(f"{self.date}: 0")

    def set_stats(self):
        """Sets current wpm stats from self.data."""

        self.today_wpm = int(self.data["daily-highscores"][-1].split()[-1])
        self.all_time_wpm = int(self.data["all-time-highscore"].split()[-1])

    def get_wpm(self):
        """Returns the daily and all time highest wpm.

        Used to display wpm scores on main menu.
        """

        self.set_stats()

        return self.today_wpm, self.all_time_wpm

    def make_backup(self):
        """Turns current pickle file into a backup file, and deletes old backup."""

        if self.exists_backup():
            os.remove(BACKUP_PATH)

        os.rename(PICKLE_PATH, BACKUP_PATH)

    def save_data(self):
        """Saves data to a pickle file."""

        if self.exists_pickle():
            self.make_backup()

        with open(PICKLE_PATH, "wb") as data_pickle:
            pickle.dump(self.data, data_pickle)

    def check_all_time_highscore(self, score: int) -> bool:
        """Returns True if highscore provided is greater than the all time highscore."""

        self.set_stats()

        return score > self.all_time_wpm

    def check_daily_highscore(self, score: int) -> bool:
        """Returns True if highscore provided is greater than today's highscore."""

        self.set_stats()

        return score > self.today_wpm

    def add_daily_highscore(self, score: int) -> None:
        """Adds a highscore to self.data for today."""

        # Remove old daily highscore
        self.data["daily-highscores"].pop()

        self.data["daily-highscores"].append(f"{self.date}: {score}")

    def add_all_time_highscore(self, score: int) -> None:
        """Adds a daily and all time highscore to self.data."""
        self.add_daily_highscore(score)

        self.data["all-time-highscore"] = f"{self.date}: {score}"

    def update(self, score: int) -> str:
        """Main function, checks if a given score is a highscore then saves that
        value to self.data and to a pickle file.

        Returns string representing whether value was a daily or all time highscore.
        """

        if self.check_all_time_highscore(score):
            self.add_all_time_highscore(score)
            self.save_data()
            return "all-time"

        elif self.check_daily_highscore(score):
            self.add_daily_highscore(score)
            self.save_data()
            return "daily"

        else:
            return "none"


if __name__ == "__main__":
    highscore = Highscores()

    print(highscore.update(1))
    print(highscore.update(2))
    print(highscore.update(1))
