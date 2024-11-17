import random
import hashlib
import base58

def generate_random_private_key():
    return ''.join(random.choices('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz', k=51)

def private_key_to_public_key(private_key):
    # This is a simplified version; in practice, use a library like `ecdsa`
    return hashlib.sha256(private_key.encode()).hexdigest()

def public_key_to_address(public_key):
    # Simplified version; in practice, use a library for proper address generation
    return base58.b58encode_check(b'\x00' + bytes.fromhex(public_key)).decode()

if __name__ == "__main__":
    private_key = generate_random_private_key()
    public_key = private_key_to_public_key(private_key)
    wallet_address = public_key_to_address(public_key)
    
    print(f"Random Private Key: {private_key}")
    print(f"Generated Wallet Address: {wallet_address}")
