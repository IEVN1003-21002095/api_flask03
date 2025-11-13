class DevelopmentConfig:
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'Alan'
    MYSQL_PASSWORD = '123456789'
    MYSQL_DB = 'api_utl'

config = {
    'development': DevelopmentConfig,
}