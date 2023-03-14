import numpy as np
raw_key = []

file_name = input("Enter samples' file name:")
my_file = open(file_name, "r")
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
raw_key = data.split("\n")
my_file.close()

while('' in raw_key):
    raw_key.remove('')

raw_key = np.array(raw_key, dtype =int)

l = len(raw_key)
print("length=",l)
print("\nraw_key:",raw_key) 

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,10)) 
t = np.arange(1,l+1)
plt.plot(t,raw_key)
plt.show()
# print(f"\nExtracted Key: {raw_key[:1000]}")

from sympy import fft

mu = np.average(raw_key)
sigma = np.std(raw_key)
print("Mean of the raw_key is % s " % (mu)) 
print("Standard Deviation of the raw_key is % s "% (sigma))


# # Toeplitz Matrix Generation

from scipy.linalg import toeplitz
i = l
j = l//100
r = np.random.randint(2, size=(1, i))
c = np.random.randint(2, size=(1, j))
t_mat = toeplitz(c,r)
print("\nToeplitz Matrix Generation:\nRow: r =", r)
print("\n")
print("Column: c =", c)
print("\n")
print("Toeplitz Matrix =\n", t_mat)


# # Toeplitz hashing

ex_key = np.zeros((j,1), dtype=int)
ex_key = np.matmul(t_mat, raw_key)
     
print("\nExtracted Key: % s "%(ex_key))
e = len(ex_key)
print("length=",e)

u = t[:j]
plt.plot(u,ex_key)
plt.show()
muu = np.average(ex_key)
sigmaa = np.std(ex_key)
print("\nStandard Deviation of the ex_key is % s "% (sigmaa))
print("Mean of the ex_key is % s " % (muu)) 

# print(f"\nExtracted Key: {ex_key[:1000]}")
k = []
for i in range(1, j):
    k.append(bin(int(ex_key[i]))[2:].zfill(8))
# print(k)


# # Binary Key 

# Python program to convert a list to string  
def listToString(k): 
    
    # initialize an empty string
    key = "" 
    
    # traverse in the string  
    for ele in k: 
        key += ele  
    
    # return string  
    return key 

key = listToString(k)
print("\nExtracted key=",key)

x = len(key)
print("length=",x)

f = open("key.txt","w+")
f.write(key)
f.close()


#--------------------------------


# server.py

TCP_IP = input("Enter Server-Rpi IP address:")
val = input("Press any key to send the key:")

import socket

# TCP_IP = '169.254.236.6'  # 192.168.13.24 -Computer // #192.168.178.193 - Rpi_Wifi //  169.254.236.6 - Rpi_Eth
#IP address of the server (RPi) will always be used by both the server (RPi) and Client (Comp).

TCP_PORT = 5005
BUFFER_SIZE = 200000  # Normally 1024, but we want fast response
                 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
s.bind((TCP_IP, TCP_PORT))            # Bind to the port
s.listen(1)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(BUFFER_SIZE)
    print('Server received', repr(data))

    filename='key.txt'
    f = open(filename,'rb')
    l = f.read(BUFFER_SIZE)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(BUFFER_SIZE)
    f.close()

    print('Done sending')
    conn.close()


# In[ ]:





# In[ ]:





# In[ ]:




