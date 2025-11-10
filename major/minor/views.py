from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from .models import Event
import json

def dashboard(request):
    return render(request, 'minor/index.html')

@csrf_exempt
def record_event(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'invalid method'}, status=405)
    try:
        data = json.loads(request.body or '{}')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'bad json'}, status=400)
    etype = data.get('type')
    if not etype:
        return JsonResponse({'error': 'missing type'}, status=400)
    Event.objects.create(type=etype, metadata=data.get('metadata', {}))
    return JsonResponse({'status': 'ok'})

def get_stats(request):
    counts = (
        Event.objects.values('type')
        .annotate(count=Count('type'))
        .order_by('type')
    )
    return JsonResponse(list(counts), safe=False)
