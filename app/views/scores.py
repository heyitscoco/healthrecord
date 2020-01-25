from .base import BaseView
from models.scores import DepressionScore, AnxietyScore


class ScoreView(BaseView):

    can_create = False
    can_delete = False
    can_edit = False

    # TODO: figure out how to display the questionnaire type
    # form_ajax_refs = {
    #     'entry': {
    #         'fields': ['id'], # ['name', 'created_at'],
    #         'page_size': 10
    #     }
    # }

    def __init__(self, model, **kwargs):
        super().__init__(model, category="Scores", **kwargs)


class DepressionScoreView(ScoreView):
    def __init__(self, **kwargs):
        super().__init__(DepressionScore, **kwargs)


class AnxietyScoreView(ScoreView):
    def __init__(self, **kwargs):
        super().__init__(AnxietyScore, **kwargs)
