import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def load_dotenv(path: str = "/.env"):
    with open(path) as file:
        for line in file:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=")
                os.environ[key] = value


def encrypt(data: bytes, key: bytes) -> bytes:
    """Used by client to encrypt data locally with enclaves public key"""
    data_key = AESGCM.generate_key(bit_length=256)
    aes_data = AESGCM(data_key)
    nonce_data = os.urandom(12)
    ciphertext = aes_data.encrypt(nonce_data, data, None)

    aes_key = AESGCM(key)
    nonce_key = os.urandom(12)
    enc_data_key = aes_key.encrypt(nonce_key, data_key, None)

    return nonce_key + enc_data_key + nonce_data + ciphertext


def decrypt(message: bytes, key: bytes) -> bytes:
    """Used by enclave to decrypt data"""
    nonce_key = message[:12]
    enc_data_key = message[12:60]
    nonce_data = message[60:72]
    ciphertext = message[72:]

    aes_key = AESGCM(key)
    data_key = aes_key.decrypt(nonce_key, enc_data_key, None)

    aes_data = AESGCM(data_key)
    return aes_data.decrypt(nonce_data, ciphertext, None)
