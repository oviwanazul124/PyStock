from enum import Enum

class search_mode(Enum):

    # This two first mode are commonly used on save.py and also on other files
    ID = "id"
    NAME = "name"

    # This are oriented to use on data_manipulation.py
    EXACT = "exact"
    MIN = "min"
    MAX = "max"
