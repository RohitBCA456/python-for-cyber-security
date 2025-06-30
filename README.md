# 🐍🛡️ Python for Cyber Security

This repository contains Python scripts and basic programming exercises aimed at learning Python in the context of cyber security. It is a collection of tools, examples, and foundational programs for those who want to understand how Python can be used in ethical hacking and penetration testing.

---

## 📁 Folder Structure

```
.
├── MAC Changer/            # MAC address spoofing tool
├── PythonBasic/            # Core Python concepts & exercises
├── Network Scanner/        # Scapy-based tool to detect network devices
├── README.md               # You're reading it
```

---

## 🚀 Projects

### 1. MAC Changer
- **Location**: `MAC Changer/mac_changer.py`
- **Purpose**: Spoofs MAC addresses using `ifconfig`, verifies changes via regex.
- **Usage**:
  ```bash
  sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
  ```

---

### 2. Network Scanner (New!)
- **Location**: `Network Scanner/network_scanner.py`
- **Purpose**: Scans devices connected to the same network using `scapy`, retrieving their MAC and IP addresses.
- **Features**:
  - Sends ARP requests in broadcast
  - Receives responses and lists active devices
- **Usage**:
  ```bash
  sudo python3 network_scanner.py -t 192.168.1.1/24
  ```

---

### 3. PythonBasic
- **Location**: `PythonBasic/`
- **Topics Covered**:
  - Data types, conditionals, loops, and functions
  - Collections (lists, tuples, sets, dictionaries)
  - File handling and modules

---

## 🎓 Learning Resources

- **Scripts**: Real-world tools like MAC spoofers and network scanners
- **Courses**:
  - Coursera – *Python for Cybersecurity Specialization*
  - Udemy – *Python for Ethical Hacking*
  - Cybrary – *Python for Cybersecurity Professionals*
- **Books**:
  - *Python for Cybersecurity: Offense and Defense*
  - *Python Programming for Cybersecurity*
- **Articles**:
  - GeeksforGeeks: Python cybersecurity libraries
  - Medium: Security scripts like keyloggers, brute-force tools, scanners

---

## ⚙️ Prerequisites

- Python 3.x
- Required tools and libraries:
  ```bash
  sudo apt install net-tools
  pip install scapy
  ```

---

## 👨‍💻 Author

**Rohit Yadav**  
GitHub: [@RohitBCA456](https://github.com/RohitBCA456)

---

## 🤝 Contributing

Contributions are welcome! You can:

- Fix bugs 🐞
- Add tools 🔧
- Improve docs 📝

```bash
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

- ✅ Added Network Scanner using `scapy`
- ✅ Improved folder structure and tool descriptions
- ✅ Updated learning resource section
