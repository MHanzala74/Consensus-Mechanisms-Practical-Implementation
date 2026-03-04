import random

"""
Proof of Authority (PoA) Simulation

Description:
Pre-approved validators produce blocks.
No mining or staking required.
"""

authorities = ["Authority1", "Authority2", "Authority3"]

def poa_block_production():
    """
    Select random authority to produce block.

    authorities (list): List of approved validators
    """
    leader = random.choice(authorities)
    print("Authorized Leader:", leader)
    print("Block Produced by:", leader)

poa_block_production()
