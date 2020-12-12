class Config(object):
    FLASK_APP = 'run.py'
    CSRF_ENABLED = True
    DEBUG_MODE = False
    # FLASK_LOG = {
    #     'version': 1,
    #     'formatters': {
    #         'fmt': {
    #             'format': '[%(asctime)s][%(levelname)-5s] %(module)-12s: %(message)s'
    #         }
    #     },
    #     'handlers': {
    #         'console': {
    #             'class': 'logging.StreamHandler',
    #             'formatter': 'fmt',
    #             'stream': 'ext://sys.stdout',
    #             'level': 'DEBUG'
    #         }
    #     },
    #     'root': {
    #         'level': 'DEBUG',
    #         'handlers': ['console']
    #     }
    # }


class LocalConfig(Config):
    DEBUG_MODE = True


app_config = {
    'local': LocalConfig,
    'dev': Config
}
