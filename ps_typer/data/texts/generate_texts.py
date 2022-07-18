import re
from pathlib import Path
from string import ascii_letters

from ps_typer.data.utils import PATH_TEXT_BROWN, PATH_TEXT_GUTENBERG, PATH_TEXT_WEBTEXT

# Nltk corpora for 'random' texts
CORPORA = [
    "brown",
    "webtext",
    "gutenberg",
]
try:
    # Check if nltk corpora are downloaded
    from nltk import corpus

    corpus.brown.ensure_loaded()
    corpus.webtext.ensure_loaded()
    corpus.gutenberg.ensure_loaded()

except LookupError:
    # Download nltk corpora
    from nltk import download

    for corpus in CORPORA:
        download(corpus)

    # Used for splitting texts into sentences
    download("punkt")

finally:
    # Import corpora
    from nltk.corpus import brown, gutenberg, webtext

    # Remove certain texts from corpora
    for fileid in [
        "bible-kjv.txt",
        "blake-poems.txt",
        "bryant-stories.txt",
        "melville-moby_dick.txt",
        "shakespeare-caesar.txt",
        "shakespeare-hamlet.txt",
        "shakespeare-macbeth.txt",
        "whitman-leaves.txt",
    ]:
        gutenberg._fileids.remove(fileid)

    for fileid in [
        "grail.txt",
        "pirates.txt",
        "singles.txt",
        "wine.txt",
    ]:
        webtext._fileids.remove(fileid)


# CONSTANTS
SENTENCE_MIN_LEN: int = 25
SENTENCE_MAX_LEN: int = 275

REPLACE_SYMBOLS: dict = {
    " ,": ",",
    ",,": ",",
    " .": ".",
    " ?": "?",
    "??": "?",
    "( ": "(",
    " )": ")",
    " ;": ";",
    ";;": ";",
    " :": ":",
    " !": "!",
    "!!": "!",
    " ' ": "'",
    "` ": "'",
    """"'""": "'",
    """"`""": "'",
    "'''": "'",
    " -- ": "-",
    " - ": "-",
    ";--": "-",
    ".--": "-",
    "!--": "-",
    ",--": "-",
    "...": "....",
    "....": ".....",
    "..": ".",
}

PATTERN_REMOVE: re.Pattern = re.compile(
    "|".join(
        [
            " ''",
            "'' ",
            " ``",
            "``",
            "`'",
            "-- ",
            r"^-",
            r'(?<!")"$',
        ]
    )
)

PATTERN_DISALLOWED: re.Pattern = re.compile(
    "|".join(
        [
            r"[-\s]af[.,;:\s]",
            r"^af[.,;:\s]",
            r"bitch|cunt|fuck|nigg|retarded|shit|whore",
        ]
    ),
    flags=re.IGNORECASE,
)


# FUNCTIONS
def replace_from_text(raw_text: str) -> str:
    """
    Replace every key of the REPLACE_SYMBOLS with it's corresponding value
    in the given raw_text.
    """

    for symbol in REPLACE_SYMBOLS:
        if symbol in raw_text:
            raw_text = raw_text.replace(symbol, REPLACE_SYMBOLS[symbol])

    return raw_text


def remove_from_text(raw_text: str) -> str:
    """
    Removes every symbol/character which matches the pattern PATTERN_REMOVE
    from the given raw_text.
    """

    return PATTERN_REMOVE.sub("", raw_text)


def clean_text(raw_text: str) -> str:
    """
    Takes a raw string from having joined words from an nltk corpus
    using, for example " ".join(words), and returns a more cleaned
    version of the text.

    This is achieved by replacing and removing certain symbols so that
    the text reads more like normal written English.
    """

    return remove_from_text(replace_from_text(raw_text))


def validate_corpus_sentence(sentence: str) -> bool:
    """Returns True if sentence is valid i.e. meets all criteria."""

    is_correct_length = SENTENCE_MIN_LEN < len(sentence) <= SENTENCE_MAX_LEN
    starts_with_letter = sentence[0] in ascii_letters
    does_not_end_with_letter = is_correct_length and sentence[-2] not in ascii_letters
    has_no_disallowed_patterns = not PATTERN_DISALLOWED.search(sentence)

    return all(
        [
            is_correct_length,
            starts_with_letter,
            does_not_end_with_letter,
            has_no_disallowed_patterns,
        ]
    )


def generate_corpus_text(corpus, filename: Path) -> None:
    """
    Generates a text file of the given filename (absolute path) from the given
    corpus.
    """
    # Get a list of sentences from the corpus
    raw_sentences = corpus.sents()

    with open(filename, "wt") as corpus_file:
        for sentence in raw_sentences:
            joined_sentence = " ".join(word for word in sentence)

            if not joined_sentence:
                continue

            processed_sentence = f"{clean_text(joined_sentence).strip()}\n"

            if validate_corpus_sentence(processed_sentence):
                corpus_file.write(processed_sentence)


def main():
    generate_corpus_text(brown, PATH_TEXT_BROWN)
    generate_corpus_text(webtext, PATH_TEXT_WEBTEXT)
    generate_corpus_text(gutenberg, PATH_TEXT_GUTENBERG)


if __name__ == "__main__":
    main()
