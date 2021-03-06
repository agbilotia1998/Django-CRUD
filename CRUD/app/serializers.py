from .models import Question, Choice
from rest_framework import serializers


class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Question
        fields = ('question', 'date')


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), read_only=False)

    class Meta:
        model = Choice
        fields = ('question', 'choice', 'votes')
