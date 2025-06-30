# Python for Cyber Security 🐍🛡️

This repository contains Python scripts and basic programming exercises aimed at learning Python in the context of cyber security. It is a collection of tools, examples, and foundational programs for those who want to understand how Python can be used in ethical hacking and penetration testing.

---

## 📁 Folder Structure

```bash
.
├── MAC Changer/            # A MAC address spoofing tool
├── PythonBasic/            # Basic Python programs (conditions, loops, functions, etc.)
├── README.md               # You're reading it
```

---

## 🚀 Projects

### 1. MAC Changer
A Python script to change the MAC address of a specified network interface.

> 📍 Located in: `MAC Changer/mac_changer.py`

#### 🔧 Features:
- Takes arguments from the command line (`-i` for interface, `-m` for new MAC)
- Changes MAC using `ifconfig`
- Validates change success with regex

#### 🧪 Usage:
```bash
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

---

### 2. PythonBasic

> 📍 Located in: `PythonBasic/`

Contains beginner-friendly Python programs, ideal for anyone starting their journey into:
- Data types
- Conditional statements
- Loops
- Functions
- Lists, Tuples, Sets, Dictionaries
- File handling
- Modules and packages

---

## 📌 Prerequisites

- Python 3.x
- `ifconfig` (part of `net-tools`) for MAC Changer tool:
  
  ```bash
  sudo apt install net-tools
  ```

---

## 👨‍💻 Author

**Rohit Yadav**  
GitHub: [RohitBCA456](https://github.com/RohitBCA456)  
Project Repo: [Python for Cyber Security](https://github.com/RohitBCA456/python-for-cyber-security)

---

## 🤝 Contributing

Contributions are welcome!

If you want to:
- Fix bugs 🐞
- Add new tools 🔧
- Improve documentation 📝
- Clean up code 🧹

Feel free to fork the repo, create a branch, and submit a pull request.

```bash
# Example workflow
git clone https://github.com/RohitBCA456/python-for-cyber-security.git
cd python-for-cyber-security
git checkout -b your-feature-branch
# Make your changes
git add .
git commit -m "Your message"
git push origin your-feature-branch
```

---

Let me know if you want to contribute something and need help getting started!
