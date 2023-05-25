from django.http import  JsonResponse
from .data_source import find_user



def user_details(request, name):
    user_data = find_user(name)
    if not user_data:
        return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse(user_data)
