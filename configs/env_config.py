"""
The configurations for local develop environment,
the schema (columns) & information could find in
"./EnvConfigExample.py". Because this config file will
be ignored by Git, when this config file schema be
modified, please update the "./EnvConfigExample.py"
"""


flask_config = {
    "host": "127.0.0.1",
    "port": 8888,
    "debug": True
}

flask_xss = {
    r"/*": {"origins": ""}
}

mongodb_config = {
}
