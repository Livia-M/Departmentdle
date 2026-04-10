# Copyright (C) Livia Muamba - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Livia Muamba, November 2025

# secret

SECRET_KEY = "SECRET_KEY"

# session cleaning

SESSION_TTL_MINUTES = 30

LESS_THAN_30K_INT = 0
BETWEEN_30K_60K_INT = 1
BETWEEN_60K_100K_INT = 2
BETWEEN_100K_200K_INT = 3
MORE_THAN_200K_INT = 4

POPULATION_TRANSLATOR = {
    "0": "-30k",
    "1": "30k - 60k",
    "2": "60k - 100k",
    "3": "100k - 200k",
    "4": "+ 200k"
}

CLOSE_POPULATION = 1

# apex

MIN_ALTITUDE = 0
MAX_ALTITUDE = 4806

# keys

ANSWER = "answer"
ANSWER_DEP_CODE = "answer_dep_code"
APEX = "apex"
ATTEMPTS = "attempts"
CLIENT_KEY = "client_key"
DEPARTMENT = "department"
DISTANCE = "distance"
FOUND = "found"
GUESS = "guess"
POPULATION = "prefecture_pop"
SEA_OCEAN = "sea_ocean"
TRIED = "tried"

# precision

CLOSE_TO_TARGET = "close_to_target"
CORRECT = "correct"
FAR_FROM_TARGET = "far_from_target"
INCORRECT = "incorrect"
QUITE_CLOSE_TO_TARGET = "quite_close_to_target"

NO_PRECISION = "no_precision"

# distance close to target / far from target 

ROUND_DISTANCE = 5

CLOSE_TO_TARGET_DISTANCE = 100
QUITE_CLOSE_TO_TARGET_DISTANCE = 200
FAR_FROM_TARGET_DISTANCE = 300

# north_south east_west

NORTH_SOUTH = "north_south"
EAST_WEST = "east_west"

# apex close to target / far from target 

CLOSE_TO_TARGET_APEX = 375
FAR_FROM_TARGET_APEX = 750

# symbols

METER = "m"
KILOMETER = "km"
GREATER_THAN = "🔼"
LOWER_THAN = "🔽"

NORTH_SYMBOL = "🔼"
SOUTH_SYMBOL = "🔽"
EAST_SYMBOL = "▶️"
WEST_SYMBOL = "◀️"

NO_SYMBOL = ""

# seas / oceans

SEAS_OCEANS = "seas_oceans"

ATLANTIC_OCEAN = "atlantic_ocean"
CARIBBEAN_SEA = "caribbean_sea"
CELTIC_SEA = "celtic_sea"
ENGLISH_CHANNEL = "english_channel"
INDIAN_OCEAN = "indian_ocean"
IROISE_SEA = "iroise_sea"
MEDITERRANEAN_SEA = "mediterranean_sea"
NO_SEA_OCEAN = "none"
NORTH_SEA = "north_sea"

ATLANTIC_OCEAN_FR = "Atlantique"
CARIBBEAN_SEA_FR = "Caraïbes"
CELTIC_SEA_FR = "Celtique"
ENGLISH_CHANNEL_FR = "Manche"
INDIAN_OCEAN_FR = "Indien"
IROISE_SEA_FR = "Iroise"
MEDITERRANEAN_SEA_FR = "Méditerranée"
NO_SEA_OCEAN_FR = "Aucun"
NORTH_SEA_FR = "Nord"

SEAS_OCEANS_TRANSLATOR = {
    ATLANTIC_OCEAN: ATLANTIC_OCEAN_FR,
    CARIBBEAN_SEA: CARIBBEAN_SEA_FR,
    CELTIC_SEA: CELTIC_SEA_FR,
    ENGLISH_CHANNEL: ENGLISH_CHANNEL_FR,
    INDIAN_OCEAN: INDIAN_OCEAN_FR,
    IROISE_SEA: IROISE_SEA_FR,
    MEDITERRANEAN_SEA: MEDITERRANEAN_SEA_FR,
    NO_SEA_OCEAN: NO_SEA_OCEAN_FR,
    NORTH_SEA: NORTH_SEA_FR
}

# separators / join characters

DATA_SEPARATOR = ";"
FORMATTED_SEPARATOR = ", "

# error messages

POPULATION_INTERVAL_ERROR = "NaN"
APEX_INTERVAL_ERROR = "Invalid"
TRANSLATION_ERROR = "Translation error"
