from django.views.generic import ListView, DetailView
from django_countries import countries
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", context={"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404()


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


def Search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guest = int(request.GET.get("guest", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = request.GET.get("instant", False)
    super_host = request.GET.get("super_host", False)
    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    Facilities = models.Facility.objects.all()
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")

    print(s_amenities, s_facilities)
    # 입력받는 것
    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guest": guest,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "super_host": super_host,
    }

    # DB에서 가져오는 것
    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "Facilities": Facilities,
    }

    return render(request, "rooms/search.html", {**form, **choices})

