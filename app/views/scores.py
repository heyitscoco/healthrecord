from .base import BaseModelView
from app.models.scores import AnxietyScore
from app.models.scores import DepressionScore


class ScoreView(BaseModelView):

    can_create = False
    can_delete = False
    can_edit = False

    # TODO: figure out how to display the questionnaire type

    def __init__(self, model, **kwargs):
        name = self.get_name()
        endpoint = f'scores/{name.lower()}'
        super().__init__(
            model, name=name, endpoint=endpoint, category='Scores', **kwargs
        )

    @classmethod
    def get_name(cls):
        tokens = cls.__name__.split('ScoreView')
        return tokens[0] if tokens else None


class DepressionScoreView(ScoreView):
    def __init__(self, **kwargs):
        super().__init__(DepressionScore, **kwargs)


class AnxietyScoreView(ScoreView):
    def __init__(self, **kwargs):
        super().__init__(AnxietyScore, **kwargs)
