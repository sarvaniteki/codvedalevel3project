from django.urls import path
#from feedback.feedback.urls import urlpatterns
from. import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
]
