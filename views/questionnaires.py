from .base import BaseView
from models import db
from models.questionnaires import DepressionQuestionnaire


class QuestionnaireView(BaseView):
    form_args = {
        'question1': {'label': 'Little interest or pleasure in doing things'},
        'question2': {'label': 'Feeling down, depressed, or hopeless'},
        'question3': {'label': 'Trouble falling or staying asleep, or sleeping too much'},
        'question4': {'label': 'Feeling tired or having little energy'},
        'question5': {'label': 'Poor appetite or overeating'},
        'question6': {'label': 'Feeling bad about yourself   or that you are a failure orhave let yourself or your family down'},
        'question7': {'label': 'Trouble concentrating on things, such as reading thenewspaper or watching television'},
        'question8': {'label': 'Moving or speaking so slowly that other people could have noticed. Or the opposite being so figety or restless that you have been moving around a lot more than usual'},
        'question9': {'label': 'Thoughts that you would be better off dead, or of hurting yourself'},
    }


class DepressionQuestionnaireView(QuestionnaireView):

    def __init__(self, **kwargs):
        super().__init__(DepressionQuestionnaire, name='Depression', **kwargs)
