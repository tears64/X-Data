# X-Data

**X-Data** is a modular OSINT and information-gathering multitool written in Python.

## Features

* Domain intelligence
* Email intelligence
* IP lookup
* Username search
* URL analysis
* Hash utilities
* HTTP headers
* Metadata analysis
* Password utilities
* Social intelligence
* Search utilities
* Locator tools

> ⚠️ **Disclaimer:** X-Data is intended for educational purposes, authorized security testing, and legitimate OSINT research. Only use it against systems, accounts, domains, or data you are authorized to investigate.

---

# Installation

## 🐧 Linux

### 1. Install the requirements

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

### 7. Test the installation

```bash
xdata 
```

If everything is installed correctly, X-Data's menu will be displayed.

### Updating X-Data

```bash
cd X-Data
git pull
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

---

# 📱 Termux

X-Data can run on Android using **Termux**.

### 1. Update Termux

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

### 5. Activate the virtual environment

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

### 8. Test the installation

```bash
xdata
```

X-Data should now be available directly through the `xdata` command.

### Using X-Data again later

After closing Termux, navigate back to the project and activate the environment:

```bash
cd X-Data
source .venv/bin/activate
```

Then:

```bash
xdata
```

---

# 🪟 Windows

### 1. Install Python

Download and install Python from the official Python website.

During installation, make sure to enable:

```text
Add Python to PATH
```

Verify Python:

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
pip install -r requirements.txt
```

### 7. Install X-Data

```powershell
pip install -e .
```

### 8. Test the installation

```powershell
xdata
```

If the command displays the X-Data menu, the installation was successful.

---

# 🚀 Basic Usage

After installation, activate your virtual environment and run:

```bash
xdata
```

---

# 🛠️ Development

Clone the repository:

```bash
git clone https://github.com/tears64/X-Data.git
cd X-Data
```

Create and activate a virtual environment, then install the development dependencies:

```bash
pip install -r requirements-dev.txt
pip install -e .
```

Run the tests:

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
└── requirements-dev.txt
```

---

# ⚠️ Disclaimer

X-Data is provided for **educational and authorized security/OSINT purposes only**.

The developers are not responsible for misuse of this software.

Always respect applicable laws, terms of service, privacy, and authorization requirements when using X-Data.

---

# 👤 Author

**tears64**

GitHub: https://github.com/tears64/X-Data

---

# ⭐ Support

If you find X-Data useful, consider giving the repository a ⭐ on GitHub.
