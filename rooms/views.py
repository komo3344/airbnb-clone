from math import ceil
from django.shortcuts import render
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)  # default 1
    page = int(page or 1)  # 빈 페이지 에러 해결
    pagesize = 10
    limit = pagesize * page
    offset = limit - pagesize
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / pagesize)
    return render(
        request,
        "rooms/all_rooms.html",
        context={
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count),
        },
    )
