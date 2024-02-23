# PyMess
Software made to communicate. Mostly made in Python

So, basically we can focus on two main files. Server and client. Server is well... Server, 
it has to manage sending messages between clients.
Server does not need any fancy GUI, however I can not promise not to make one in the future.

Client should have ease of use and at least OK GUI. The more functionalities, the better.

Last, however the most importatnt is securiy, right now it has zero security, all messages goes through 
as a plain text. Big updates in this matter in the future. 

If anyone want to use this, you can, it was tested in a local lan network, and it works OK.
As I said earlier, everything is send as a plain text, so be careful with that.

            I highly reccommend not to put it up in public domain!!!

More technical things below, like how to setup or smthn... 

First, if you only want to test it localy, you can just set:
            HOST = 127.0.0.1
            PORT = 10001
In both files (server.py and client.py)

If you want to set it up in a local network, first, set up server. check your IP adres
and set it as a value of HOST, then set a port, tbh any should work, for testing I am using 
port 80 (http port)

If the server boots up, you can change HOST and PORT in a clinent file. You should assign them the 
same values as for server. 
Now, log in users and have fun chatting. 


