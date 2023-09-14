from functools import wraps
from django.http import JsonResponse

def user_type_required(user_type):

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.user_type == user_type:
                return view_func(request, *args, **kwargs)
            else:
                return JsonResponse({"msg":"Permission denied"})

        return _wrapped_view

    return decorator
