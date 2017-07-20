from django.shortcuts import get_object_or_404
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from .models import pp_subjects
from .serializers import pp_subjectsSerializer

#List all subjects or create a new one
class subjectslist(APIView):
    parser_classes = (FileUploadParser,)
    def get(self, request):
        subjects = pp_subjects.objects.all()
        serializer = pp_subjectsSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=200)


















# Create your views here.
