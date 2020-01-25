from . import db


class DepressionScore(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    entry = db.Column(db.Integer, db.ForeignKey("depression_questionnaire.id"))


class AnxietyScore(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    entry = db.Column(db.Integer, db.ForeignKey("anxiety_questionnaire.id"))
