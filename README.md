# X-Data

**X-Data** is a modular, cross-platform OSINT and information-gathering multitool written in Python.

It provides a collection of tools for public-source research, network information, file analysis, and other legitimate OSINT workflows.

## Features

* Username search
* Email intelligence
* Domain intelligence
* IP intelligence
* URL analysis
* HTTP header analysis
* File metadata analysis
* File hash utilities
* Password generator
* Public IP locator
* Search query generator
* Port scanner
* Device information
* Web snapshot / archiving
* Public Snapchat / TikTok intelligence
* OSINT resources
* Discord integration
* Self-hosted TempMail
* Interactive CLI interface

> ⚠️ **Disclaimer:** X-Data is intended for educational purposes, authorized security testing, and legitimate OSINT research. Only use it against systems, accounts, domains, or data you are authorized to investigate.

---

# 🖥️ Platform Status

| Platform   | Status              |
| ---------- | ------------------- |
| 🐧 Linux   | ✔️ Tested           |
| 📱 Termux  | ✔️ Testing          |
| 🪟 Windows | ⚠️ Not fully tested |

---

# 🚀 Installation

## 🐧 Linux

### 1. Install Python and Git

**Debian / Ubuntu:**

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip git -y
```

### 2. Clone X-Data

```bash
git clone https://github.com/tears64/X-Data.git
cd X-Data
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install X-Data

```bash
pip install -e .
```

### 7. Start X-Data

```bash
xdata
```

If the installation was successful, the X-Data v1.2 menu will appear.

---

## 📱 Termux

X-Data can be run on Android using **Termux**.

### 1. Update packages

```bash
pkg update
```

### 2. Install Python and Git

```bash
pkg install python git
```

### 3. Clone X-Data

```bash
git clone https://github.com/tears64/X-Data.git
cd X-Data
```

### 4. Create a virtual environment

```bash
python3 -m venv .venv
```

### 5. Activate the environment

```bash
source .venv/bin/activate
```

### 6. Install dependencies

```bash
pip install -r requirements.txt
```

### 7. Install X-Data

```bash
pip install -e .
```

### 8. Start X-Data

```bash
xdata
```

### Using X-Data again

After closing Termux:

```bash
cd X-Data
source .venv/bin/activate
xdata
```

---

## 🪟 Windows

### 1. Install Python

Install Python from the official Python website.

During installation, enable:

```text
Add Python to PATH
```

Verify the installation:

```powershell
python --version
```

### 2. Install Git

Install Git for Windows, then open **PowerShell** or **Command Prompt**.

### 3. Clone X-Data

```powershell
git clone https://github.com/tears64/X-Data.git
cd X-Data
```

### 4. Create a virtual environment

```powershell
python -m venv .venv
```

### 5. Activate the virtual environment

**PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Command Prompt:**

```cmd
.venv\Scripts\activate
```

### 6. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 7. Install X-Data

```powershell
python -m pip install -e .
```

### 8. Start X-Data

```powershell
xdata
```

If the X-Data menu appears, the installation was successful.

---

# 🔄 Updating X-Data

From inside the X-Data directory:

### Linux / Termux

```bash
git pull
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

### Windows

```powershell
git pull
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m pip install -e .
```

Then run:

```bash
xdata
```

---

# 🛠️ Basic Usage

Start the interactive interface:

```bash
xdata
```

X-Data provides an interactive menu containing the available tools.

The toolkit is designed around public-source information and authorized investigations.

---

# 🧰 Development

Clone the repository:

```bash
git clone https://github.com/tears64/X-Data.git
cd X-Data
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install development dependencies:

```bash
pip install -r requirements-dev.txt
pip install -e .
```

Run the test suite:

```bash
pytest
```

---

# 📁 Project Structure

```text
X-Data/
├── xdata/
│   ├── modules/
│   │   ├── domain.py
│   │   ├── email.py
│   │   ├── hash.py
│   │   ├── headers.py
│   │   ├── ip.py
│   │   ├── locator.py
│   │   ├── metadata.py
│   │   ├── password.py
│   │   ├── search.py
│   │   ├── socialintel.py
│   │   ├── url.py
│   │   └── username.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── http.py
│   └── snapshot.py
├── tests/
├── Makefile
├── VERSION
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
└── xdata_cli.py
```

---

# ⚠️ Disclaimer

X-Data is provided for **educational, authorized security-testing, and legitimate OSINT purposes only**.

Do not use X-Data to:

* Access accounts without authorization
* Bypass authentication or security controls
* Collect private information without permission
* Conduct unauthorized network scanning
* Capture credentials or authentication data
* Harass, stalk, or target individuals

You are responsible for complying with applicable laws, regulations, terms of service, and authorization requirements.

---

# 👤 Author

**tears64**

GitHub: https://github.com/tears64/X-Data

---

# ⭐ Support

If you find X-Data useful, consider giving the repository a ⭐ on GitHub.

Contributions, bug reports, and improvements are welcome.

