from django.utils.timezone import now
from .models import Profile

class SetLastVisitMiddleware(object):
    def process_response(self, request, response):
        if request.user.is_authenticated():
            # Update last visit time after request finished processing.
            Profile.objects.filter(pk=request.user.pk).update(last_login=now())
        return response