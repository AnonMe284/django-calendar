from googleapiclient.discovery import build
from rest_framework.views import APIView
from datetime import datetime
from django.http import HttpResponseRedirect, JsonResponse

from calender.services import get_google_oauth_flow
from app.settings import HOST

class CalendarInitView(APIView):
    def get(self, request):
        flow = get_google_oauth_flow()
        authorization_url, state = flow.authorization_url(    
            access_type='offline',
            include_granted_scopes='true'
        )
        request.session["state"] = state
        return HttpResponseRedirect(redirect_to=authorization_url)


class CalendarRedirectView(APIView):

    def get(self, request):
        flow = get_google_oauth_flow(request.session["state"])
        authorization_response = f"https://{HOST}{request.get_full_path()}"
        flow.fetch_token(authorization_response=authorization_response)
        credentials = flow.credentials
        calendar = build("calendar", "v3", credentials=credentials)
        now = datetime.utcnow().isoformat() + "z"
        res = calendar.events().list(
            calendarId='primary',
            timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
        events = res.get("items", [])
        if not events:
            return JsonResponse([])
        return JsonResponse(events, safe=False)
