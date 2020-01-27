import os


class Config:
    DEBUG = True
    FLASK_ADMIN_SWATCH = 'cosmo'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/healthrecord.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'FC7280EFF8F8462CA2DD3D485BE23BB2'

    SECURITY_REGISTERABLE = True
    SECURITY_REGISTER_URL = '/signup'
    SECURITY_LOGIN_URL = '/'
    SECURITY_POST_LOGIN_VIEW = '/progress'
    SECURITY_LOGOUT_URL = '/logout'
    SECURITY_POST_LOGOUT_VIEW = '/'
    SECURITY_RESET_URL = '/reset'
    SECURITY_CHANGE_URL = '/change'
    SECURITY_USER_IDENTITY_ATTRIBUTES = ['email']
    SECURITY_PASSWORD_SALT = '09B9356242454F91A8298B7C6E25960E'
    SECURITY_SEND_REGISTER_EMAIL = False

    @staticmethod
    def get(key, default=None):
        return os.environ.get(key, default)
