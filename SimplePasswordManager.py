from SimplePasswordManagerCore.SimpleEncryption import SimpleEncryptor
from getpass import getpass

Encryptor = SimpleEncryptor(getpass("Wprowadź hasło:"))