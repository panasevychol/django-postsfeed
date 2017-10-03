from apps.users.models import User

def check_role(request, role):
    token = request.GET.get('token', default=None)
    return (
        getattr(User.objects.filter(token=token).first(), 'role', None)
        == role
    )
