import os

# ---------- create small binary file (fake PNG) if missing ----------
if not os.path.exists("input_image.bin"):
    with open("input_image.bin", "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        for i in range(200):
            f.write(bytes([i % 256]))

print("Source binary file ready: input_image.bin")
print("")

# ---------- copy binary ----------
source = "input_image.bin"
dest   = "output_image.bin"

with open(source, "rb") as src:
    with open(dest, "wb") as dst:
        while 1:
            chunk = src.read(1024)
            if chunk == b"":
                break
            dst.write(chunk)

# ---------- verify sizes ----------
src_size = os.path.getsize(source)
dst_size = os.path.getsize(dest)

print("Copied %s -> %s" % (source, dest))
print("Source size = %d bytes" % src_size)
print("Dest   size = %d bytes" % dst_size)

if src_size == dst_size:
    print("Copy OK")
else:
    print("Copy FAILED")
