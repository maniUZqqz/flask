from cryptography.fernet import Fernet

key = Fernet.generate_key()

Uz = Fernet(key)

message = "mmnbvh"

QQZ = Uz.encrypt(message.encode())

print(QQZ)

Artor = Uz.decrypt(QQZ).decode()

print(Artor)