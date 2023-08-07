# File: cli.py
# Creation: Mon Aug  7 13:04:36 2023
# Time-stamp: <2023-08-07 15:36:10>
# Copyright (C): 2023 Pierre Lecocq

"""Command line interface for auth0_tokens."""

import argparse
from auth0_tokens import Auth0Tokens

parser = argparse.ArgumentParser(description ='Fetch Auth0 tokens for pre-configured profiles')

parser.add_argument('-n', '--name',
                    required = True,
                    action='store', dest='profile_name',
                    help='profile name configuration used to fetch the token', metavar='profile_name')

parser.add_argument('-c', '--config',
                    action='store', dest='config_file', default='./.profiles.json',
                    help='profiles configuration file path', metavar='config_file_path')

args = parser.parse_args()

auth0_tokens = Auth0Tokens(args.config_file)

token = auth0_tokens.fetch_token(args.profile_name)
if token is None:
    raise RuntimeError(f'Unable to fetch token for profile "{args.name}"')

print(token)
