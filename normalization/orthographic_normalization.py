import arabic_script.elements as ase


def encoding_cleanup():
    raise NotImplementedError


def tatweel_removal(text):
    """
    The Tatweel (elongation) is used to stretch words to indicate
    prominence or simply to force vertical justification.
    This symbol has no effect on the meaning of the word so it's
    usually normalized.

    Examples:
        - A word without Tatweel:       جميل
        - The same word with Tatweel:   جـــمـــيـــل
    :param text: The text that we need to extract the Tatweel from.
    :return: A text without Tatweels.
    """
    if text is None:
        return None

    return text.replace(ase.TATWEEL, '')


def diacritic_removal(text):
    """
    Since diacritics occur so infrequently, they are considered noise
    by most researchers and are simply removed from the text.
    Examples:
        - A word without diacritics:     جميل
        - The same word with diacritics: جَمِيلٌ
    :param text: The text that we need to extract diacritics from.
    :return: A text without diacritics.
    """
    if text is None:
        return None

    for diacritic in ase.DIACRITICS:
        text = text.replace(diacritic, '')

    return text


def punctuation_removal(text):
    """
    Remove all punctuation marks from text
    :param text:
    :return: A punctuation-free text
    """
    if text is None:
        return None

    for mark in ase.PUNCTUATION_MARKS:
        if mark in ase.NUMBERS_PUNCTUATION_MARKS:
            continue

        text = text.replace(mark, '')

    return text


def letter_normalization(text, egyptian=False):
    """
    There are four letters in Arabic that are so often misspelled using
    variants that researchers find it more helpful to completely make
    these variants ambiguous (normalized).

    1. The Hamzated forms of Alif -> Alif.
    2. The Alif-Maqsura -> Ya (Only in Egypt).
    3. The Ta-Marbuta -> Ha.
    4. The non-Alif forms of Hamza -> Hamza letter.

    However, this is sometimes may be problematic. Let's take the
    name 'Ana' and the word 'Me' meaning for example, both words after
    normalization are gonna produce the same word which's not going
    to be interesting especially in named entity recognition.

     Examples:
       * Ana:
        - Correct form: آنا
        - After Normalization: انا
       * Me:
        - Correct form: أنا
        - After Normalization: انا

    :param text: The text we want to normalize its letters.
    :param egyptian: To flag if we want to normalize the Alif-Maqsura.
    :return: A letter-normalized string
    """
    if text is None:
        return None

    if egyptian:
        text = text.replace(ase.ALIF_MAQSURA, 'ي')

    for form in ase.ALEF_HAMZA_FORMS:
        text = text.replace(form, 'ا')

    text = text.replace(ase.TA_MARBUTA, 'ه')

    for form in ase.NON_ALIF_HAMZA_FORMS:
        text = text.replace(form, ase.HAMZA)

    return text


def clean_text(text):
        """
        Cleans the word by removing punctuations, diacritics, non-letter
        characters.
        :param text: The word to clean
        :return: A cleaned word that has nothing but letters.
        """
        if text is None:
            return None

        # Remove whitespace characters from the beginning and the end
        text = text.strip()

        for letter in text:
            if letter not in ase.LETTERS and letter != ' ':
                text = text.replace(letter, '')

        return text
