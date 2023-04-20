from django.urls import path
from .views import CalendarInitView, CalendarRedirectView

urlpatterns = [
    path("calendar/init", CalendarInitView.as_view(), name="calendar_init"),
    path("calendar/redirect", CalendarRedirectView.as_view(), name="calendar_redirect")
]
