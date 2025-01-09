from django.urls import path

from apps.views import HomeListView, HomeFormView, home_delete

urlpatterns = [
    path('home-list',HomeListView.as_view(),name='home-list'),
    path('home',HomeFormView.as_view(),name='home'),
    path("delete/<int:pk>",home_delete,name='delete'),
]
