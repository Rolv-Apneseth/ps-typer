import random
from pathlib import Path
from typing import Generator

from ps_typer.data.utils import (PATH_TEXT_BROWN, PATH_TEXT_COMMON_PHRASES,
                                 PATH_TEXT_FACTS, PATH_TEXT_FAMOUS_LIT,
                                 PATH_TEXT_FAMOUS_QUOTES, PATH_TEXT_GUTENBERG,
                                 PATH_TEXT_WEBTEXT)

# CONSTANTS
RANDOM_TEXT_LINES: int = 3  # Number of lines from a text file to use for random text


# FUNCTIONS
def get_text_lines(text_file: Path) -> list[str]:
    """Returns a list of the lines of text in a given text file."""

    with open(text_file) as stream:
        return stream.read().splitlines()


def get_single_line_generator(text_file: Path) -> Generator:
    """Returns generator which yields 1 string from the given list per iteration."""

    lines: list[str] = get_text_lines(text_file)

    random.shuffle(lines)

    while True:
        for text in lines:
            yield text


def get_multi_line_generator(
    text_file: Path, num_lines: int = RANDOM_TEXT_LINES
) -> Generator:
    """
    Returns generator which yields a variable number of strings from the given list
    per iteration.

    The text is also formatted slightly.
    """

    if num_lines < 1:
        raise ValueError(
            f"The value for num_lines must be greater than 0, value given: {num_lines}"
        )

    lines: list[str] = get_text_lines(text_file)

    while True:
        # Break loop if the "lines" does not contain enough strings
        len_lines = len(lines)
        if len_lines < num_lines:
            break

        # Get a random index to start, and an end index based on "num_lines"
        index_start = int(random.random() * (len_lines - num_lines))
        index_end = index_start + num_lines

        # Cut random sentences from the "lines" random sentences
        rand_sentences = lines[index_start:index_end]
        del lines[index_start:index_end]

        raw_text = " ".join(rand_sentences)
        # Make sure first character is always capitalised if possible
        processed_text = f"{raw_text[0].upper()}{raw_text[1:]}"

        yield processed_text


_translate = {
    "Common Phrases": lambda: get_single_line_generator(PATH_TEXT_COMMON_PHRASES),
    "Facts": lambda: get_single_line_generator(PATH_TEXT_FACTS),
    "Famous Literature Excerpts": lambda: get_single_line_generator(
        PATH_TEXT_FAMOUS_LIT
    ),
    "Famous Quotes": lambda: get_single_line_generator(PATH_TEXT_FAMOUS_QUOTES),
    "Random Text: Brown": lambda: get_multi_line_generator(PATH_TEXT_BROWN),
    "Random Text: Gutenberg": lambda: get_multi_line_generator(PATH_TEXT_GUTENBERG),
    "Random Text: Webtext": lambda: get_multi_line_generator(PATH_TEXT_WEBTEXT),
}
