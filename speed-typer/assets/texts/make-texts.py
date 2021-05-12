from pathlib import Path
import re


# PATHS
TEXTS_FOLDER = Path(__file__).absolute().parent
BROWN = TEXTS_FOLDER / "brown.txt"
WEBTEXT = TEXTS_FOLDER / "webtext.txt"
GUTENBERG = TEXTS_FOLDER / "gutenberg.txt"


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
    from nltk.corpus import brown
    from nltk.corpus import webtext
    from nltk.corpus import gutenberg


# CONSTANTS
SENTENCE_MIN_LEN = 4
SENTENCE_MAX_LEN = 275
REPLACE_SYMBOLS = {
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
    " -- ": "--",
    " !": "!",
    "!!": "!",
    " ' ": "'",
    "` ": "'",
    """"'""": "'",
    """"`""": "'",
}

REMOVE_SYMBOLS = [
    " ''",
    "'' ",
    " ``",
    "``",
    "`'",
]

DISALLOWED_WORDS = [
    "nigg",
    "Nigg",
]


# FUNCTIONS
def replace_from_text(raw_text: str, symbols: dict) -> str:
    """
    Replace every symbol/character in the keys of the given symbols dictionary
    with the corresponding value for each key, from the given string raw_text.
    """

    for symbol in symbols:
        if symbol in raw_text:
            raw_text = raw_text.replace(symbol, symbols[symbol])

    return raw_text


def remove_from_text(raw_text: str, symbols: list) -> str:
    """
    Removes every symbol/character in the given symbols list from a given string,
    raw_text.
    """

    return re.sub("|".join(symbols), "", raw_text)


def clean_text(raw_text: str) -> str:
    """
    Takes a raw string from having joined words from an nltk corpus
    using, for example " ".join(words), and returns a more cleaned
    version of the text.

    This is achieved by replacing and removing certain symbols so that
    the text reads more like normal written English.
    """

    return remove_from_text(
        replace_from_text(raw_text, REPLACE_SYMBOLS), REMOVE_SYMBOLS
    )


def generate_corpus_text(corpus, filename: Path) -> None:
    """
    Generates a text file of the given filename (absolute path) from the given
    corpus.
    """
    # Get a list of sentences from the corpus
    raw_sentences = corpus.sents()

    processed_sentences = []
    for sentence in raw_sentences:
        joined_sentence = " ".join(word for word in sentence)

        processed_sentence = f"{clean_text(joined_sentence).strip()}\n"

        # Checks for sentence length and whether sentence contains an unallowed word
        conditions_met = SENTENCE_MIN_LEN <= len(
            processed_sentence
        ) <= SENTENCE_MAX_LEN and not any(
            (word in processed_sentence) for word in DISALLOWED_WORDS
        )

        if conditions_met:
            processed_sentences.append(processed_sentence)

    # Write the processed sentences to a text file
    with open(filename, "wt") as corpus_file:
        corpus_file.writelines(processed_sentences)


if __name__ == "__main__":
    # Generate brown corpus text
    generate_corpus_text(brown, BROWN)
    # Generate webtext corpus text
    generate_corpus_text(webtext, WEBTEXT)
    # Generate gutenberg corpus text
    generate_corpus_text(gutenberg, GUTENBERG)
