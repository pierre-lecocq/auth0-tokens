# File: auth0_tokens.py
# Creation: Sun Aug  6 11:29:03 2023
# Time-stamp: <2023-08-07 13:09:30>
# Copyright (C): 2023 Pierre Lecocq

"""Fetch Auth0 tokens for pre-configured profiles."""

import json
import os
import stat

import requests

class Auth0Tokens:
    """Main class for Auth0 fetching tokens for pre-configured profiles."""

    def __init__(self, config_file):
        self.profiles_data = self.load_profiles_from_file(config_file)

    def load_profiles_from_file(self, file_path):
        """Load profiles data from configuration file."""
        if not os.path.isfile(file_path):
            raise RuntimeError(f'Missing profiles file (path: {file_path})')

        file_stat = os.stat(file_path)
        file_mode = file_stat.st_mode

        if not stat.S_IRUSR & file_mode:
            raise RuntimeError(f'Profiles file (path: {file_path}) is not readable')

        if ((stat.S_IRGRP & file_mode)
            or (stat.S_IWGRP & file_mode)
            or (stat.S_IXGRP & file_mode)
            or (stat.S_IROTH & file_mode)
            or (stat.S_IWOTH & file_mode)
            or (stat.S_IXOTH & file_mode)):
            raise RuntimeError(f'Profiles file ({file_path}) is not protected enough. Consider applying a 0400 mask to the file')

        with open(file_path, mode='r', encoding='utf-8') as file_descriptor:
            profiles = json.load(file_descriptor)

        return profiles

    def fetch_token(self, profile_name):
        """Fetch token for the profile given in class constructor arguments."""
        if not profile_name in self.profiles_data:
            raise RuntimeError(f'Unkown profile "{profile_name}"')

        profile = self.profiles_data[profile_name]

        response = requests.post(profile['issuer'] + '/oauth/token', json={
            'client_id': profile['client_id'],
            'client_secret': profile['client_secret'],
            'audience': profile['audience'],
            'grant_type': 'client_credentials'
        }, headers={
            'content-type': 'application/json'
        }, timeout=5)

        if not response.status_code == 200:
            raise RuntimeError(f'Bad request ({response.status_code} {response.reason})')

        json_body = response.json()

        if not 'access_token' in json_body:
            raise RuntimeError('Missing access_token key in response')

        return json_body['access_token']
