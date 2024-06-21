import os

from app.settings.config import LoggerSettings

root_path = os.path.abspath(os.curdir)
logs_path = os.path.join(root_path, "app/logs")

LOGGER_SETTINGS = LoggerSettings()
LOGGING_CONFIG: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "app.utils.logger.ColourizedFormatter",
            "fmt": "%(levelprefix)s %(asctime)s - [%(process)s] - %(name)s(%(lineno)d): %(message)s",
            "use_colors": True,
        },
        "console": {
            "()": "app.utils.logger.ColourizedFormatter",
            "fmt": "%(levelprefix)s %(asctime)s %(name)s: %(message)s",
            "use_colors": True,
        },
        "file_formatter": {
            "()": "app.utils.logger.ColourizedFormatter",
            "fmt": "%(levelprefix)s %(asctime)s - [%(process)s] - %(name)s(%(lineno)d): %(message)s",
            "use_colors": False,
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "console": {
            "formatter": "console",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "debug_file_handler": {
            "formatter": "file_formatter",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "filename": f"{logs_path}/debug.log",
            "when": "midnight",
            "interval": 1,
            "backupCount": 7,
            "encoding": "utf8",
        },
        "error_file_handler": {
            "formatter": "file_formatter",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "ERROR",
            "filename": f"{logs_path}/error.log",
            "when": "midnight",
            "interval": 1,
            "backupCount": 7,
            "encoding": "utf8",
        },
        "logstash": {
            "level": LOGGER_SETTINGS.logstash_log_level,
            "class": "logstash.TCPLogstashHandler",
            "host": LOGGER_SETTINGS.logstash_host,
            "port": LOGGER_SETTINGS.logstash_port,  # Default value: 50000
            "version": 1,
            "message_type": "logstash",  # 'type' field in logstash message. Default value: 'logstash'.
            "fqdn": False,  # Fully qualified domain name. Default value: false.
            "tags": [LOGGER_SETTINGS.app_tag],  # list of tags. Default: None.
        },
    },
    "loggers": {
        "app": {
            "handlers": [
                "console",
                "debug_file_handler",
                "error_file_handler",
                "logstash",
            ],
            "level": LOGGER_SETTINGS.app_log_level,
            "propagate": False,
        },
        "app.elk": {
            "handlers": [
                "console",
                "logstash",
            ],
            "level": LOGGER_SETTINGS.app_log_level,
            "propagate": False,
        },
        "app.database.mysql": {
            "handlers": [
                "console",
            ],
            "level": LOGGER_SETTINGS.app_log_level,
            "propagate": False,
        },
        "uvicorn": {
            "handlers": [
                "console",
            ],
            "level": LOGGER_SETTINGS.uvicorn_log_level,
            "propagate": False,
        },
        "celery": {
            "handlers": [
                "console",
                "logstash",
            ],
            "level": LOGGER_SETTINGS.app_log_level,
            "propagate": False,
        },
    },
}
