from django.contrib import admin
from django.urls import path
from app1.views import start_email_sending  # ✅ Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('start_email_sending/', start_email_sending, name='start_email_sending'),  # ✅ Add this line
]
