import json

CONFIG_FILE = "config/config.json"

ADDRESS = "address"
USER = "user"
PASSWORD = "password"
SERVER = "server"

# _config = None
# _mail_config = None


def _load(email=None, filepath=CONFIG_FILE):
    """ get key from json """
    # global _config, _mail_config
    try:
        with open(filepath, "r") as config_file:
            _config = json.load(config_file)
    except FileNotFoundError as FNFE:
        print(f"_load|KO|the file '{filepath}' does not exist")
        return False
    else:
        if email is None:
            email = next(iter(_config))
        _mail_config = _config.get(email)
        _mail_config[ADDRESS] = email
        if _mail_config:
            print(f"_load|OK|mail '{email}' found in file '{filepath}'")
            return _mail_config
        else:
            print(f"_load|KO|mail '{email}' NOT found in file '{filepath}'")
            return None


def get_config_pretty(email=None, filepath=CONFIG_FILE):
    config = _load(email, filepath)
    if config is not None:
        return json.dumps(config, indent=4)
    return None


def get_config(email=None, filepath=CONFIG_FILE):
    config = _load(email, filepath)
    if config is not None:
        return config
    return None


def get_user(email=None, filepath=CONFIG_FILE):
    config = _load(email, filepath)
    if config is not None:
        return config.get(USER)
    return None


def get_password(email=None, filepath=CONFIG_FILE):
    config = _load(email, filepath)
    if config is not None:
        return config.get(PASSWORD)
    return None


def get_server(email=None, filepath=CONFIG_FILE):
    config = _load(email, filepath)
    if config is not None:
        return config.get(SERVER)
    return None


def get_email(filepath=CONFIG_FILE):
    config = _load(None, filepath)
    if config is not None:
        return config.get(ADDRESS)
