#!/usr/bin/env/python

ip_address = input("Enter an IP address: ")
ipList = ip_address.split(".")

print(f"{ipList[0]:12}{ipList[1]:12}{ipList[2]:12}{ipList[3]:12}")
