from django.urls import path
from rooms import views as room_views

app_name = "core"  # namespace랑 같아야함

urlpatterns = [path("", room_views.all_rooms, name="home")]  # view에 이름주기

