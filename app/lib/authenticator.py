from fastapi import Depends
from typing import Dict


class AuthenticatorConfig():
    def __init__(self, users: Dict[str, str] = {}):
        self._users = users

    def users(self):
        return self._users


class Authenticator():
    def __init__(self, config: AuthenticatorConfig = Depends(AuthenticatorConfig)):
        self._config = config

    def authenticate(self, username: str, password: str):
        print(f"Authenticating {username}")
        print(f"Current users:", self._config.users())
        try:
            return self._config.users()[username] == password
        except KeyError as key_error:
            return False