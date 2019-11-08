
class Development(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:password@127.0.0.1:5433/blog_api_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Production(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:password@127.0.0.1:5433/blog_api_db'

app_config = {
    'development': Development,
    'production': Production,
}
