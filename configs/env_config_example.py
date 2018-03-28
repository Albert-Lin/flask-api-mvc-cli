"""
The schema (columns) and default example value
for "./EnvConfig". When "./EnvConfig.py"schema
be modified please also update this config example
file.
"""

# flask configuration
flask_config = {
    "host": "127.0.0.1",
    "port": 8888,
    "debug": True
}

# the configuration of white list for enable allow cross origin
flask_xss = {
    r"/*": {"origins": "http://soldata.semanticlab.com"}
}

# mongodb configuration:
mongodb_config = {
    "db_name": {
        "db": "db_name",
        "host": "host_ip",
        "port": 27017,
        "username": "user_name",
        "password": "user_password"
    },
}
