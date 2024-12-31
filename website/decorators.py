from functools import wraps
from django.shortcuts import render


def add_common_models(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        request.context = {}

        try:
            # import and set them in the context:

            # from app_name.model import model
            # context['model_name'] = model.objects.all()
            ...
        except:
            ...

        response = view_func(request, *args, **kwargs)

        if isinstance(response, dict):
            response.context_data.update(request.context)

        return response

    return wrapper
