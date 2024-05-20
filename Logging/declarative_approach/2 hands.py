import sys

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(asctime)s - %(name)s - %(lineno)s - %(levelname)s - %(message)s",
        }
    },
    "handlers": {
        "screen": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            "stream": sys.stdout
        },
        "file_debug": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "calc_debug.log",
            "mode": "a"
        },
        "file_error": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "base",
            "filename": "calc_error.log",
            "mode": "a"
        }
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["screen", "file_debug", "file_error"],
        },
        "utils": {
            "level": "DEBUG",
            "handlers": ["screen", "file_debug", "file_error"],
        }
    },
}
