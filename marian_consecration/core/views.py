from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User  # Import the User model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProgress, Consecration  # Import other models as needed
from .serializers import UserProgressSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):
    def post(self, request):
        # User registration view
        username = request.data.get('username')
        password = request.data.get('password')
        # You can add more fields as needed

        if username and password:
            user = User.objects.create_user(username, password=password)
            login(request, user)
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Invalid registration data'}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        # User login view
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class EnrollConsecrationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # User enrolls in the consecration
        user = request.user
        consecration_id = request.data.get('consecration_id')

        try:
            # Check if the consecration exists
            consecration = Consecration.objects.get(id=consecration_id)

            # Check if the user is already enrolled
            if UserProgress.objects.filter(user=user, day__consecration=consecration).exists():
                return Response({'message': 'User is already enrolled in this consecration.'}, status=status.HTTP_400_BAD_REQUEST)

            # Create UserProgress records for each day of the consecration
            for day_number, day in enumerate(consecration.day_set.all(), start=1):
                UserProgress.objects.create(user=user, day=day, day_number=day_number)

            return Response({'message': 'User enrolled in the consecration successfully'}, status=status.HTTP_201_CREATED)
        except Consecration.DoesNotExist:
            return Response({'message': 'Consecration not found'}, status=status.HTTP_404_NOT_FOUND)

class FetchDailyContentView(APIView):
    def get(self, request, user_id, day_number):
        # Fetch daily content for a user
        user_progress = UserProgress.objects.filter(user=user_id, day__day_number=day_number).first()
        if user_progress:
            serializer = UserProgressSerializer(user_progress)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Daily content not found'}, status=status.HTTP_404_NOT_FOUND)

class MarkCompletionView(APIView):
    def post(self, request, user_id, day_number):
        # Mark the day as completed for a user
        user_progress = UserProgress.objects.filter(user=user_id, day__day_number=day_number).first()
        if user_progress:
            user_progress.completed = True
            user_progress.save()
            return Response({'message': 'Day marked as completed'}, status=status.HTTP_200_OK)
        return Response({'message': 'User progress not found'}, status=status.HTTP_404_NOT_FOUND)
