import os

# ---------- setup: make test folder and files if missing ----------
if not os.path.exists("test_folder"):
    os.makedirs("test_folder")

if not os.path.exists("test_folder/file1.txt") and not os.path.exists("test_folder/new_file1.txt"):
    with open("test_folder/file1.txt", "w") as f:
        f.write("Hello from file1")
    with open("test_folder/file2.txt", "w") as f:
        f.write("Hello from file2")

print("1. Rename files with prefix")
print("2. Copy file (binary)")
print("3. List files and save")
print("4. Exit")
choice = int(input("Enter choice: "))

# ---------- a) rename with prefix ----------
if choice == 1:
    folder = "test_folder"
    prefix = "new_"

    for f in os.listdir(folder):
        old_path = os.path.join(folder, f)
        if os.path.isfile(old_path) and not f.startswith(prefix):
            new_name = prefix + f
            new_path = os.path.join(folder, new_name)
            os.rename(old_path, new_path)
            print("%s -> %s" % (f, new_name))

# ---------- b) copy file (binary) ----------
elif choice == 2:
    # pick any existing source - works no matter which option ran first
    if os.path.exists("test_folder/file1.txt"):
        source = "test_folder/file1.txt"
    elif os.path.exists("test_folder/new_file1.txt"):
        source = "test_folder/new_file1.txt"
    else:
        source = None

    if source is None:
        print("No source file found in test_folder")
    else:
        dest = "test_folder/copied.txt"
        with open(source, "rb") as src:
            with open(dest, "wb") as dst:
                while 1:
                    chunk = src.read(1024)
                    if chunk == b"":
                        break
                    dst.write(chunk)
        print("Copied %s -> %s" % (source, dest))

# ---------- c) list files and save ----------
elif choice == 3:
    folder = "test_folder"
    output = "test_folder/list.txt"

    with open(output, "w") as out:
        for f in os.listdir(folder):
            out.write(f + "\n")
            print(f)

    print("List saved to %s" % output)

elif choice == 4:
    print("Bye")

else:
    print("Invalid choice")
