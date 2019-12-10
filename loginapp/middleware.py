# from datetime import timedelta as td
# from django.utils import timezone
# from django.conf import settings
# from django.db.models.expressions import F    
# from .models import Profile  

# class SetLastVisitMiddleware(object):
#     KEY = "last-login"

#     def process_request(self, request):
#         if request.user.is_authenticated():
#             last_login = request.session.get(self.KEY)

#             # If key is old enough, update database.
#             too_old_time = timezone.now() - td(seconds=settings.LAST_ACTIVITY_INTERVAL_SECS)
#             if not last_login or last_login < too_old_time:
#                 Profile.objects.filter(user=request.user.pk).update(
#                         last_login=timezone.now(),
#                         login_count=F('login_count') + 1)

#             request.session[self.KEY] = timezone.now()

#         return None