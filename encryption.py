
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


class Encryption:
    def __init__(self, path):
        self.path = path

    def create_key(self, password):
        salt = b'\xda\x01\xsa\asdasd\vdsd\x2131\sadbsa'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000
        )

        key =

    def execute(self):
        with open(self.path, 'r') as file:
            data_to_encrypt = file.read()

        fernet = Fernet()
