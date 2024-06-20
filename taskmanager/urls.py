from django.urls import path

from . import views

app_name = "taskmanager"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_id>/", views.detail, name="detail"),
    path("edit/<int:task_id>/", views.edit, name="edit"),
    path("update/<int:task_id>/", views.update, name="update"),
    path("delete/<int:task_id>/", views.delete, name="delete"),
    path("create", views.create, name="create"),

]