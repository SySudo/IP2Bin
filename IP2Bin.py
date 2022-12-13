IPbin = input("1.Bin-IP    2.IP-Bin: ")

if IPbin == "1":
    Bin = input("Bin: ")
    bin10ip = ".".join(str(int(x, 2)) for x in Bin.split("."))
    print(bin10ip)

elif IPbin == "2":
    IP = input("IP: ")
    ip2bin = ".".join(map(str,["{0:08b}".format(int(x)) for x in IP.split(".")]))
    print(ip2bin)

else:
    print("Error: Type(1 or 2)")
