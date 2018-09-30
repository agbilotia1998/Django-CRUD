# Create your views here.
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import views, status
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework.decorators import api_view
from rest_framework import generics

from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer

factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}

class IndexView(views.APIView):
    def get(self, request):
        questions = Question.objects.order_by('date')
        data = QuestionSerializer(questions, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

class QuestionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# class QuestionView(views.APIView):
#     def get(self, request, question_id):
#         # question_id = request.GET.get('question_id')
#         question = Question.objects.filter(pk=question_id).first()
#         questionData = QuestionSerializer(question)
#
#         return Response(questionData.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#
#             return Response(serializer.data, status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, question_id):
#         question = Question.objects.get(pk=question_id)
#         serializer = QuestionSerializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#
#             return Response(serializer.data, status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, question_id):
#         question = Question.objects.get(pk=question_id)
#         question.delete()
#
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ChoiceView(views.APIView):
    def get(self, request, choice_id):
        choice = Choice.objects.get(pk=choice_id)
        choiceData = ChoiceSerializer(choice)

        return Response(choiceData.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, choice_id):
        choice = Choice.objects.get(pk=choice_id)
        serializer = ChoiceSerializer(choice, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, choice_id):
        choice = Choice.objects.get(pk=choice_id)
        choice.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

# class ChoiceView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer

@api_view(['GET'])
def question_and_choices(request, question_id):
    # question_id = request.GET.get('question_id')
    question = Question.objects.get(pk=question_id)
    # choices = Choice.objects.filter(question_id=question_id)
    choiceData = ChoiceSerializer(instance=question.choice_set.all(), context=serializer_context, many=True)

    return Response(choiceData.data, status=status.HTTP_200_OK)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
