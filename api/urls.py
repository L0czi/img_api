from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.DisplayImages.as_view()),
    path('upload/', views.PostImage.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)