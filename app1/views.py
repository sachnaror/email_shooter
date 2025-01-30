


from django.http import HttpResponse
from .models import EmailLog
from django.http import JsonResponse
from .tasks import send_email_task

def start_email_sending(request):
    send_email_task.delay()  # ✅ Call the Celery task asynchronously
    return JsonResponse({"message": "Email sending started!"})

def track_email_open(request, email_id):
    try:
        email_log = EmailLog.objects.get(id=email_id)
        email_log.opened = True
        email_log.save()
        return HttpResponse("Tracking pixel", content_type="image/gif")
    except EmailLog.DoesNotExist:
        return HttpResponse("Not Found", status=404)
