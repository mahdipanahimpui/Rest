from rest_framework.permissions import BasePermission, SAFE_METHODS


#.has_permission(self, request, view):
    # view-level permission check befor enter the view

# .has_object_permission(self, request, view, obj)
    # instance(obj)-level pemission 
    # note: it is requied to use check_object_permissions(request, obj) to force the instance-level perms


class IsOwnerOrReadOnly(BasePermission):
    message = 'owner permission!!' # optional

    def has_permissions(self, request, view):
        return request.user and request.user.is_authenticated  

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user