from . import views
from django.urls import path

app_name = "food"
urlpatterns = [
    # home
    path("", views.index, name="index"),
    # /item_id number
    path("<int:item_id>/", views.detail, name="detail"),
    #  add items
    path("add/", views.create_items, name="create_items"),
]
