from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserProfileImageSerializer
from .models import UserProfileImage


@csrf_exempt
@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
@parser_classes([MultiPartParser, FormParser, FileUploadParser])
def upload_avatar_images(request):
    serializer = UserProfileImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "File has been uploaded successfully"}, status=200)
    else:
        return Response({"message": "File has NOT been uploaded successfully"}, status=400)


@csrf_exempt
@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
@parser_classes([MultiPartParser, FormParser, FileUploadParser, JSONParser])
def get_avatar_images(request):
    avatar = UserProfileImage.objects.all()
    serializer = UserProfileImageSerializer(avatar, many=True)
    return Response(serializer.data, status=200)
