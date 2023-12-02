from django.urls import path
from .views import RegisterView, LoginView, EnrollConsecrationView, FetchDailyContentView, MarkCompletionView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('enroll-consecration/', EnrollConsecrationView.as_view(), name='enroll_consecration'),
    path('daily-content/<int:user_id>/<int:day_number>/', FetchDailyContentView.as_view(), name='fetch_daily_content'),
    path('mark-completion/<int:user_id>/<int:day_number>/', MarkCompletionView.as_view(), name='mark_completion'),
]
