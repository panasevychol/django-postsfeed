from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from apps.users.constants import PASSWORD_MAX_LENGTH


def validate_user_email(email):
    if not email:
        return False

    try:
        validate_email(email)
    except ValidationError:
        return False
    else:
        return True


def validate_user_password(password):
    if password:
        return len(password) <= PASSWORD_MAX_LENGTH
    else:
        return False
