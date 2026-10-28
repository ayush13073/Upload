import os

key = 42
tag = b"ENC:"
filename = "secret.txt"

# ---------- create demo file if missing ----------
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("This is a top secret message that needs protection.\n")
        f.write("Nobody should read this without the key.\n")
    print("Created demo file: %s" % filename)
    print("")

# ---------- read ----------
with open(filename, "rb") as file:
    data = file.read()

# ---------- decide: encrypt or decrypt ----------
if data[:4] == tag:
    # file has the tag -> already encrypted -> decrypt it
    inner = data[4:]
    new_list = []
    for byte in inner:
        new_list.append((byte - key) % 256)

    with open(filename, "wb") as file:
        file.write(bytes(new_list))

    print("File was ENCRYPTED -> now DECRYPTED")

else:
    # file has no tag -> normal -> encrypt it
    new_list = []
    for byte in data:
        new_list.append((byte + key) % 256)

    with open(filename, "wb") as file:
        file.write(tag + bytes(new_list))

    print("File was NORMAL -> now ENCRYPTED")
