import nacl.utils

n = nacl.utils.random(2)

int_val = int.from_bytes(n, "big")##regresa el valor numerico del random.

print(n)
print(int_val)
