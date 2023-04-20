import google_auth_oauthlib.flow
from django.urls import reverse
from app.settings import HOST, GOOGLE_CLIENT_CONFIG

def get_google_oauth_flow(state=None):
    scopes = ["https://www.googleapis.com/auth/calendar.events.readonly"]
    kwargs = {"scopes": scopes}
    if state:
        kwargs["state"] = state
    flow = google_auth_oauthlib.flow.Flow.from_client_config(
        GOOGLE_CLIENT_CONFIG,
        **kwargs
    )
    flow.redirect_uri = f"http://{HOST}{reverse('calendar_redirect')}"
    return flow
