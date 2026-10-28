source = input("Enter the source image  : ")
dest = input("ENter destination : ")

with open(source,"rb") as src:
    with open(dest,"wb") as dst:
        while(1):
            chunk = src.read(1024)
            if chunk == b"":
                break
            dst.write(chunk)
print("done")
