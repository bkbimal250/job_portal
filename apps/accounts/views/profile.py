from rest_framework.views import APIView
from rest_framework.response import Response

class ProfileView(APIView):
    def get(self, request):
        return Response({"message": "Profile details here"})
