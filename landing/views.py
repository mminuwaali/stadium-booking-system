from website import decorators
from django.shortcuts import render


@decorators.add_common_models
def index_view(request):
    return render(request, "landing/pages/index.html")


@decorators.add_common_models
def about_view(request):
    return render(request, "landing/pages/about.html")


@decorators.add_common_models
def contact_view(request):
    return render(request, "landing/pages/contact.html")
