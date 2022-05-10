DARK_MODE = dict(
    base=dict(
        bg="hsl(217, 35%, 17%)",
        bg_lighter="hsl(217, 35%, 25%)",
        text="hsl(0, 0%, 85%)",
        text_button="hsl(0, 0%, 62%)",
    ),
    rich_text=dict(
        green="hsl(124, 70%, 21%)",
        red="hsl(0, 65%, 38%)",
    ),
    graph=dict(
        axes="#d9d9d9",
        curve="#136c19",
    ),
)
LIGHT_MODE = dict(
    base=dict(
        bg="hsl(217, 35%, 84%)",
        bg_lighter="hsl(217, 35%, 94%)",
        text="hsl(0, 0%, 14%)",
        text_button="hsl(0, 0%, 47%)",
    ),
    rich_text=dict(
        green="hsl(124, 60%, 45%)",
        red="hsl(0, 80%, 55%)",
    ),
    graph=dict(
        axes="#000000",
        curve="#1ca025",
    ),
)
SWITCH_COLOURS = dict(
    bg_colour="#9e9e9e",
    circle_colour="#d9d9d9",
    active_bg_colour="#3381ff",
)


# FUNCTIONS -----------------------------------------------------------------------------
def get_colours(is_dark_mode: bool = True) -> dict[str, dict[str, str]]:
    """Returns dictionary of of all colours used for program."""

    return dict(DARK_MODE if is_dark_mode else LIGHT_MODE, switch=SWITCH_COLOURS)


def get_style_sheet(
    bg: str = "", bg_lighter: str = "", text: str = "", text_button: str = ""
) -> str:
    """
    Returns a string representing the style sheet.

    Usage: get_style_sheet(True) for dark mode or get_style_sheet(False) for light mode
    """

    return f"""QWidget {{
            background: {bg};
            color: {text};
            font-size: 24pt;
            font-weight: bold;
            font-family: "Inconsolata Bold";
        }}
        QPushButton, QComboBox {{
            background: transparent;
            font-size: 25pt;
            border-radius: 5;
            padding: 8px;
            text-align: left;
            color: {text_button};
        }}
        QPushButton::hover, QComboBox::hover, QPushButton::focus, QComboBox::focus {{
            background: transparent;
            color: {text};
            outline: none;
        }}
        QComboBox::down-arrow {{
            background: transparent;
        }}
        QComboBox::item {{
            background: {bg_lighter};
        }}
        QComboBox::item:selected {{
            font-weight: bold;
            color: {text};
        }}
        QLabel, QRadioButton, QScrollArea, QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical, #graphView {{
            background: transparent;
            border: none;
        }}
        QScrollBar {{
            background: {bg};
        }}
        QScrollBar::handle {{
            background: {text_button};
            border: none;
        }}
        QScrollBar::handle:pressed {{
            background: {text};
        }}
        #labelMainMenu, #labelTitle, #labelStatistics {{
            font-size: 50pt;
        }}
        #labelDaysAgo {{
            color: {text_button}
        }}"""
