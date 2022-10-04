import hashlib
m = hashlib.sha256(b"mensaje")
print(m.digest())

m = hashlib.sha256(m.digest())
print(m.digest())

m = hashlib.sha256(m.digest())
print(m.digest())