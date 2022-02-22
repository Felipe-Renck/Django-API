from django.urls import path
from rest_api import views

urlpatterns = [
    path("",views.ListProviderAPIView.as_view(),name="todo_list"),
    path("create/", views.CreateProviderAPIView.as_view(),name="todo_create"),
    path("update/<int:pk>/",views.UpdateProviderAPIView.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.DeleteProviderAPIView.as_view(),name="delete_todo")
]