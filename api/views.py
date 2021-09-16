from .serializers import DisplayImageSerializer, UploadImageSerializer
from .models import Account, Image
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions
from rest_framework import generics


class DisplayImages(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DisplayImageSerializer

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        return Image.objects.filter(owner=account)


class PostImage(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = UploadImageSerializer(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            account = Account.objects.get(user=request.user)
            serializer.save(owner=account)

            response = {}
            print(account.tier)
            if account.tier == "BASIC":
                response["thumbnail_200"] = serializer.data["thumbnail_200"]

            elif account.tier == "PREMIUM":
                response["image"] = serializer.data["image"]
                response["thumbnail_200"] = serializer.data["thumbnail_200"]
                response["thumbnail_400"] = serializer.data["thumbnail_400"]

            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
