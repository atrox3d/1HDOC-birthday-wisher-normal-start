########################################################################################################################
#
#   configmanager.py
#
#   problem:    use configuration data/credentials for smtp without versioning them for security reasons
#   solution:   .gitignore data folder
#               create a proxy(this module) between the code and the sensitive data
#               expose some handy methods to access configuration values
#
#   data example:
#
# {
#     "mail@server.com": {
#         "user": "mail",
#         "password": "p4ssw0rd",
#         "server": "smtp.server.com"
#     }
#     "mail2@server.com": {
#         "user": "mail2",
#         "password": "p4ssw0rd2",
#         "server": "smtp.server.com"
#     }
#     ...
# }
#
########################################################################################################################
import json

# default configuratio file path
CONFIG_FILE = "config/config.json"

# dictionary keys as string constants to avoid mistyping
ADDRESS = "address"
USER = "user"
PASSWORD = "password"
SERVER = "server"


def _load(email=None, filepath=CONFIG_FILE):
    """ get dictionary from json """
    try:
        with open(filepath, "r") as config_file:                # open config file and load json dict
            _config = json.load(config_file)
    except FileNotFoundError:
        print(f"_load|KO|the file '{filepath}' does not exist")
        return None                                             # no data file
    else:
        if email is None:
            email = next(iter(_config))                         # no email specified, get first dict key
        _mail_config = _config.get(email)                       # get configuration dict for key
        _mail_config[ADDRESS] = email                           # save email key as new key
        if _mail_config:
            print(f"_load|OK|mail '{email}' found in file '{filepath}'")
            return _mail_config                                 # config ok
        else:
            print(f"_load|KO|mail '{email}' NOT found in file '{filepath}'")
            return None                                         # mail not found


def get_config_pretty(email=None, filepath=CONFIG_FILE):
    """ get string representation for debug purposes """
    config = _load(email, filepath)
    if config is not None:
        return json.dumps(config, indent=4)
    return None


def get_config(email=None, filepath=CONFIG_FILE):
    """ get configuration dict """
    config = _load(email, filepath)
    if config is not None:
        return config
    return None


def get_user(email=None, filepath=CONFIG_FILE):
    """ get just the user """
    config = _load(email, filepath)
    if config is not None:
        return config.get(USER)
    return None


def get_password(email=None, filepath=CONFIG_FILE):
    """ get just the password """
    config = _load(email, filepath)
    if config is not None:
        return config.get(PASSWORD)
    return None


def get_server(email=None, filepath=CONFIG_FILE):
    """ get just the server """
    config = _load(email, filepath)
    if config is not None:
        return config.get(SERVER)
    return None


def get_email(filepath=CONFIG_FILE):
    """ get just the email """
    config = _load(None, filepath)
    if config is not None:
        return config.get(ADDRESS)
