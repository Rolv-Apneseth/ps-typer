import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta

from ps_typer.data.utils import (OPTIONS_HIGHSCORES, PATH_USER_DATA_DB,
                                 get_datetime_from_str, get_today)

# SQL -----------------------------------------------------------------------------------
COMMANDS = dict(
    create_table="""CREATE TABLE IF NOT EXISTS highscores (
            date timestamp PRIMARY KEY,
            score INTEGER NOT NULL,
            is_all_time INTEGER DEFAULT NULL
            );""",
    create_index="""CREATE UNIQUE INDEX
            IF NOT EXISTS
            all_time_index ON highscores(is_all_time)
            where is_all_time = 1;""",
    add_row="""INSERT INTO 'highscores'
            ('score', 'date')
            VALUES (?, ?);""",
    del_row="""DELETE FROM 'highscores'
            WHERE {0}=?;""",
    update_row="""UPDATE 'highscores'
            SET {0}=?
            WHERE {1}=?;""",
    del_all="""DELETE FROM 'highscores';""",
)

QUERIES = dict(
    all="""SELECT * FROM highscores;""",
    single_row="""SELECT * FROM highscores WHERE {0}=?;""",
)


# MODEL ---------------------------------------------------------------------------------
@dataclass
class Highscore:
    date: str
    score: int
    is_all_time: int | None


# DATA HANDLER --------------------------------------------------------------------------
class HighscoreDataHandler:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn
        self.cursor = self.conn.cursor()

        self.cursor.execute(COMMANDS["create_table"])
        self.cursor.execute(COMMANDS["create_index"])

    def _insert_highscore(self, score: int) -> None:
        self.cursor.execute(COMMANDS["add_row"], (score, get_today()))
        self.conn.commit()

    def _get_highscore(self, field: str, value: str | int | None) -> Highscore | None:
        self.cursor.execute(QUERIES["single_row"].format(field), (value,))
        row: tuple | None = self.cursor.fetchone()

        return Highscore(*row) if row else None

    def _update_highscore(
        self,
        field: str,
        value: str | int | None,
        identifier_field: str,
        identifier_value: str | int | None,
    ):
        self.cursor.execute(
            COMMANDS["update_row"].format(field, identifier_field),
            (value, identifier_value),
        )
        self.conn.commit()

    def _update_highscore_todays(self, score: int) -> None:
        self._update_highscore("score", score, "date", get_today())
        self.conn.commit()

    def _set_highscore_all_time(self):
        self._update_highscore("is_all_time", 1, "date", get_today())
        self.conn.commit()

    def _update_highscore_all_time(self) -> None:
        self._update_highscore("is_all_time", None, "is_all_time", 1)
        self._set_highscore_all_time()

    # PUBLIC
    def get_all_highscores(self) -> list[Highscore]:
        self.cursor.execute(QUERIES["all"])

        return [Highscore(*row) for row in self.cursor.fetchall()]

    def get_highscore_todays(self) -> Highscore | None:
        return self._get_highscore("date", get_today())

    def get_highscore_all_time(self) -> Highscore | None:
        return self._get_highscore("is_all_time", 1)

    def new_highscore(self, score: int) -> str:
        # None
        highscore_row_todays: Highscore | None = self.get_highscore_todays()
        if highscore_row_todays and highscore_row_todays.score >= score:
            return OPTIONS_HIGHSCORES[0]

        # Set todays if none found
        if not highscore_row_todays:
            self._insert_highscore(score)

        # Update todays after getting all time (if todays highscore = all time highscore)
        highscore_row_all_time: Highscore | None = self.get_highscore_all_time()
        self._update_highscore_todays(score)

        if highscore_row_all_time:
            if score > highscore_row_all_time.score:
                self._update_highscore_all_time()
            else:
                # Today's highscore
                return OPTIONS_HIGHSCORES[1]
        else:
            self._set_highscore_all_time()

        # All time higghscore
        return OPTIONS_HIGHSCORES[2]

    def delete_all_highscores(self) -> None:
        self.cursor.execute(COMMANDS["del_all"])
        self.conn.commit()

    def delete_highscore(self, date: str) -> None:
        self.cursor.execute(COMMANDS["del_row"].format("date"), (date,))
        self.conn.commit()

    def days_since_set(self) -> int:
        """Returns the number of days since the all-time highscore was set."""

        datetime_today: datetime = datetime.today()

        all_time_highscore: Highscore | None = self.get_highscore_all_time()
        datetime_all_time: datetime = (
            get_datetime_from_str(all_time_highscore.date)
            if all_time_highscore
            else datetime_today
        )

        time_delta: timedelta = datetime_today - datetime_all_time

        return time_delta.days

    def get_wpm(self) -> tuple:
        """Returns the daily and all time highest wpm scores."""

        highscore_today: Highscore | None = self.get_highscore_todays()
        highscore_all_time: Highscore | None = self.get_highscore_all_time()

        return (
            highscore_today.score if highscore_today else 0,
            highscore_all_time.score if highscore_all_time else 0,
        )
