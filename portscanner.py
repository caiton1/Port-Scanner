#!/usr/bin/python3
import socket
import sys

while True:
    try: # host/port input and validation
        host_server = input("Enter a host: ") # host ip
        host_ip = socket.gethostbyname(host_server)
        low_bound = int(input("Enter port scan lower bound: ")) 
        high_bound = int(input("Enter port scan higher bound: "))
    except socket.gaierror:
        print("Please input a valid host address")
        continue
    except ValueError:
        print("Please input a valid number\n")
        continue
    except KeyboardInterrupt:
        print("\nCanceling operation")
        sys.exit()
    if low_bound > high_bound:
        print("Please make sure the the lower bound is lower than the higher bound.\n")
        continue
    else:
        break

# print header
print("=" * 40)
print("Scanning remote host.")

try:
    for port in range(low_bound, high_bound):
        endpoint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection = endpoint.connect_ex((host_ip, port))

        if connection == 0: # check for connect_ex 0
            print(f"Port {port} is open")
        endpoint.close()

except KeyboardInterrupt:
    print("Canceling scan.")
    sys.exit

print(f"port scan is done") 

