from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.metadata import BaseMetadata


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
    




# point to this class in rest_framework = {} in settings.py
class CustomMetadata(BaseMetadata):
    
    # override the determine_metadata
    def determine_metadata(self, request, view):
        return {
            'name': view.get_view_name(),
            'renderer': [renderer.media_type for renderer in view.renderer_classes],
            'parsers': [parser.media_type for parser in view.parser_classes],
            'extra': 'extra_data'
        }