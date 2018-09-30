from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('questions/', views.IndexView.as_view(), name='getAllQuestions'),
    path('<int:question_id>', views.QuestionView.as_view()),
    path('question', views.QuestionView.as_view(), name='addQuestion'),
    path('<int:question_id>/choices', views.ChoiceView.as_view(), name='getChoices'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]

urlpatterns = format_suffix_patterns(urlpatterns)