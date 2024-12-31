from website import decorators
from django.shortcuts import render


@decorators.add_common_models
def index_view(request):
    return render(request, "events/pages/index.html")


@decorators.add_common_models
def detail_view(request, id):
    return render(request, "events/pages/detail.html")
