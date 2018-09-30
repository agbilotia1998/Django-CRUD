from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url

app_name = 'app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('questions/', views.IndexView.as_view(), name='getAllQuestions'),
    url(r'^question/(?P<pk>[0-9]+)', views.QuestionView.as_view()),
    #path('question/<int:question_id>', views.QuestionView.as_view()),
    path('question', views.QuestionView.as_view(), name='addQuestion'),
    path('<int:question_id>/choices', views.question_and_choices, name='getAllChoicesForQuestion'),
    path('choice/<int:choice_id>', views.ChoiceView.as_view()),
    path('choice', views.ChoiceView.as_view(), name='addChoice'),
    path('<int:question_id>/vote', views.vote, name='vote')
]

urlpatterns = format_suffix_patterns(urlpatterns)