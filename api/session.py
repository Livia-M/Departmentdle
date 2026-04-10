# Copyright (C) Livia Muamba - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Livia Muamba, November 2025

__author__ = "Livia Muamba"
__copyright__ = "Copyright (C) 2025 Livia Muamba"
__license__ = "Private"
__version__ = "1.0"

import logging
import os
from typing import Optional
import uuid

from datetime import timedelta
from flask import session

from constants.constants import ANSWER, ANSWER_DEP_CODE, SECRET_KEY, SESSION_TTL_MINUTES, TRIED

def generate_key() -> str:
    return str(uuid.uuid4())


class Session:

    def __init__(self, app):
        app.secret_key = os.getenv(SECRET_KEY)
        app.config["SESSION_PERMANENT"] = False
        app.config["SESSION_TYPE"] = "filesystem"
        app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=SESSION_TTL_MINUTES)
        self._session = session
        self._attempts = dict()

    def init_session(self, data) -> str:
        client_key = generate_key()
        self.session[client_key] = dict()
        self.session[client_key][TRIED] = list()
        session[client_key][ANSWER_DEP_CODE] = data[ANSWER_DEP_CODE]
        session[client_key][ANSWER] = data[ANSWER]
        self.attempts[client_key] = list()
        return client_key

    def remove_session(self, client_key):
        try:
            del self.session[client_key]
        except KeyError:
            logging.error("remove_session: could find client_key in session")
        finally:
            try:
                del self.attempts[client_key]
            except KeyError:
                logging.error("remove_session: could find client_key in attempts")

    def add_attempts(self, client_key, attempt):
        try:
            self.attempts[client_key]
        except KeyError:
            logging.error("add_attempts: could not find client_key in attempts")
        else:
            self.attempts.get(client_key).append(attempt)

    def get_data(self, client_key) -> Optional[dict]:
        return self.session.get(client_key)

    def already_tried(self, client_key, dep_code) -> bool:
        if self.attempts.get(client_key):
            return dep_code in self.attempts[client_key]
        return False

    def get_answer(self, client_key) -> Optional[dict]:
        if self.session.get(client_key):
            return self.session.get(client_key).get(ANSWER)

    def get_answer_field(self, client_key, field) -> Optional[int|str]:
        return self.session.get(client_key, {}).get(ANSWER, {}).get(field)
    
    def get_field(self, client_key, field) -> Optional[dict|str|list]:
        return self.session.get(client_key, {}).get(field)

    def get_nb_attempts(self, client_key) -> int:
        return len(self.attempts.get(client_key, {}))

    # getters

    @property
    def session(self):
        return self._session
    
    @property
    def attempts(self):
        return self._attempts

    # setters

    @session.setter
    def session(self, value):
        self._session = value
        
    @attempts.setter
    def attempts(self, value):
        self._attempts = value
