import subprocess
import time

#--------------------------------------------------------------------------------------------------------------------
print("Make sure you ran this script as root")
time.sleep(1)
print("1] Mac address changer")
print("2] Tor start")
print("3] Run python code")
op1 = input("Enter the number given to the tool that you want to use > ")

if(op1 == '1'):
    print("Which interface's mac address do you want to change-")
    print("1] wlan0(wifi)")
    print("2] lo")
    print("3] eth0(ethernet)")
    print("4] other")
    interface_number = input("mac_changer > ")
    if(interface_number == '4'):
        interface = input("Enter the interface- ")


    elif(interface_number == '1' or '2' or '3'):

        if(interface_number == '1'):
            interface = "wlan0"

        elif(interface_number == '2'):
            interface = "lo"

        elif(interface_number == '3'):
           interface = "eth0"

    mac = input("Enter the mac address- ")

    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])

if(op1 == '2'):
    print("Select an option-")
    print("1] Start tor")
    print("2] Restart tor")
    print("3] Stop tor")
    tor_op = input("tor > ")

    if(tor_op == '1'):
        subprocess.call(['sudo', 'service', 'tor', 'start'])
    if(tor_op == '2'):
        subprocess.call(['sudo','service','tor','restart'])
    if(tor_op == '3'):
        subprocess.call(['sudo','service','tor','stop'])
if (op1 == '3'):

    print("command line python code runner-")
    print("select python interpreter-")
    print("1] python1")
    print("2] python2")
    print("3] python3")
    py_version1 = input("interpreter > ")

    if(py_version1 == '1'):
        py_version = "python"

    if (py_version1 == '2'):
        py_version = "python2"

    if(py_version1 == '3'):
        py_version = "python3"
    code_file = input("enter the location of the file that you want to execute")

    subprocess.call(['sudo', py_version, code_file])
