from django.urls import path

from .views import posts_list, post_details

app_name = "posts"
urlpatterns = [
    path("", posts_list, name="list"),
    path("<int:pk>/", post_details, name="details")
]
