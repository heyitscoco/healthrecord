from .base import BaseModelView
from app.models.questionnaires import AnxietyQuestionnaire
from app.models.questionnaires import DepressionQuestionnaire


class QuestionnaireView(BaseModelView):
    can_edit = False
    can_delete = False
    can_view_details = True

    def __init__(self, *args, name=None, **kwargs):
        name = self.get_name()
        endpoint = name.lower()
        super().__init__(*args, name=name, endpoint=endpoint, **kwargs)

    @classmethod
    def get_name(cls):
        tokens = cls.__name__.split('QuestionnaireView')
        return tokens[0] if tokens else None


class DepressionQuestionnaireView(QuestionnaireView):

    form_args = {
        'question1': {'label': 'Little interest or pleasure in doing things'},
        'question2': {'label': 'Feeling down, depressed, or hopeless'},
        'question3': {'label': 'Trouble falling or staying asleep, or sleeping too much'},
        'question4': {'label': 'Feeling tired or having little energy'},
        'question5': {'label': 'Poor appetite or overeating'},
        'question6': {
            'label': (
                'Feeling bad about yourself or that you are a failure or have let '
                'yourself or your family down'
            )
        },
        'question7': {'label': 'Trouble concentrating on things, such as reading thenewspaper or watching television'},
        'question8': {
            'label': (
                'Moving or speaking so slowly that other people could have noticed. '
                'Or the opposite being so figety or restless that you have been moving '
                'around a lot more than usual'
            )
        },
        'question9': {'label': 'Thoughts that you would be better off dead, or of hurting yourself'},
    }

    # TODO: Fix this
    # form_overrides = {colname: RadioField for colname in form_args}

    def __init__(self, **kwargs):
        super().__init__(DepressionQuestionnaire, **kwargs)


class AnxietyQuestionnaireView(QuestionnaireView):

    form_args = {
        'question1': {'label': 'Feeling nervous, anxious, or on edge'},
        'question2': {'label': 'Not being able to stop or control worrying'},
        'question3': {'label': 'Worrying too much about different things'},
        'question4': {'label': 'Trouble relaxing'},
        'question5': {'label': "Being so restless that it's hard to sit still"},
        'question6': {'label': 'Becoming easily annoyed or irritable'},
        'question7': {'label': 'Feeling afraid as if something awful might happen'},
    }

    def __init__(self, **kwargs):
        super().__init__(AnxietyQuestionnaire, **kwargs)
