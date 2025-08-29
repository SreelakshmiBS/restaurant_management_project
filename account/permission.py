from rest_framework.permissions import BasePermission

class IsManagerOrAdmin(BasePermission):
    """ Only Managers or Admins can add/edit menu """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['Manager', 'Admin']

class IsWaiter(BasePermission):
    """ Only Waiters can create orders """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Waiter'

class IsCashier(BasePermission):
    """ Only Cashiers can process payments """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Cashier'
