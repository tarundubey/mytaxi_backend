from rest_framework.permissions import IsAuthenticated


class IsAuth(IsAuthenticated):

   def has_permission(self, request, view):
       return True
       # if request.method == 'OPTIONS':
       #     return True
       # if request is not None and request.user is not None:
       #     return request.user.is_authenticated
       # return False