import random

authorities = ["Authority1", "Authority2", "Authority3"]

def poa_block_production():
    leader = random.choice(authorities)
    print("Authorized Leader:", leader)
    print("Block Produced by:", leader)

poa_block_production()
