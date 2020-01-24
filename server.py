from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from create_app import create_app
from views.questionnaires import DepressionQuestionnaireView

app = create_app()

admin = Admin(app, name='HealthRecord', template_mode='bootstrap3', url='/')
admin.add_view(DepressionQuestionnaireView())


if __name__ == '__main__':    
    app.run()
