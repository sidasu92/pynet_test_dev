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



net_device1 = NetworkDevice("1.1.1.1", "admin", "pwd")
print(net_device1.ip_addr)
