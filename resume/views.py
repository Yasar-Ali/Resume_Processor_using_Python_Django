from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CandidateSerializer
from .services import ResumeParser

def home(request):
    return render(request, 'resume/home.html')

@api_view(['POST'])
def extract_resume(request):
    """
    API endpoint that accepts a resume file and returns extracted information
    """
    if 'resume' not in request.FILES:
        return Response(
            {'error': 'No resume file provided'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        resume_file = request.FILES['resume']
        parser = ResumeParser(resume_file)
        
        data = {
            'first_name': parser.extract_first_name(),
            'email': parser.extract_email(),
            'mobile_number': parser.extract_phone()
        }
        
        # Validate extracted data
        serializer = CandidateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )