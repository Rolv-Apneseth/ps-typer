from PyQt5 import QtWidgets
from typing import List
import pyqtgraph
import datetime
import time
from calendar import month_abbr

from source_ui import stats_window


class StatsWindow(QtWidgets.QWidget, stats_window.Ui_statsWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

    def update_days_ago(self, days_ago: int):
        """Updates labelDaysAgo with a given number of days."""

        self.labelDaysAgo.setText(f"- Set {str(days_ago)} days ago")

    def set_up_graph(self, data: List[str]):
        """Sets up the graphView wpm over time graph."""

        self.set_data(data)

        self.graphView.setLabel("left", "WPM")
        self.graphView.setAxisItems({"bottom": DateAxisItem(orientation="bottom")})

        self.curve = self.graphView.plot(pen="g")

        self.update_graph()

    def update_graph(self):
        """Updates self.curve with the data set in self.set_data."""

        x = self.dates
        y = self.wpms

        self.curve.setData(x=x, y=y)

    def get_time_stamp(self, datetime_object):
        """Returns a timestamp (int) from a given datetime object."""

        return int(time.mktime(datetime_object.timetuple()))

    def clean_date(self, date_str):
        """
        Takes a string in the format yyyy-mm-dd and returns a timestamp
        representing that date.
        """

        raw_date: List[int] = list(map(int, date_str.replace(":", "").split("-")))
        raw_datetime: datetime.datetime = datetime.datetime(
            raw_date[0], raw_date[1], raw_date[2]
        )
        time_stamp = self.get_time_stamp(raw_datetime)

        return time_stamp

    def set_data(self, data: List[str]):
        """
        Sets self.dates and self.wpms from the given data for
        daily highscores.

        Strings in the data list should be in the format 'yyyy-mm-dd WPM'.
        """

        self.dates: List[str] = []
        self.wpms: List[int] = []

        # Add data for each day (data point) to 2 seperate lists
        for day in data:
            split_day: List[str] = day.split()

            self.wpms.append(int(split_day[1]))
            self.dates.append(self.clean_date(split_day[0]))


class DateAxisItem(pyqtgraph.AxisItem):
    """
    Axis item to replace the x-axis in the above class's graphView item
    so that strings are used to represent the time stamp values plotted.
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.setLabel(text="Day Set", units=None)
        self.enableAutoSIPrefix(False)

    def get_string(self, time_stamp: int) -> str:
        """Gets the string value which is to replace the given time_stamp value."""

        list_from_time = (
            datetime.datetime.fromtimestamp(time_stamp).strftime(f"%m %d").split()
        )

        return " ".join([month_abbr[int(list_from_time[0])], list_from_time[1]])

    def tickStrings(self, values, scale, spacing):
        """
        Will change the axis tick values to be strings which represent
        the given time stamp values in the format of Month Day.
        """

        return [self.get_string(value) for value in values]


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = StatsWindow()
    window.show()

    app.exec_()
