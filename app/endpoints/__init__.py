from .questions import * # noqa
from .quiz import * # noqa

from . import quiz
from . import questions

quiz.urlpatterns += questions.urlpatterns
