#Author: Eshwar RA
#mail  : eshwarra5@gmail.com
import subprocess
import time

#-------------------------------------------------------------------------------
print("Make sure you ran this script as root")
time.sleep(1)
print("1] Mac address changer")
print("2] Tor start")
print("3] Run python code")
print("4] Apache2 (Web Server)")
print("5] Shutdown/restart/Switch_user")
op1 = input("Enter the number given to the tool that you want to use > ")
#-------------------------------------------------------------------------------
#mac address mac_changer
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
    print("If it did not work, run the following in the linux terminal-")
    print("'sudo ifconfig <interface> down'")
    print("'sudo ifconfig <interface> hw ether <mac_address>'")
    print("'sudo ifconfig <interface> up'")
#-------------------------------------------------------------------------------
#tor start/stop/restart
if(op1 == '2'):
    print("Select an option-")
    print("1] Start tor")
    print("2] Restart tor")
    print("3] Stop tor")
    tor_op = input("tor> ")

    if(tor_op == '1'):
        subprocess.call(['sudo', 'service', 'tor', 'start'])

    if(tor_op == '2'):
        subprocess.call(['sudo','service','tor','restart'])
    if(tor_op == '3'):
        subprocess.call(['sudo','service','tor','stop'])
        
            else:
                print("Invalid Input")    
                break
                
    print("open the website- 'check.torproject.org' to check if it worked")
    print("If none of the above 3 (tor start/stop/restart) did not work, ")
    print("then run the command 'sudo service tor <start/stop/restart>' in the linux terminal")
#-------------------------------------------------------------------------------
#python script runner
if (op1 == '3'):
    print("command line python code runner-")
    print("select python interpreter-")
    print("1] python1")
    print("2] python2")
    print("3] python3")
    py_version1 = input("interpreter> ")

    if(py_version1 == '1'):
        py_version = "python"

    if (py_version1 == '2'):
        py_version = "python2"

    if(py_version1 == '3'):
        py_version = "python3"

        else:
            print("Invalid Input")        
            break 
    code_file = input("enter the location of the file that you want to execute")

    subprocess.call(['sudo', py_version, code_file])
    print("If it did not work, then run 'sudo <python3/python2/python> <file_location>'")
    
#-------------------------------------------------------------------------------
#Apache2 start/stop/Restart
if (op1 == '4'):
    print("Choose an option-")
    print("1] Configure Apache2")
    print("2] Configure and start Apache2")
    print("3] Start Apache2")
    print("4] Stop Apache2")
    print("5] Restart Apache2")
    apache2_option_1 = input("Apache2> ")

    if (apache2_option_1 == '1'):
        print("Configure Apache2")
        subprocess.call(['cd'])
        html_file = input("Enter the location of the html file for the web server- ")
        subprocess.call(['sudo','touch',html_file +'1'])
        subprocess.call(['sudo','mv',html_file +'1','/var/www/html'])
        print("If it did not work, run the following in the linux terminal-")
        print("'cd'")
        print("'sudo touch <file>1.html '")
        print("'sudo mv <file>1.html /var/www/html'")

    elif (apache2_option_1 == '2'):
        print("Starting Apache2...")
        subprocess.call(['sudo','service','apache2','start'])
        time.sleep(1)
        print("Configure Apache2")
        subprocess.call(['cd'])
        html_file = input("Enter the location of the html file for the web server- ")
        subprocess.call(['sudo','touch',html_file +'1'])
        subprocess.call(['sudo','mv',html_file +'1','/var/www/html'])
        subprocess.call(['sudo','service','apache2','restart'])
        print("View your web server by typing localhost in the URL section of your web browser")
        print("If it did not work, then run 'sudo service apache2 start/restart'")

    elif (apache2_option_1 == '3'):
        print("Starting Apache2...")
        subprocess.call(['sudo','service','apache2','start'])
        print("If it did not work, run the following in the linux terminal-")
        print("'sudo service apache2 start'")
        print("View your web server by typing localhost in the URL section of your web browser")

    elif (apache2_option_1 == '4'):
        print("Stopping apache2...")
        subprocess.call(['sudo','service','apache2','stop'])
        print("If it did not work, run the following in the linux terminal-")
        print("'sudo service apache2 stop'")
        print("Check if it worked by typing localhost in the URL section of your web browser")

    elif (apache2_option_1 == '5'):
        print("Restarting apache2...")
        subprocess.call(['sudo','service','apache2','restart'])
        print("If it did not work, run the following in the linux terminal-")
        print("'sudo service apache2 restart'")
        print("Check if it worked by typing localhost in the URL section of your web browser")

    else:
        print("Invalid Input")  
        break  

#-------------------------------------------------------------------------------
Shutdown/restart/switch_user
if (op1 == '5'):
    print("Choose an option-")
    print("1] shutdown")
    print("2] restart")
    print("3] switch_user")     
    shutdown_option = input("Shutdown/restart/switch_user > ")

    if (shutdown_option == '1'):
        subprocess.call(['sudo','shutdown','now'])
        
    elif (shutdown_option == '2'):
        subprocess.call(['reboot'])

    elif (shutdown_option == '3'):
        user_name = input("Enter the name of the user-")
        subprocess.call(['su',user_name])

    else:
        print("Invalid Input")  
        break  
