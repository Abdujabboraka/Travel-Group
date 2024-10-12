from django.urls import path
from .views import homepage, destination_detail
urlpatterns = [
    path('', homepage, name='homepage'),
    path('detail/<d_id>',destination_detail, name="detail")
]