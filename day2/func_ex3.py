

def open_read_file(filename):
    with open(filename) as f:
        return f.read()


def find_serial_no(fileContent):
    serialNo = ""
    for line in fileContent.splitlines():
        if "Processor board ID" in line:
            _, serialNo = line.split("Processor board ID")
    return serialNo

filename = "show version.txt"
print(find_serial_no(open_read_file(filename)))

