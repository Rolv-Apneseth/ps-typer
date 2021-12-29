from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEasingCurve, QPropertyAnimation, pyqtProperty
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QCheckBox


class Switch(QCheckBox):
    """A custom toggle switch widget which inherits from QCheckBox."""

    def __init__(
        self,
        bg_colour="#777777",
        active_bg_colour="#00BCFF",
        circle_colour="#DDDDDD",
        animation_curve=QEasingCurve.InCurve,
        animation_duration=150,
    ):

        super().__init__()

        # Colours
        self._active_bg_colour = QColor(active_bg_colour)
        self._bg_colour = QColor(bg_colour)
        self._circle_colour = QColor(circle_colour)
        self._focused_circle_colour = self._circle_colour.lighter(120)

        # Size and Cursor
        self.setFixedSize(60, 28)
        self.setCursor(Qt.PointingHandCursor)

        # Animation
        self._circle_position = 3
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(animation_duration)

        self.stateChanged.connect(self.start_transition)

        # Focus default value
        self._is_focused = False

    # Position property for animation
    @pyqtProperty(int)
    def circle_position(self):
        return round(self._circle_position)

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

    # FOCUS
    def focusInEvent(self, event):
        super().focusInEvent(event)
        self._is_focused = True

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self._is_focused = False

    def isFocused(self):
        """
        Convenience helper method, so focus can be checked for in the same way as
        self.isChecked() operates.
        """

        return self._is_focused

    # PAINT
    def _paint(self, painter, bg_colour, circle_colour):
        """Helper method for self.PaintEvent()."""
        width = self.width()
        height = self.height()
        half_height = height // 2

        # Draw BG
        painter.setBrush(bg_colour)
        painter.drawRoundedRect(0, 0, width, height, half_height, half_height)

        # Draw circle
        painter.setBrush(circle_colour)
        painter.drawEllipse(self._circle_position, 3, 22, 22)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        bg_colour = self._active_bg_colour if self.isChecked() else self._bg_colour

        circle_colour = (
            self._focused_circle_colour if self.isFocused() else self._circle_colour
        )

        self._paint(painter, bg_colour, circle_colour)

        painter.end()
