from flask import abort
from flask import redirect
from flask import request
from flask import url_for
from flask_admin import BaseView as FlaskAdminBaseView
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user

from app.models import db


class BaseView(FlaskAdminBaseView):
    def is_accessible(self):
        return current_user.is_active and current_user.is_authenticated

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


class BaseModelView(BaseView, ModelView):
    def __init__(self, model, **kwargs):
        super().__init__(model, db.session, **kwargs)
