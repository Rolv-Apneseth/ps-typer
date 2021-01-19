from PyQt5 import QtWidgets
from typing import List
import pyqtgraph
import datetime
import time
from calendar import month_abbr

from source_ui import stats_window

# CONSTANTS
AXIS_WIDTH = 1.5
CURVE_WIDTH = 2
GRID_ALPHA = 90
DEFAULT_BACKGROUND = (20, 20, 20)
DEFAULT_CURVE = (0, 170, 0)
DEFAULT_AXES = (225, 225, 225)


class StatsWindow(QtWidgets.QWidget, stats_window.Ui_statsWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

    def update_days_ago(self, days_ago: int):
        """Updates labelDaysAgo with a given number of days."""

        self.labelDaysAgo.setText(f"- Set {str(days_ago)} days ago")

    def set_up_graph(self, data: List[str]):
        """Sets up the graphView wpm over time graph with the given data."""

        # Set up axes
        self.graphView.setLabel("left", "WPM")
        self.graphView.setAxisItems({"bottom": DateAxisItem(orientation="bottom")})

        # Set axes items to instance variables so they can be easily modified
        self.left_axis = self.graphView.getAxis("left")
        self.bottom_axis = self.graphView.getAxis("bottom")

        # Set the default colours for the graph
        self.set_graph_background_colour(DEFAULT_BACKGROUND)
        self.set_axes_colour(DEFAULT_AXES)
        self.set_grid_alpha(GRID_ALPHA)

        # Set up curve of wpm against date set and colour it
        self.curve = self.graphView.plot()
        self.set_curve_colour(DEFAULT_CURVE)

        # Give the curve data and update the graph
        self.set_data(data)
        self.update_graph()

    def set_graph_background_colour(self, colour: tuple) -> None:
        """Sets the graph's background colour to the provided tuple (rgb)."""

        self.graphView.setBackground(background=colour)

    def set_curve_colour(self, colour: tuple) -> None:
        """Sets curve's colour to the provided tuple (rgb)."""

        self.curve.setPen(color=colour, width=CURVE_WIDTH)

    def set_axes_colour(self, colour: tuple) -> None:
        """Sets the graph's axes colours to the provided tuple (rgb)."""

        self.left_axis.setTextPen(color=colour)
        self.left_axis.setPen(color=colour, width=AXIS_WIDTH)

        self.bottom_axis.setTextPen(color=colour)
        self.bottom_axis.setPen(color=colour, width=AXIS_WIDTH)

    def set_grid_alpha(self, alpha: int) -> None:
        """
        Sets the alpha values (and turns on, if they are off) the grid
        lines for both x and y axes on the graph.
        """

        self.left_axis.setGrid(alpha)
        self.bottom_axis.setGrid(alpha)

    def get_time_stamp(self, datetime_object: datetime.datetime) -> int:
        """Returns a timestamp (int) from a given datetime object."""

        return int(time.mktime(datetime_object.timetuple()))

    def get_datetime_object(self, date_str: str) -> datetime.datetime:
        """Takes a string in the format yyyy-mm-dd: and returns a datetime object."""

        raw_date: List[str] = date_str.replace(":", "").split("-")
        date_ints: List[int] = list(map(int, raw_date))

        return datetime.datetime(date_ints[0], date_ints[1], date_ints[2])

    def clean_date(self, date_str: str) -> int:
        """
        Takes a string in thr format 'yyyy-mm-dd:' and returns a
        usable timestamp representation.
        """

        return self.get_time_stamp(self.get_datetime_object(date_str))

    def set_data(self, data: List[str]):
        """
        Sets self.dates and self.wpms from the given data for
        daily highscores.

        Strings in the data list should be in the format 'yyyy-mm-dd: WPM'.
        """

        self.dates: List[int] = []
        self.wpms: List[int] = []

        # Add data for each day (data point) to 2 seperate lists (2 axes)
        for day in data:
            split_day: List[str] = day.split()

            self.dates.append(self.clean_date(split_day[0]))
            self.wpms.append(int(split_day[1]))

    def update_graph(self):
        """Updates self.curve with the data set in self.set_data."""

        self.curve.setData(x=self.dates, y=self.wpms)


class DateAxisItem(pyqtgraph.AxisItem):
    """
    Axis item to replace the x-axis in the above class's graphView item
    so that strings are used to represent the time stamp values plotted.
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Set up label for axis
        self.setLabel(text="Day Set", units=None)
        self.enableAutoSIPrefix(False)

    def get_string(self, time_stamp: int) -> str:
        """Gets the string value which is to replace the given time_stamp value."""

        # types
        datetime_object: datetime.datetime
        list_from_time: List[str]
        month_name: str

        datetime_object = datetime.datetime.fromtimestamp(time_stamp)
        list_from_time = datetime_object.strftime("%m %d").split()

        month_name = month_abbr[int(list_from_time[0])]

        return " ".join((month_name, list_from_time[1]))

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
