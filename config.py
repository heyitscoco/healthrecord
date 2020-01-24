import os

class Config():
    DEBUG = True
    FLASK_ADMIN_SWATCH = 'cosmo'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/healthrecord.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'FC7280EFF8F8462CA2DD3D485BE23BB2'

    @staticmethod
    def get(key, default=None):
        return os.environ.get(key, default)
