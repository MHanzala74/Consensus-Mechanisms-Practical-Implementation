import hashlib

"""
Proof of Work (PoW) Simulation

Description:
Simulates mining process by finding a nonce
such that hash starts with required number of zeros.

Security:
Attacker must control > 50% hash power.
"""
def mine(data, difficulty):
    """
    Mine a block.

    data (str): Block data
    difficulty (int): Number of leading zeros required
    """
    nonce = 0
    prefix = "0" * difficulty

    while True:
        text = data + str(nonce)
        hash_result = hashlib.sha256(text.encode()).hexdigest()

        if hash_result.startswith(prefix):
            return nonce, hash_result

        nonce += 1

nonce, hash_value = mine("BlockData", 4)
print("Nonce:", nonce)
print("Hash:", hash_value)