# Copyright (C) Livia Muamba - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Livia Muamba, November 2025

import html
import json
import logging
import random
from typing import Union
from flask import Flask, request

from haversine import haversine

from data.departments import departments
from data.coordinates import coordinates_data
from constants.constants import ANSWER, ANSWER_DEP_CODE, APEX, APEX_INTERVAL_ERROR, ATTEMPTS, CLIENT_KEY, CLOSE_TO_TARGET, CLOSE_TO_TARGET_APEX, CLOSE_TO_TARGET_DISTANCE, CORRECT, DATA_SEPARATOR, DISTANCE, EAST_SYMBOL, EAST_WEST, FAR_FROM_TARGET, FAR_FROM_TARGET_APEX, FAR_FROM_TARGET_DISTANCE, FORMATTED_SEPARATOR, FOUND, GREATER_THAN, GUESS, INCORRECT, KILOMETER, LOWER_THAN, MAX_ALTITUDE, METER, MIN_ALTITUDE, NO_PRECISION, NO_SYMBOL, NORTH_SOUTH, NORTH_SYMBOL, POPULATION, POPULATION_INTERVAL_ERROR, POPULATION_TRANSLATOR, QUITE_CLOSE_TO_TARGET, QUITE_CLOSE_TO_TARGET_DISTANCE, ROUND_DISTANCE, SEAS_OCEANS, SEAS_OCEANS_TRANSLATOR, SOUTH_SYMBOL, WEST_SYMBOL
from session import Session

