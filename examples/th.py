from time import sleep, time
from multiprocessing import Process, current_process


def foo(n=3):
    print(f'Foo started with Thread: {current_thread()}')
    sleep(n)
    print(f'Foo finished with Thread: {current_thread()}')

# start = time()
# foo()
# foo()
# foo()
# end = time()
# print(end - start)
from threading import Thread, current_thread


# start = time()
# th1 = Thread(target=foo)
# th2 = Thread(target=foo)
# th3 = Thread(target=foo)
#
# th1.start()  # foo()
# th2.start()
# th3.start()
#
# th1.join()  # wait till foo ends in th1
# th2.join()  # wait till foo ends in th2
# th3.join()  # wait till foo ends in th3
#
#
# end = time()
# print(end - start)
# print(f'Current Thread: {current_thread()}')


# start = time()
#
# threads = []
# for index in range(10):
#     # foo()
#     th = Thread(target=foo, args=[index])  # foo(index)
#     # th = Thread(target=foo, kwargs={'n': index})  # foo(n=index)
#     # th = Thread(target=foo, args=[1, 2], kwargs={'n': index})  # foo(1, 2, n=index)
#     th.start()
#     threads.append(th)
#
# for thread in threads:
#     thread.join()
#
# end = time()
# print(end - start)
# print(f'Current Thread: {current_thread()}')

import requests

def check_server(url):
    response = requests.get(url)
    print(response.status_code)

URLS = [
    'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
    'https://uk.wikipedia.org/wiki/%D0%92%D1%96%D0%BA%D1%96%D0%BF%D0%B5%D0%B4%D1%96%D1%8F:%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BB_%D1%81%D0%BF%D1%96%D0%BB%D1%8C%D0%BD%D0%BE%D1%82%D0%B8',
    'https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D1%96_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B8',
    'https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:LintErrors',
] * 40

start = time()

# 62.8
# for url in URLS:
#     check_server(url)

# 4.5
# threads = []
# for url in URLS:
#     th = Thread(target=check_server, args=[url])
#     # th = Process(target=check_server, args=[url])  # 3.5
#     th.start()
#     threads.append(th)
#
# for thread in threads:
#     thread.join()
#
# end = time()
# print(end - start)

def countdown(n):
    print(f'Countdown: {current_process()}')
    # print(n)
    while n != 0:
        n -= 1


N = 500_000_000
N2 = 500_000_000

start = time()


# 11.9  11.9  12.0 --- 12
# countdown(N)

# 0.5 GIL
# 12.2 13 12.3 --- 12.5
# 4  4.3  3.9
threads = []
print(f'Main: {current_process().pid}')
for i in range(5):
    # th = Thread(target=countdown, args=[N2])
    th = Process(target=countdown, args=[N2])
    th.start()
    threads.append(th)

for thread in threads:
    thread.join()

end = time()
print(end - start)

'''
IO bound - sleep, requests.get - Thread  (!Process!)
CPU bound - countdown (+, -) - Process
GIL - global interpreter lock
'''
