from django.urls import path
from app.views import CategoryView,ProductView


urlpatterns = [
    path('category/',CategoryView.as_view() ),
    path('product/',ProductView.as_view() ),
]
