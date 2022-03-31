'''
Dima -> HTND -> HTND -> HTND -> HTND (Dima)
A    -> C    -> D    -> E    -> B

1. Dima (key: 2) -> HTND

2. Dima (key: 2)
'''

'''
key = 1

encrypt
D   i   m   a
68  105 109 97
+
69  106 110 98
E   j   n   b




69  106 110 98
E   j   n   b
-
68  105 109 97
D   i   m   a
'''
KEY = 1

def encrypt(message):
    result_message = ''
    for char in message:
        result_message += chr(ord(char) + KEY)
    return result_message

def decrypt(message):
    result_message = ''
    for char in message:
        result_message += chr(ord(char) - KEY)
    return result_message

print(encrypt('Dima'))
print(decrypt('Ejnb'))


'''
A - encrypt decrypt KEY message
B - encrypt decrypt KEY message


A - encrypt, KEY

B - (only encrypted message) 

B -> send email/password -> A -> sessionid -> B

B -> sends sessionid -> A decrypt sessionid

'''


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.user.is_anonymous:
            return redirect('login')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response