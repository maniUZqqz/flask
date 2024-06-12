import hashlib

password = "Mani1386"
hash = hashlib.new("SHA256")
hash.update(password.encode())
passdword_After_Hash = hash.hexdigest()

# print(hash.digest())
# print(hash)


mani = "Mani1386"
hash_mani = hashlib.new("SHA256")
hash_mani.update(mani.encode())
passdword_mani = hash_mani.hexdigest()

haker1 = "Mami1385"
hash_haker1 = hashlib.new("SHA256")
hash_haker1.update(haker1.encode())
passdword_haker1 = hash_haker1.hexdigest()

haker2 = "zalzalak"
hash_haker2 = hashlib.new("SHA256")
hash_haker2.update(haker2.encode())
passdword_haker2 = hash_haker2.hexdigest()

print(passdword_After_Hash)
print(passdword_mani)
print(passdword_haker1)
print(passdword_haker2)



def Enter():
    print("ستونم برو")
def Haker():
    print("باستور کن هکر")


if passdword_mani == passdword_After_Hash :
    Enter()
elif passdword_haker1 == passdword_After_Hash:
    Haker()
elif passdword_haker2 == passdword_After_Hash:
    Haker()
else:
    print("FBI Open up your door")

M = "================================================================================================================================"

print(passdword_mani == passdword_After_Hash)
print(passdword_haker1 == passdword_After_Hash)
print(passdword_haker2 == passdword_After_Hash)