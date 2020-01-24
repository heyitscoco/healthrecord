from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from create_app import create_app
from views.questionnaires import DepressionQuestionnaireView, AnxietyQuestionnaireView

app = create_app()

admin = Admin(app, name='HealthRecord', template_mode='bootstrap3', url='/')
admin.add_view(DepressionQuestionnaireView())
admin.add_view(AnxietyQuestionnaireView())


if __name__ == '__main__':    
    app.run()
