"""Functions for creating, transforming, and adding prefixes to strings."""

# 1


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """


    return "un" + word

add_prefix_un("manageable")


# 2
def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefix = ' :: ' + vocab_words[0]
    return prefix.join(vocab_words)


make_word_groups(['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric',
                  'complete', 'echolalia', 'encoder', 'biography'])

# 3


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    trimmed = word[:-4]
    
    if trimmed.endswith("i"):
       trimmed = trimmed[:-1] + "y"
    return trimmed



remove_suffix_ness('happiness')

# 4


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    verbed = sentence.split()[index]
    if verbed.endswith("."):
        verbed = verbed[:-1]
    verbed += "en"
    return verbed


adjective_to_verb("It got dark as the sun set.", 2)
