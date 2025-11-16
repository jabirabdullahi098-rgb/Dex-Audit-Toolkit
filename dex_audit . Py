# dex_audit.py
# Simple DEX Router Security Scanner
# Author: @AbdullahiJabir5 | Physics x Web3 Security
# GitHub: github.com/AbdullahiJabir5/Dex-Audit-Toolkit

from web3 import Web3
import requests

# === CONFIG (Replace with your keys) ===
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"
ETHERSCAN_API_KEY = "YOUR_ETHERSCAN_KEY"
DEX_ROUTER = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"  # Uniswap V2

print("DEX Audit Toolkit v0.1 | @AbdullahiJabir5\n")
print(f"Target: {DEX_ROUTER}\n")

# === 1. REENTRANCY CHECK ===
def check_reentrancy():
    print("1️⃣ Checking Reentrancy...")
    try:
        url = f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={DEX_ROUTER}&apikey={ETHERSCAN_API_KEY}"
        data = requests.get(url).json()
        code = data['result'][0]['SourceCode']
        if "nonReentrant" in code or "ReentrancyGuard" in code:
            print("   Reentrancy Guard: DETECTED")
        else:
            print("   WARNING: No Reentrancy Guard!")
    except:
        print("   Source fetch failed (rate limit or private)")

# === 2. UNSAFE CALLS ===
def check_unsafe_calls():
    print("\n2️⃣ Checking Unsafe External Calls...")
    try:
        code = requests.get(f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={DEX_ROUTER}&apikey={ETHERSCAN_API_KEY}").json()['result'][0]['SourceCode']
        unsafe = ['call(', 'delegatecall(', 'staticcall(']
        found = [u for u in unsafe if u in code]
        if found:
            print(f"   Unsafe calls found: {', '.join(found)}")
        else:
            print("   No raw low-level calls")
    except:
        print("   Source fetch failed")

# === 3. ACCESS CONTROL ===
def check_access():
    print("\n3️⃣ Access Control Check...")
    print("   Critical functions typically protected in verified contracts")
    print("   Manual review recommended for full audit")

# === RUN ===
if __name__ == "__main__":
    check_reentrancy()
    check_unsafe_calls()
    check_access()
    print("\nAudit Complete! Share: github.com/AbdullahiJabir5/Dex-Audit-Toolkit")
