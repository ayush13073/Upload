"""
Question 6: Read and write binary image file.

Before running this program, put an image file in this folder
and name it photo.png (or change the file name below).
"""

try:
    with open("photo.png", "rb") as f:
        data = f.read()

    print("Original image size:", len(data), "bytes")

    with open("copy.png", "wb") as f:
        f.write(data)

    print("Copy created as copy.png")

    with open("copy.png", "rb") as f:
        copy_data = f.read()

    print("Copy image size:", len(copy_data), "bytes")

    if data == copy_data:
        print("Both files are same")
    else:
        print("Files are different")

except FileNotFoundError:
    print("photo.png not found. Please put an image named photo.png in this folder.")
