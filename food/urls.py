from . import views
from django.urls import path

app_name = "food"
urlpatterns = [
    # home
    path("", views.IndexClassView.as_view(), name="index"),
    #  item
    path("item/", views.item, name="item"),
    # /item_id number
    path("<int:pk>/", views.FoodDetail.as_view(), name="detail"),
    #  add items
    path("add/", views.CreateItem.as_view(), name="create_items"),
    #  edit
    path("update/<int:item_id>/", views.update_item, name="update_item"),
    #  delete
    path("delete/<int:id>/", views.delete_item, name="delete_item"),
]
