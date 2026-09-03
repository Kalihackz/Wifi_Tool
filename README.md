# 📶 Wifi_Tool

**A Python3 tool for scanning nearby WiFi networks and connecting to them —
either with a manually entered password or via a brute-force dictionary
attack.**

> ⚠️ For educational and authorized security-testing use only. Only use
> against networks you own or have explicit permission to test.

<p>
  <a href="https://www.buymeacoffee.com/kalihackz"><img src="https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=kalihackz&button_colour=FFDD00&font_colour=000000&font_family=Bree&outline_colour=000000&coffee_colour=ffffff" /></a>
</p>

---

## ✨ Features

- **Scan** nearby WiFi networks and list them.
- **Connect** to a network with a manually entered password.
- **Brute force** a network's password using a wordlist file.

---

## 📦 Requirements

Python3 and the following modules:

| Module | Install |
|---|---|
| `wifi` | `pip3 install wifi` |
| `time` | comes pre-installed with Python3 |
| `termcolor` | `pip3 install termcolor` |
| `texttable` | `pip3 install texttable` |

---

## 🚀 Usage

```bash
sudo python3 Wifi_Tool.py
```

Follow the on-screen prompts to scan for networks, then choose to connect
manually or attempt a brute-force attack using a password list (see
`pass.txt` for the expected format).

---

## 📄 Files

| File | Purpose |
|---|---|
| `Wifi_Tool.py` | Scans nearby WiFi networks and connects via manual password entry or brute-force attack |
| `pass.txt` | Example password wordlist used by the brute-force mode |

---

## 🖼️ Screenshot

![Screenshot of Wifi_Tool](https://i.imgur.com/A1KXZ44.png)

---

## ☕ Support

If this tool saved you some time, consider buying me a coffee:

<a href="https://www.buymeacoffee.com/kalihackz"><img src="https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=kalihackz&button_colour=FFDD00&font_colour=000000&font_family=Bree&outline_colour=000000&coffee_colour=ffffff" /></a>
