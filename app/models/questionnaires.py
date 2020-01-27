from datetime import datetime

from sqlalchemy import event

from . import db
from .scores import AnxietyScore
from .scores import DepressionScore


RESPONCE_CHOICES = (
    'Not at all',
    'Several days',
    'More than half the days',
    'Nearly every day',
)

RESPONSE_MAPPING = {text: idx for idx, text in enumerate(RESPONCE_CHOICES)}


def question(text):
    return db.Column(text, db.Enum(*RESPONCE_CHOICES))


class QuestionnaireMixin:
    def score(self) -> int:
        score = 0
        for attr_name in dir(self):
            if not attr_name.startswith('question'):
                continue
            response = getattr(self, attr_name)
            if not response:
                continue
            score += RESPONSE_MAPPING[response]
        return score


class DepressionQuestionnaire(db.Model, QuestionnaireMixin):

    id = db.Column(db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)

    question1 = question('Little interest or pleasure in doing things')
    question2 = question('Feeling down, depressed, or hopeless')
    question3 = question('Trouble falling or staying asleep, or sleeping too much')
    question4 = question('Feeling tired or having little energy')
    question5 = question('Poor appetite or overeating')
    question6 = question(
        'Feeling bad about yourself   or that you are a failure orhave let yourself or your family down'
    )
    question7 = question(
        'Trouble concentrating on things, such as reading thenewspaper or watching television'
    )
    question8 = question(
        'Moving or speaking so slowly that other people could have noticed. Or the opposite being '
        'so figety or restless that you have been moving around a lot more than usual'
    )
    question9 = question(
        'Thoughts that you would be better off dead, or of hurting yourself'
    )


@event.listens_for(DepressionQuestionnaire, 'after_insert')
def score_depression_questionnaire(mapper, connection, target):
    score = DepressionScore(score=target.score(), entry=target.id)
    db.session.add(score)


class AnxietyQuestionnaire(db.Model, QuestionnaireMixin):

    id = db.Column(db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)

    question1 = question('Feeling nervous, anxious, or on edge')
    question2 = question('Not being able to stop or control worrying')
    question3 = question('Worrying too much about different things')
    question4 = question('Trouble relaxing')
    question5 = question("Being so restless that it's hard to sit still")
    question6 = question('Becoming easily annoyed or irritable')
    question7 = question('Feeling afraid as if something awful might happen')


@event.listens_for(AnxietyQuestionnaire, 'after_insert')
def score_anxiety_questionnaire(mapper, connection, target):
    score = AnxietyScore(score=target.score(), entry=target.id)
    db.session.add(score)
