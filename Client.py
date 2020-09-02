# Author: Eric Orellana
# The Client will connect with the Server through a TCP Connection

from socket import *
from tkinter import *
import time
import threading

class Client_Control():
    def __init__(self):
        # Establish connection with server
        self.sock = socket(AF_INET, SOCK_STREAM)
        host_name = 'localhost' # This is where the IP address would be placed, by default it is on localhost
        self.server_address = (host_name, 10000)

    def receiver(self):
        time.sleep(2)
        self.sock.connect(self.server_address)
        while True:
            data = self.sock.recv(250).decode()
            M2 = 'Server: "%s"' % data + '\n'
            T.config(state=NORMAL)
            T.insert(INSERT, M2)
            T.config(state=DISABLED)

    # Command function to send messages to server
    def send(self):
        try:
            message = E.get()
            self.sock.sendall(message.encode())
            M1 = 'Me: "%s"' % message + '\n'
            T.config(state=NORMAL)
            T.insert(INSERT, M1)
        except:
            T.config(state=NORMAL)
            T.insert(INSERT, "System: Something went wrong. Is a Server connected?" + '\n')
        finally:
            T.config(state=DISABLED)
            E.delete(0, END)

    # Figure out how to put in a clear text box
    def clear_text(self):
        T.config(state=NORMAL)
        T.delete(1.0, 'end')
        T.config(state=DISABLED)

# Define a loop for the client receiver
client = Client_Control()
R = threading.Thread(target=client.receiver)
R.start()

# Establish tkinter
top = Tk()
top.title("Pigeon Coop Client")
L0 = Label(top, text = "Enter message here:")
E = Entry(top, bd = 2)
T = Text(top)

# Display
top.resizable(width=False, height=False)
B0 = Button(top, text = "Send", command = client.send)
B1 = Button(top, text = "Clear Text History", command = client.clear_text)
T.pack()
L0.pack(side = LEFT)
E.pack(side = LEFT, fill = X)
B0.pack(side = LEFT)
B1.pack(side= LEFT)
top.mainloop()
