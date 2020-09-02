# Author: Eric Orellana
# The Server will connect with the Client through a TCP Connection

from socket import *
from tkinter import *
import time
import sys
import threading

class Server_Control():
    def receiver(self):
        # Establishes server and extends connection
        sock = socket(AF_INET, SOCK_STREAM)
        host_name = 'localhost'
        server_address = (host_name, 10000)
        sock.bind(server_address)
        sock.listen(1)
        self.connection, _ = sock.accept()
        while True:
            try:
                data = self.connection.recv(250).decode()
                M2 = 'Client: "%s"' % data + '\n'
                T.config(state=NORMAL)
                T.insert(INSERT, M2)
                T.config(state=DISABLED)
            except:
                T.config(state=NORMAL)
                T.insert(INSERT, "Connection Error: Disconnecting.")
                T.config(state=DISABLED)
                self.connection.close()

    def send(self):
        try:
            message = E.get()
            self.connection.sendall(message.encode())
            M1 = 'Me: "%s"' % message + '\n'
            T.config(state=NORMAL)
            T.insert(INSERT, M1)
        except:
            T.config(state=NORMAL)
            T.insert(INSERT, "System: Something went wrong. Is a Client connected?" + '\n')
        finally:
            T.config(state=DISABLED)
            E.delete(0, END)

    def clear_text(self):
        T.config(state=NORMAL)
        T.delete(1.0, 'end')
        T.config(state=DISABLED)

    # def Quit(self):
    #     T.config(state=NORMAL)
    #     T.insert(INSERT, "Disconnecting..." + '\n')
    #     T.config(state=DISABLED)
    #     E.delete(0, END)
    #     quit()

# Define a loop for the server receiver
server = Server_Control()
R = threading.Thread(target=server.receiver)
R.start()

# Establishes tkinter
top = Tk()
top.title("Pigeon Coop Server")
L0 = Label(top, text = "Enter message here:")
E = Entry(top, bd = 2)
T = Text(top)

# Display loop
top.resizable(width=False, height=False)
B0 = Button(top, text = "Send", command = server.send)
B1 = Button(top, text = "Clear Text History", command = server.clear_text)
# B2 = Button(top, text = "Quit Program", command = server.Quit)
T.pack()
L0.pack(side = LEFT)
E.pack(side = LEFT, fill = X)
B0.pack(side = LEFT)
B1.pack(side= LEFT)
# B2.pack(side= LEFT)
top.mainloop()
