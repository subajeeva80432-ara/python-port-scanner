import socket

target = input("Enter target IP address: ")

print("Scanning target:", target)

found = False

for port in range(1,101):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((target,port))

    if result == 0:
        print("Port",port,"is OPEN")
        found = True

    s.close()

if not found:
    print("No ports are open")
