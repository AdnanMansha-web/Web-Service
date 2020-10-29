import configparser

cfg = configparser.ConfigParser()
try:
    print(f'Reading config from "api_server_config.ini"')
    cfg.read('api_server_config.ini')

    BASE_URL = cfg.get('general', 'base_url', fallback='')
    DEBUG = cfg.getboolean('general', 'debug', fallback=False)

    STANDALONE_HOST = cfg.get('standalone', 'host', fallback='127.0.0.1')
    STANDALONE_PORT = cfg.get('standalone', 'port', fallback=3333)

    AUTH_TOKEN = cfg.get('authorization', 'token', fallback='')
except Exception as e:
        print("Invalid or missing configuration file: ", str(e))
        exit(-1)
