import os


class Config:
    DEBUG = bool(int(os.environ.get('BOT_DEBUG', '0')))
    COMMAND_PREFIX = os.environ.get('BOT_COMMAND_PREFIX', '/')

    PLUGINS_PATH = 'plugins'
    STORAGE_PATH = 'storage'

    CONNECTIONS = {}
