from bot.bot import start

from exception.exception import ConfigDoesNotExist
from parse_config.parse_config import parse


if __name__ == "__main__":
    try:
        token, backend, filename, model_name, size = parse("config", "config.yaml")
    except ConfigDoesNotExist as e:
        print(repr(e))
        exit()

    start(token, backend, filename, model_name, size)
