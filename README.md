# TCP-Messaging
You only need to run Main.py to execute the program. 

This folder contain four separate files. 

Main.py acts as the hub for the messaging application. This file could open either the server or the client file. It also contains an image of the pigeon, the mascot for this project.

Server.py is the file that will be actively listening for the client when it is running. This file will establish a low level TCP connection, utilizing the socket library within Python. By default, the server file uses the IP address of the local machine, requiring no modifcations. 

Client.py is the file that will connect to a Server that is listening. This file will search for the IP address written within the file, by default it is the local machine; however, it could be changed to any IP address where there is a Server listening. This is a low level connection, hence this connection should only work when using the same unlocked wifi connection. 

Pigeon.gif is the image used to decorate Main.py.
