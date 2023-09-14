import socket
import time
import threading
from queue import Queue


q = Queue()
open_ports = []

start = time.time()

target ='127.0.0.1'



def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024):
            q.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            q.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            q.put(port)
    elif mode == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            q.put(port)


def worker():
    while not q.empty():
        port = q.get()
        if portscan(port):
            print("Port {} is open".format(port))
            open_ports.append()
        else:
            print("Port {} is closed".format(port))


def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print(f"Open ports are: {open_ports}")


run_scanner(100, 2)

end = time.time()
totaltime = end - start

print(f"Time Taken: {totaltime}")