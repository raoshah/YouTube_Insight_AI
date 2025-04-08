from django.http import JsonResponse
from .transcript import transcript


def index(request):
    result = transcript()
    data = {
    'message': result,
    'status': 'success',
    'items': [
        {'id': 1, 'name': 'Item 1'},
        {'id': 2, 'name': 'Item 2'},
        {'id': 3, 'name': 'Item 3'},
    ]
    }
    return JsonResponse(data)