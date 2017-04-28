
TATWEEL = 'ـ'
DIACRITICS = (
    'َ',  # Fatha
    'ُ',  # Damma
    'ِ',  # Kasra
    'ً',  # Tanween Fath
    'ٌ',  # Tanween Damm
    'ٍ',  # Tanween Kase
    'ْ',  # Sokoon
    'ّ',  # Shadda
)

WESTERN_ARABIC_DIGITS = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,)
INDO_ARABIC_DIGITS = ('٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩',)

DIGITS = WESTERN_ARABIC_DIGITS + INDO_ARABIC_DIGITS

ALEF_HAMZA_FORMS = ('أ', 'إ', 'آ',)
NON_ALIF_HAMZA_FORMS = ('ؤ', 'ئ',)
HAMZA = 'ء'
HAMZA_LETTERS = ALEF_HAMZA_FORMS + NON_ALIF_HAMZA_FORMS + (HAMZA,)

TA_MARBUTA = 'ة'
ALIF_MAQSURA = 'ى'
BASIC_LETTERS = (
    'ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش',
    'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه',
    'و', 'ي',
)

LETTERS = BASIC_LETTERS + HAMZA_LETTERS + \
          (TA_MARBUTA,) + (ALIF_MAQSURA, )

NUMBERS_PUNCTUATION_MARKS = ('ر',)
ARABIC_PUNCTUATION_MARKS = ('،', '؟', '؛')
OTHER_PUNCTUATION_MARKS = (
    ',', '~', '^', '(', '%', ')', '\'', '!', '÷', '\\', '.', '@', '=',
    '¡', '×', '<', '¿', '$', 'º', '&', '#', '>', '*', '_', '|', '+',
    ':', 'ø', ';', '-'
)

PUNCTUATION_MARKS = ARABIC_PUNCTUATION_MARKS + \
                    OTHER_PUNCTUATION_MARKS + NUMBERS_PUNCTUATION_MARKS

PREFIXES = ('ب', 'و', 'ا', 'ي', 'س', 'ت', 'ن', 'م', 'ف', 'ل', 'لل',)
SUFFIXES = ('ا', 'تي', 'ن', 'تن', 'كن', 'وا', 'ين', 'هما', 'ون',
            'ان', 'ما', 'ك', 'نا', 'ته', 'ات', 'ة', 'تما', 'هن',
            'ه', 'كم', 'ت', 'ي', 'ني', 'كما', 'ها', 'تا', 'هم', 'تم')