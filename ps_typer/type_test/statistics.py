import datetime
import time
from calendar import month_abbr

import pyqtgraph
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor

from ps_typer.data.highscores_data_handler import Highscore
from ps_typer.data.utils import GRAPH_MEASUREMENTS
from ps_typer.ui import stats_window

# CONSTANTS


class StatsWindow(QtWidgets.QWidget, stats_window.Ui_statsWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

    def _get_qcolors(self, colours: dict):
        """Converts the given dict of colours to a dict of QColor objects."""

        qcolours = dict()
        for name, colour in colours.items():
            qcolours[name] = QColor(colour)

        return qcolours

    def update_days_ago(self, days_ago: int) -> None:
        """Updates labelDaysAgo with a given number of days."""

        self.labelDaysAgo.setText(f"- {str(days_ago)} days ago")

    def set_up_graph(self, data: list[Highscore], colours: dict) -> None:
        """Sets up the graphView wpm over time graph with the given data."""

        self.colours = self._get_qcolors(colours)

        # Set up axes
        self.graphView.setLabel("left", "WPM")
        self.graphView.setAxisItems({"bottom": DateAxisItem(orientation="bottom")})

        # Save axes items to instance variables so they can be easily modified
        self.left_axis = self.graphView.getAxis("left")
        self.bottom_axis = self.graphView.getAxis("bottom")

        # Set the colours for the graph
        self.graphView.setBackground(None)
        self._set_axes_style(self.colours["axes"])

        # Set up curve of wpm against date
        self.curve = self.graphView.plot()
        self._set_data(data)
        self._update_graph()

    # Private Methods
    def _set_axes_style(
        self,
        colour: tuple,
        width=GRAPH_MEASUREMENTS["axis_width"],
        grid_alpha=GRAPH_MEASUREMENTS["grid_alpha"],
    ) -> None:
        """
        Sets the graph's axes colours to the provided tuple (rgb) and
        sets their alpha value.
        """

        self.left_axis.setTextPen(color=colour)
        self.left_axis.setPen(color=colour, width=width)
        self.left_axis.setGrid(grid_alpha)

        self.bottom_axis.setTextPen(color=colour)
        self.bottom_axis.setPen(color=colour, width=width)
        self.bottom_axis.setGrid(grid_alpha)

    def _get_time_stamp(self, datetime_object: datetime.datetime) -> int:
        """Returns a timestamp (int) from a given datetime object."""

        return int(time.mktime(datetime_object.timetuple()))

    def _get_datetime_object(self, date_str: str) -> datetime.datetime:
        """Takes a string in the format yyyy-mm-dd: and returns a datetime object."""

        raw_date: list[str] = date_str.replace(":", "").split("-")
        date_ints: list[int] = list(map(int, raw_date))

        return datetime.datetime(date_ints[0], date_ints[1], date_ints[2])

    def _clean_date(self, date_str: str) -> int:
        """
        Takes a string in the format 'yyyy-mm-dd:' and returns a usable timestamp
        representation.
        """

        return self._get_time_stamp(self._get_datetime_object(date_str))

    def _set_data(self, highscores: list[Highscore]) -> None:
        """
        Sets self.dates and self.wpms from the given data for daily highscores.

        Strings in the data list should be in the format 'yyyy-mm-dd: WPM'.
        """

        self.dates: list[int] = []
        self.wpms: list[int] = []

        # Add data for each day (data point) to 2 separate lists (2 axes)
        for highscore in highscores:
            self.dates.append(self._clean_date(highscore.date))
            self.wpms.append(highscore.score)

    def _update_graph(
        self, curve_width: int = GRAPH_MEASUREMENTS["curve_width"]
    ) -> None:
        """Updates self.curve with the data set in self._set_data."""

        self.curve.setData(
            x=self.dates,
            y=self.wpms,
            pen=pyqtgraph.mkPen(color=self.colours["curve"], width=curve_width),
            symbolBrush=pyqtgraph.mkBrush(color=self.colours["curve"]),
            symbolPen=pyqtgraph.mkPen(color=self.colours["curve"]),
            symbolSize=GRAPH_MEASUREMENTS["symbol_width"],
        )


class DateAxisItem(pyqtgraph.AxisItem):
    """
    Axis item to replace the x-axis in the above class's graphView item
    so that strings are used to represent the time stamp values plotted.
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Set up label for axis
        self.setLabel(text="Date Set", units=None)
        self.enableAutoSIPrefix(False)

    def _get_string(self, time_stamp: int) -> str:
        """Gets the string value which is to replace the given time_stamp value."""

        # types
        datetime_object: datetime.datetime
        list_from_time: list[str]
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

        return [self._get_string(value) for value in values]