def create_app():
    app = Flask(__name__)
    session = Session(app)

    def select_answer() -> dict:
        keys = list(departments)
        r = random.randint(0, len(departments) - 1)
        return {ANSWER_DEP_CODE: keys[r], ANSWER: departments[keys[r]]}

    def get_department_data(key) -> dict:
        return departments.get(key)

    def get_population_interval(category) -> str:
        for k in POPULATION_TRANSLATOR:
            if k == category:
                return POPULATION_TRANSLATOR[k]
        return POPULATION_INTERVAL_ERROR

    def get_apex(guess) -> Union[int, str]:
        return guess if MIN_ALTITUDE < guess < MAX_ALTITUDE else APEX_INTERVAL_ERROR

    def more_or_less_symbol(guess, answer):
        if int(answer) > int(guess):
            return GREATER_THAN
        if int(answer) < int(guess):
            return LOWER_THAN
        return NO_SYMBOL

    def north_or_south_symbol(guess, answer):
        if guess < answer:  # target is further north
            return NORTH_SYMBOL
        if guess > answer:  # target is further south
            return SOUTH_SYMBOL
        return NO_SYMBOL 

    def east_or_west_symbol(guess, answer):
        if guess < answer:  # target is further east
            return EAST_SYMBOL
        if guess > answer:  # target is further west
            return WEST_SYMBOL
        return NO_SYMBOL  

    def formatted_seas_oceans(data) -> str:
        data = data.split(DATA_SEPARATOR)
        output = list()
        for so in data:
            output.append(SEAS_OCEANS_TRANSLATOR[so])
        return FORMATTED_SEPARATOR.join(output)

    def get_list_seas_oceans(data):
        return data.split(DATA_SEPARATOR)

    def get_precision_seas_oceans(guess, answer):
        guess = get_list_seas_oceans(guess)
        answer = get_list_seas_oceans(answer)
        if guess == answer:
            return CORRECT
        for so in guess:
            if so in answer:
                return FAR_FROM_TARGET
        return INCORRECT

    def round_5(d) -> int:
        return int(ROUND_DISTANCE * (d // ROUND_DISTANCE) if (abs(ROUND_DISTANCE * (d // ROUND_DISTANCE) - d)) < (ROUND_DISTANCE / 2) else (ROUND_DISTANCE * (d // ROUND_DISTANCE)) + ROUND_DISTANCE)

    def check_guess(dep_code, guess_data, client_key) -> json:
        formatted = dict()
        try:
            session.get_data(client_key=client_key)
        except KeyError:
            logging.error("check_guess: could not find client key in session")
        else:
            result = list()
            if session.already_tried(client_key=client_key, 
                                    dep_code=dep_code):
                return
            session.add_attempts(client_key=client_key,
                                attempt=dep_code)
            
            answer = session.get_answer(client_key)
            for k in answer:
                
                if k == APEX:
                    symbol = NO_SYMBOL
                    apex = get_apex(guess_data[k])
                    target = session.get_answer_field(client_key=client_key, field=k)
                    if apex != APEX_INTERVAL_ERROR:
                        symbol = more_or_less_symbol(guess_data[k], target)
                    if guess_data[k] == target:
                        precision = CORRECT
                    elif abs(guess_data[k] - target) < CLOSE_TO_TARGET_APEX:
                        precision = CLOSE_TO_TARGET
                    elif abs(guess_data[k] - target) < FAR_FROM_TARGET_APEX:
                        precision = FAR_FROM_TARGET
                    else:
                        precision = INCORRECT
                    formatted[APEX] = (str(guess_data[k]) + METER, symbol, precision)
                
                elif k == POPULATION:
                    symbol = NO_SYMBOL
                    population_interval = get_population_interval(guess_data[k])
                    target = session.get_answer_field(client_key=client_key, field=k)
                    if population_interval != POPULATION_INTERVAL_ERROR:
                        symbol = more_or_less_symbol(guess_data[k], target)
                    if guess_data[k] == target:
                        precision = CORRECT
                    else:
                        precision = INCORRECT
                    formatted[POPULATION] = (population_interval, symbol, precision)

                elif k == SEAS_OCEANS:
                    target = session.get_answer_field(client_key=client_key, field=k)
                    result.append({SEAS_OCEANS: (formatted_seas_oceans(guess_data[k]), get_precision_seas_oceans(guess_data[k], target))})
                    formatted[SEAS_OCEANS] = (formatted_seas_oceans(guess_data[k]), get_precision_seas_oceans(guess_data[k], target))

                else:
                    precision = CORRECT if guess_data[k] == session.get_answer_field(client_key=client_key, field=k) else INCORRECT
                    formatted[k] = (guess_data[k], precision)

            answer_dep_code = session.get_field(client_key=client_key, field=ANSWER_DEP_CODE)

            # distance
            distance = round_5(haversine(coordinates_data[dep_code], coordinates_data[answer_dep_code]))
            if isinstance(distance, int):
                if distance < ROUND_DISTANCE:
                    precision = CORRECT
                elif distance < CLOSE_TO_TARGET_DISTANCE:
                    precision = CLOSE_TO_TARGET
                elif distance < QUITE_CLOSE_TO_TARGET_DISTANCE:
                    precision = QUITE_CLOSE_TO_TARGET
                elif distance < FAR_FROM_TARGET_DISTANCE:
                    precision = FAR_FROM_TARGET
                else:
                    precision = INCORRECT
            formatted[DISTANCE] = (str(distance) + KILOMETER, precision)

            # north / south
            north_south_symbol = north_or_south_symbol(coordinates_data[dep_code][0], coordinates_data[answer_dep_code][0])
            formatted[NORTH_SOUTH] = (north_south_symbol, NO_PRECISION)

            # east / west
            east_west_symbol = east_or_west_symbol(coordinates_data[dep_code][1], coordinates_data[answer_dep_code][1])
            formatted[EAST_WEST] = (east_west_symbol, NO_PRECISION)

            formatted[FOUND] = dep_code == answer_dep_code
            formatted[ATTEMPTS] = session.get_nb_attempts(client_key=client_key)

        return json.dumps(formatted)

    @app.route('/api/init_session')
    def init_session():
        client_key = session.init_session(data=select_answer())
        return json.dumps(client_key)

    @app.route('/api/reset_session', methods=['POST'])
    def reset_session(): 
        req = request.get_json()
        session.remove_session(html.escape(str(req[CLIENT_KEY])))
        client_key = session.init_session(data=select_answer())
        return json.dumps(client_key)

    def sanitize_input(input):
        sanitized = input
        if CLIENT_KEY not in input:
            return
        if GUESS not in input:
            return
        sanitized[CLIENT_KEY] = html.escape(str(input[CLIENT_KEY]))
        sanitized[GUESS] = html.escape(str(input[GUESS]))
        return sanitized

    @app.route('/api/process_data', methods=['POST'])
    def process_data():
        req = request.get_json()
        sanitized = sanitize_input(req)
        if not sanitized:
            return json.dumps(list()) 
        guess_data = get_department_data(sanitized[GUESS])
        if guess_data:
            formatted_answer = check_guess(sanitized[GUESS], guess_data, sanitized[CLIENT_KEY])
        else:
            formatted_answer = []
        return json.dumps(formatted_answer)
    
    return app
    
app = create_app()
