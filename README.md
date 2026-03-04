# Mathematical & Practical Implementation of Blockchain Consensus Mechanisms

## 📌 Project Overview

This project provides **clean, structured, demo-ready Python simulations** of major Blockchain Consensus Mechanisms.

The goal is to bridge:

- Mathematical Analysis
- Distributed Systems Theory
- Practical Python Implementation

It covers both **permissioned** and **permissionless** consensus models.

---

# 🚀 Implemented Consensus Mechanisms

## 1️⃣ CFT – Crash Fault Tolerance

Used in systems like etcd (based on Raft by Diego Ongaro).

### Safety Condition
n ≥ 2f + 1

### Key Properties
- Handles crash failures only
- Majority-based agreement
- Linear communication complexity O(n)

---

## 2️⃣ PBFT – Practical Byzantine Fault Tolerance

Used in Hyperledger Fabric.

### Safety Condition
n ≥ 3f + 1

### Protocol Phases
1. Pre-Prepare
2. Prepare
3. Commit

### Properties
- Tolerates malicious nodes
- Requires 2f+1 agreement
- Communication Complexity: O(n²)

---

## 3️⃣ HotStuff – Optimized BFT

Modern scalable BFT protocol (used in DiemBFT).

### Improvements Over PBFT
- Uses threshold signature aggregation
- Reduces complexity to O(n)
- Maintains n ≥ 3f + 1 Byzantine safety

---

## 4️⃣ Proof of Work (PoW)

Used in Bitcoin.

### Core Condition
SHA-256(Block) < Target

### Security
Secure if attacker < 50% hash power

### Properties
- Probabilistic finality
- High energy consumption
- Mining-based consensus

---

## 5️⃣ Proof of Stake (PoS)

Used in Ethereum (after The Merge).

### Selection Probability
P_i = Stake_i / Total_Stake

### Security
Attacker must control ≥ 1/3 stake to disrupt finality.

### Properties
- Deterministic finality
- Energy efficient
- Stake-based validation

---

## 6️⃣ Delegated Proof of Stake (DPoS)

Used in EOS.

### Mechanism
- Token holders vote
- Top N delegates selected
- Delegates produce blocks in rotation

### Properties
- High throughput
- Reduced decentralization
- O(N) complexity

---

## 7️⃣ Proof of Authority (PoA)

Used in VeChain and enterprise blockchains.

### Mechanism
- Pre-approved validators
- Identity-based trust

### Properties
- Very fast
- Low energy
- Suitable for private networks

---

# 📊 Comparative Summary

| Mechanism | Fault Model | Min Nodes | Complexity | Finality |
|-----------|------------|-----------|------------|----------|
| CFT | Crash only | 2f+1 | O(n) | Deterministic |
| PBFT | Byzantine | 3f+1 | O(n²) | Deterministic |
| HotStuff | Byzantine | 3f+1 | O(n) | Deterministic |
| PoW | Hash power | 51% | Hash-based | Probabilistic |
| PoS | Economic stake | 2/3 majority | O(n) | Deterministic |
| DPoS | Delegated voting | Top N | O(N) | Deterministic |
| PoA | Authority list | Fixed | O(1) | Deterministic |

---

# 🛠 Requirements

- Python 3.8+
- No external libraries required
- Only built-in modules used:
  - random
  - hashlib

---

# ▶️ How to Run

Clone the repository:

```bash
git clone <your-repo-link>
cd <project-folder>
