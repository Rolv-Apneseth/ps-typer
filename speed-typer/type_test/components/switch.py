from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtProperty


class Switch(QtWidgets.QCheckBox):
    """A custom toggle switch widget which inherits from QCheckBox."""

    def __init__(
        self,
        bg_colour="#777777",
        circle_colour="#DDDDDD",
        active_bg_colour="#00BCFF",
        animation_curve=QtCore.QEasingCurve.InCurve,
        animation_duration=150,
    ):

        super().__init__()

        self._bg_colour = bg_colour
        self._circle_colour = circle_colour
        self._active_bg_colour = active_bg_colour

        # Size and Cursor
        self.setFixedSize(60, 28)
        self.setCursor(QtCore.Qt.PointingHandCursor)

        # Animation
        self._circle_position = 3
        self.animation = QtCore.QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(animation_duration)

        self.stateChanged.connect(self.start_transition)

    # Position property for animation
    @pyqtProperty(float)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()

    def start_transition(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - 26)
        else:
            self.animation.setEndValue(3)

        self.animation.start()

    def hitButton(self, pos):
        return self.contentsRect().contains(pos)

    def _paint(self, painter, colour):
        width = self.width()
        height = self.height()
        half_height = height / 2

        # Draw BG
        painter.setBrush(QtGui.QColor(colour))
        painter.drawRoundedRect(0, 0, width, height, half_height, half_height)

        # Draw circle
        painter.setBrush(QtGui.QColor(self._circle_colour))
        painter.drawEllipse(self._circle_position, 3, 22, 22)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtCore.Qt.NoPen)

        if self.isChecked():
            self._paint(painter, self._active_bg_colour)
        else:
            self._paint(painter, self._bg_colour)

        painter.end()
