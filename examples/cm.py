# with open('cypher.py') as file:
#     print(file.read())

# try:
#     file = open('cypher.py')
#     print(file.read())
# finally:
#     file.close()

class ServiceConnection:
    def __init__(self, url):
        self.url = url

    def read(self):
        return f'READING FROM CONNECTION: {self.url}'

    def close(self):
        print(f'CLOSE CONNECTION: {self.url}')

    def __enter__(self):
        # print(...)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(exc_type, exc_val, exc_tb)
        self.close()

    # with .. as .. == __enter__ + __exit__

# try:
#     connection = ServiceConnection('custom://localhost:8085/')
#     print(connection.read())
# finally:
#     connection.close()

with ServiceConnection('custom://localhost:8085/') as connection:  # connection = ServiceConnection('custom://localhost:8085/')
    print(connection.read())
    # 1 + '1'
