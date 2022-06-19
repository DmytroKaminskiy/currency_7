students = ['Dima', 'Alex', 'Nikolay']  # iterable, str, tuple, dict, set, list ... (__iter__)
students_iter = students.__iter__()  # iterator object

# print(dir(students_iter))
# print(dir(students))

# print(students_iter.__next__())
# print(students_iter.__next__())
# print(students_iter.__next__())
# print(students_iter.__next__())

# while True:
#     try:
#         student = students_iter.__next__()
#         print(student)
#     except StopIteration:
#         break

# for student in students:  # students.__iter__()
#     # students_iter.__next__()
#     print(student)
#
# for student in students:  # students.__iter__()
#     # students_iter.__next__()
#     print(student)

def foo():
    initial = 0
    while True:
        initial += 2
        yield initial  # STOP, START after __next__ call
        if initial == 10:
            return None

foo_call = foo()  # iterable
foo_call2 = foo()  # iterable
# foo_call_iter = foo_call.__iter__()  # iterator object

# print(dir(foo_call))  # __iter__
# print(dir(foo_call_iter))  # __next__
# print(foo_call.__next__())
# print()
# print(foo_call.__next__())
# print()
# print(foo_call.__next__())
# while True:
#     try:
#         print(foo_call.__next__())
#     except StopIteration:
#         break

# for item in foo_call:
#     print(item)
#
# for item in foo_call2:
#     print(item)
#     if item == 10:
#         break

# with open('call.py') as file:
    # print(file.read())
    # for line in file:
    #     print(line, end='')

##################################
import requests

url = 'https://images8.alphacoders.com/118/1186452.jpg'
url = 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Example_image.svg'

max_size_bytes = 512 * 1024

# response = requests.head(url)
# content_length_bytes = response.headers.get('Content-Length')
# if content_length_bytes:
#     content_length_bytes = int(content_length_bytes)
#     if content_length_bytes > max_size_bytes:
#         print(f'Image is too big')
#     else:
#         print(f'Image is ok')

# local_filename = url.split('/')[-1]
# # NOTE the stream=True parameter below
# with requests.get(url, stream=True) as r:
#     r.raise_for_status()
#     with open(local_filename, 'wb') as f:
#         for chunk in r.iter_content(chunk_size=8192):
#             # If you have chunk encoded response uncomment if
#             # and set chunk_size parameter to None.
#             #if chunk:
#             f.write(chunk)

url = 'https://images8.alphacoders.com/118/1186452.jpg'
# url = 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Example_image.svg'

response = requests.get(url, stream=True)
local_filename = url.split('/')[-1]

max_size_bytes = 512 * 1024
chunk_size_bytes = 8192
currently_used_bytes = 0
remove_file = False

with open(local_filename, 'wb') as file:
    for chunk in response.iter_content(chunk_size=chunk_size_bytes):
        if currently_used_bytes < max_size_bytes:
            file.write(chunk)
            currently_used_bytes += chunk_size_bytes
        else:
            # TODO remove file
            print('FILE IS TO BIG. REMOVE IT.')
            response.close()
            remove_file = True
            break

if remove_file:
    import os
    os.remove(local_filename)
