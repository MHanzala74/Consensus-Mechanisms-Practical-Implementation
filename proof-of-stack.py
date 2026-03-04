import random

"""
Proof of Stake (PoS) Simulation

Description:
Selects validator based on stake proportion.

Selection Probability:
Stake_i / Total_Stake
"""

validators = {
    "Alice": 50,
    "Bob": 30,
    "Charlie": 20
}

def select_validator(validators):
    total = sum(validators.values())
    pick = random.uniform(0, total)
    current = 0

    for v, stake in validators.items():
        current += stake
        if current >= pick:
            return v

for _ in range(5):
    print("Selected:", select_validator(validators))