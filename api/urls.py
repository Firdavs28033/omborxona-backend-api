from django.urls import path
from .views import MaterialRequestView

urlpatterns = [
    path('material-request/', MaterialRequestView.as_view(), name='material-request'),
]