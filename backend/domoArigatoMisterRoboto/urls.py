from django.urls import path
from .views import *

urlpatterns = [
    # ... other URL patterns ...
    path('decode_roboto_message/', DecodeMessageView.as_view(), name='decode_roboto_message'),
]
