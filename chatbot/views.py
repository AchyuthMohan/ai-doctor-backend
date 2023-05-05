from django.shortcuts import render

from django.http import JsonResponse
from chatbot.chat import get_response
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')
        if message is not None:
            response = get_response(message)
            return JsonResponse({'answer': response})
        else:
            return JsonResponse({'error': 'Invalid request data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
