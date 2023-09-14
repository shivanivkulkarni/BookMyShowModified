from django.http import JsonResponse

class CustomLoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(self.get_response)
        response = self.get_response(request)
        print(request.user)
        # Check if the user is not authenticated
        if not request.user.is_authenticated:
            # Create a JSON response with a custom message
            return JsonResponse({'message': 'You must be logged in to access this resource'}, status=401)

        return response
