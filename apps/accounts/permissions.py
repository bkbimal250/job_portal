from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == 'admin'
class IsEmployer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == 'employer'
class IsJobSeeker(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == 'jobseeker'