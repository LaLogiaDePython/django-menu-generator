def is_superuser(request):
    """
    Returns True if request.user is superuser else returns False
    """
    return is_authenticated(request) and request.user.is_superuser


def is_staff(request):
    """
    Returns True if request.user is staff else returns False
    """
    return is_authenticated(request) and request.user.is_staff


def is_authenticated(request):
    """
    Returns True if request.user authenticated else returns False
    """
    return request.user.is_authenticated


def is_anonymous(request):
    """
    Returns True if request.user is not authenticated else returns False
    """
    return not request.user.is_authenticated


def user_has_permission(request, permission):
    """
    Returns True if request.user has the permission else returns False
    :param request: HttpRequest
    :param permission: Permission to be searched
    """
    return request.user.has_perm(permission)
