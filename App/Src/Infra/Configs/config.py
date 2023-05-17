import os
from configparser import ConfigParser


def config_database(section: str = 'postgresql') -> str:
    def get_string_connection(db: dict) -> str:
        pattern = 'dialect+driver://username:password@host:port/database'

        for key, value in db.items():
            pattern = pattern.replace(key, value)

        return pattern

    path = ['Src', 'Infra', 'Configs', 'database.ini']
    full_file_path = os.path.join(os.getcwd(), *path)

    parser = ConfigParser()
    parser.read(full_file_path)

    if parser.has_section(section):
        params = parser.items(section)

        db_params = {param[0]: param[1] for param in params}

        return get_string_connection(db_params)
