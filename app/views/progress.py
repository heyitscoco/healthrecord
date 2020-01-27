from flask_admin import expose

from .base import BaseView


class ProgressView(BaseView):
    def __init__(self):
        super().__init__(name='Progress', endpoint='progress')

    @expose('/')
    def index(self):
        return self.render('progress.html')
