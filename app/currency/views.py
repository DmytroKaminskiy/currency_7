import random
import string

from django.http import HttpResponse


def generate_password(password_length: int = 10) -> str:
    """
    generate random string with 10 chars
    """
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''
    for _ in range(password_length):
        password += random.choice(chars)
    print(1)
    return password


def hello_world(request):
    length = int(request.GET['length'])
    return HttpResponse(generate_password(length))
