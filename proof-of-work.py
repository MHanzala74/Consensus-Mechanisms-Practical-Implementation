import hashlib

def mine(data, difficulty):
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