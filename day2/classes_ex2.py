class NetworkDevice(object):
    def __init__(self, ip_addr, username, password ):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password
        self.serial_number = ""
        self.vendor = ""
        self.model = ""
        self.os_version = ""
        self.uptime = ""

    def getIpAddress(self):
        print(f"The IP address for this device is {self.ip_addr}")

    def getUsernamePwd(self):
        print(f"The username is {self.username} and pwd is {self.password}")

    def setVendor(self, vendor):
        self.vendor = vendor
        print(f"vendor set to {self.vendor}")

net_device1 = NetworkDevice("1.1.1.1", "admin", "pwd")
net_device2 = NetworkDevice("2.2.2.2", "admin2", "pwd2")
net_device3 = NetworkDevice("3.3.3.3", "admin3", "pwd3")
net_device4 = NetworkDevice("4.4.4.4", "admin4", "pwd4")

print(net_device1.ip_addr)

net_device3.getIpAddress()
net_device3.getUsernamePwd()
net_device3.setVendor("Lenovo")

