from flask import url_for
from flask_admin import Admin
from flask_admin import helpers as admin_helpers
from flask_security import Security
from flask_security import SQLAlchemyUserDatastore

from .create_app import create_app
from .models import db
from .models.users import Role
from .models.users import User
from .views import AnxietyQuestionnaireView
from .views import AnxietyScoreView
from .views import DepressionQuestionnaireView
from .views import DepressionScoreView
from .views import ProgressView

app = create_app()

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

admin = Admin(app, name='HealthRecord', template_mode='bootstrap3', url='/')

admin.add_view(DepressionQuestionnaireView())
admin.add_view(AnxietyQuestionnaireView())

admin.add_view(DepressionScoreView())
admin.add_view(AnxietyScoreView())

admin.add_view(ProgressView())


@app.before_first_request
def before_first_request():
    db.create_all()

# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for,
    )


if __name__ == '__main__':
    app.run()
