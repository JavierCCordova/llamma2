from infrastructure.security.hasher import PasswordHasher

hasher  =   PasswordHasher()
info    =   hasher.hash("holamundo")
print(info)