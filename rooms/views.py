from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(
        room_list, 10, orphans=5
    )  # 5와 같거나 작으면 이전페이지에서 보여줌 6이상이면 다음페이지에서 보여줌

    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/all_rooms.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")

