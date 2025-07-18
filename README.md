# 🐍🛡️ Python for Cyber Security

This repository contains Python scripts and basic programming exercises aimed at learning Python in the context of cyber security. It is a collection of tools, examples, and foundational programs for those who want to understand how Python can be used in ethical hacking and penetration testing.

---

## 📁 Folder Structure

```
.
├── ARP SPOOF DETECTOR/     # Detects ARP spoofing attempts
├── ARP Spoofing/           # ARP spoofing tool for MITM attacks
├── ENCRYPTED FILE SYS/     # File encryption and decryption system
├── KEYLOGGER/              # Captures keystrokes from keyboard
├── LISTENER/               # Socket-based message listener with encryption
├── MAC Changer/            # MAC address spoofing tool
├── Network Scanner/        # Scapy-based tool to detect network devices
├── PACKET SNIFFER/         # Sniffs packets from the network
├── PythonBasic/            # Core Python concepts & exercises
├── README.md               # You're reading it
```

---

## 🚀 Projects

### 1. ARP Spoof Detector

```
📂 Location: ARP SPOOF DETECTOR/

📌 Purpose:
Detects ARP spoofing attempts on the network.

🔍 Features:
- Monitors ARP replies
- Alerts if MAC address mismatch is detected
```

---

### 2. ARP Spoofing

```
📂 Location: ARP Spoofing/arp_spoofing.py

📌 Purpose:
Performs ARP spoofing (man-in-the-middle attack) using `scapy`, and restores ARP tables on exit.

🔍 Features:
- Redirects traffic between target and gateway
- Restores ARP tables on CTRL+C

💻 Usage:
sudo python3 arp_spoofing.py -t 192.168.110.129 -g 192.168.110.2
```

---

### 3. Encrypted File System

```
📂 Location: ENCRYPTED FILE SYS/

📌 Purpose:
Encrypts and decrypts file contents using a secure key before writing or reading data.

🔐 Features:
- Symmetric encryption
- Command-line interface for file handling
```

---

### 4. Keylogger

```
📂 Location: KEYLOGGER/

📌 Purpose:
Logs all keyboard strokes and stores them locally.

⚠️ Warning:
Only use for ethical and educational purposes.
```

---

### 5. Listener

```
📂 Location: LISTENER/

📌 Purpose:
Implements socket-based communication with encryption and decryption of messages.

🔐 Features:
- AES/Crypto integration
- Secure listening server
```

---

### 6. MAC Changer

```
📂 Location: MAC Changer/mac_changer.py

📌 Purpose:
Spoofs MAC addresses using `ifconfig`, verifies changes via regex.

💻 Usage:
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

---

### 7. Network Scanner

```
📂 Location: Network Scanner/network_scanner.py

📌 Purpose:
Scans devices connected to the same network using `scapy`, retrieving their MAC and IP addresses.

🔍 Features:
- Sends ARP requests in broadcast
- Receives responses and lists active devices

💻 Usage:
sudo python3 network_scanner.py -t 192.168.1.1/24
```

---

### 8. Packet Sniffer

```
📂 Location: PACKET SNIFFER/

📌 Purpose:
Captures network packets and displays protocol and payload info.

🔍 Features:
- Sniffs packets using `scapy`
- Displays source, destination, and payload
```

---

### 9. PythonBasic

```
📂 Location: PythonBasic/

📚 Topics Covered:
- Data types, conditionals, loops, and functions
- Collections (lists, tuples, sets, dictionaries)
- File handling and modules
```

---

## 🎓 Learning Resources

```
📜 Scripts:
- Real-world tools like MAC spoofers and network scanners

🎓 Courses:
- Coursera – Python for Cybersecurity Specialization
- Udemy – Python for Ethical Hacking
- Cybrary – Python for Cybersecurity Professionals

📚 Books:
- Python for Cybersecurity: Offense and Defense
- Python Programming for Cybersecurity

📰 Articles:
- GeeksforGeeks: Python cybersecurity libraries
- Medium: Security scripts like keyloggers, brute-force tools, scanners
```

---

## ⚙️ Prerequisites

```
Python 3.x

Required tools and libraries:

sudo apt install net-tools
pip install scapy
```

---

## 👨‍💻 Author

```
Rohit Yadav  
GitHub: https://github.com/RohitBCA456
```

---

## 🤝 Contributing

```
Contributions are welcome! You can:

- Fix bugs 🐞
- Add tools 🔧
- Improve docs 📝

Steps:

git clone https://github.com/RohitBCA456/python-for-cyber-security.git
cd python-for-cyber-security
git checkout -b feature-branch
# make changes
git add .
git commit -m "Added new feature"
git push origin feature-branch
```

---

## ✅ Latest Updates

```
✅ Added ARP Spoofer using scapy  
✅ Added Network Scanner using scapy  
✅ Added Keylogger  
✅ Added Encrypted File System  
✅ Added Packet Sniffer  
✅ Added ARP Spoof Detector  
✅ Added Listener with encryption support  
✅ Improved folder structure and tool descriptions  
✅ Updated learning resource section
```
