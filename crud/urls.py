from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.StudentDetails.as_view(),name='student'),
    path('<int:pk>/',views.StudentUpdates.as_view(),name='student'),
    path('auth/',include('rest_framework.urls'),name='auth')
]