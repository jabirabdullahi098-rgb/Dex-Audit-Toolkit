# Dex-Audit-Toolkit
Simple Python tool to scan Dex routers for reentrancy, unsafe calls and access control 
# dex_audit.py
# Simple DEX Router Security Scanner
# Author: @AbdullahiJabir5 | Physics x Web3 Security
# GitHub: github.com/AbdullahiJabir5

from web3 import Web3
import json
import re

# === CONFIG ===
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"  # Replace with yours
DEX_ROUTER_ADDRESS = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"  # Uniswap V2 Router
ABI_URL = "https://raw.githubusercontent.com/Uniswap/v2-periphery/master/contracts/interfaces/IUniswapV2Router02.json"

# Connect to Ethereum
w3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not w3.is_connected():
    print("❌ Failed to connect to Ethereum")
    exit()

# Load ABI
import requests
response = requests.get(ABI_URL)
abi = response.json()['abi']

contract = w3.eth.contract(address=DEX_ROUTER_ADDRESS, abi=abi)

print(f"🔍 Auditing DEX Router: {DEX_ROUTER_ADDRESS}\n")

# === 1. REENTRANCY CHECK ===
def check_reentrancy():
    print("1️⃣ Checking for Reentrancy Risk...")
    source = requests.get(f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={DEX_ROUTER_ADDRESS}&apikey=YourApiKey").json()
    code = source['result'][0]['SourceCode']
    
    if "nonReentrant" in code or "ReentrancyGuard" in code:
        print("✅ Reentrancy Guard Detected")
    else:
        print("⚠️  WARNING: No Reentrancy Protection Found!")

# === 2. UNSAFE EXTERNAL CALLS ===
def check_external_calls():
    print("\n2️⃣ Checking Unsafe External Calls...")
    unsafe_patterns = ['call(', 'delegatecall(', 'staticcall(']
    source = requests.get(f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={DEX_ROUTER_ADDRESS}&apikey=YourApiKey").json()
    code = source['result'][0]['SourceCode']
    
    found = [p for p in unsafe_patterns if p in code]
    if found:
        print(f"⚠️  Unsafe calls detected: {', '.join(found)}")
        print("   → Ensure return values are checked!")
    else:
        print("✅ No raw low-level calls")

# === 3. ACCESS CONTROL ===
def check_access_control():
    print("\n3️⃣ Checking Access Control...")
    functions = [f for f in abi if f['type'] == 'function' and f.get('stateMutability') in ['nonpayable', 'payable']]
    critical = ['swap', 'addLiquidity', 'removeLiquidity']
    unprotected = []
    
    for func in functions:
        name = func['name']
        if any(c in name.lower() for c in critical) and 'onlyOwner' not in str(func):
            unprotected.append(name)
    
    if unprotected:
        print(f"⚠️  Critical functions without access control: {', '.join(unprotected)}")
    else:
        print("✅ All critical functions protected")

# === RUN AUDIT ===
if __name__ == "__main__":
    print("🚀 DEX Security Audit Toolkit v0.1")
    print("   by @AbdullahiJabir5 | #Web3Nigeria\n")
    check_reentrancy()
    check_external_calls()
    check_access_control()
    print("\n✅ Audit Complete! Share on X: https://github.com/AbdullahiJabir5/DEX-Audit-Toolkit")
