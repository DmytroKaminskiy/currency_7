from multiprocessing import Process
from threading import Thread
from time import sleep


def foo():
    sleep(3)
    print('FOO')


###############
import os
worker_type = os.environ.get('WORKER_TYPE')

if worker_type == 'process':
    WorkerType = Process
elif worker_type == 'thread':
    WorkerType = Thread
else:
    print('Please, select worker type')
    exit(1)

print(WorkerType)
workers = []
for _ in range(10):
    worker = WorkerType(target=foo)
    worker.start()
    workers.append(worker)


for worker in workers:
    worker.join()
