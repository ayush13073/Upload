import os

print("")
print("1. Rename files with prefix")
print("2. Copy file (binary)")
print("3. List files and save")
print("4. Exit")
choice = int(input("Choice: "))

if choice == 1:
    folder = input("Folder path : ")
    prefix = input("Prefix to add : ")


    for f in os.listdir(folder):
        old_path = os.path.join(folder,f)

        if os.path.isfile(old_path):
            new_name = prefix + f
            new_path = os.path.join(folder, new_name)
            os.rename(old_path, new_path)

            print("%s -> %s" %(f,new_name))

elif choice == 2:
    source = input("Enter source")
    dest = input("Enter dest")

    with open(source,"rb") as src:
        with open(dest,"wb") as dst:
            while(1):
                chunk = src.read(1024)
                if chunk == b"":
                    break
                dst.write(chunk)
    print("done")


elif choice == 3:
    folder = input("Folder path : ")
    output = input("save list to file : ")

    with open(output,"w") as out:
        for f in os.listdir(folder):
            out.write(f + "\n")
            print(f)
    print("done")


elif choice == 4:
    print("exiting>>>>>>>>")


else:
    print("Invalid choice ")


