# Auth0 Tokens

Fetch Auth0 tokens for pre-configured profiles

## Configuration

Example of a JSON configuration file:

```
{
    "profile1": {
        "issuer": "https://profile1.us.auth0.com",
        "client_id": "profile1Id",
        "client_secret": "profile1Secret",
        "audience": "http://profile1.com"
    },
    "profile2": {
        "issuer": "https://profile2.us.auth0.com",
        "client_id": "profile2Id",
        "client_secret": "profile2Secret",
        "audience": "http://profile2.com"
    }
}

```

## Usage

```
usage: cli.py [-h] -n profile_name [-c config_file_path]

Fetch Auth0 tokens for pre-configured profiles

options:
  -h, --help            show this help message and exit
  -n profile_name, --name profile_name
                        profile name configuration used to fetch the token
  -c config_file_path, --config config_file_path
                        profiles configuration file path
```

## Examples

```
python3 cli.py --config profiles.json --name profile1
```
