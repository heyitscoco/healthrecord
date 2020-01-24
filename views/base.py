from flask_admin.contrib.sqla import ModelView
from models import db


class BaseView(ModelView):
    def __init__(self, model, **kwargs):
        super().__init__(model, db.session, **kwargs)
