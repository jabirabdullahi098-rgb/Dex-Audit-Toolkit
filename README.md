# Dex-Audit-Toolkit

A lightweight Python tool to audit DEX routers and smart contracts for common vulnerabilities (reentrancy, unsafe calls, tx.origin issues, giveaway scams, etc.).

## Features
- Detects reentrancy risks
- Flags unsafe external calls (`call`, `delegatecall` without checks)
- Checks for improper access control / ownership issues
- tx.origin vulnerability detection
- Giveaway scam pattern detection
- Simple console output with warnings

## Installation
```bash
git clone https://github.com/jabirabdullahi098-rgb/Dex-Audit-Toolkit.git
cd Dex-Audit-Toolkit
pip install -r requirements.txt
