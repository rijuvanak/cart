from django.urls import path
from .views import process_cart

app_name = 'cartapp'

urlpatterns = [
    path('process_cart/', process_cart, name='process_cart'),

    # Add other URL patterns for your application
]
