# filename = input("enter file name : ")

with open("sample.txt","r") as file:
    text = file.read()


print()

print("letter frequency")

lower_text = text.lower()

done = ""

for ch in lower_text:
    if ch.isalpha() and ch not in done:
        count = 0

        for c in lower_text:
            if c == ch:
                count = count + 1
        print("%s = %d" % (ch, count))
        done = done + ch

words = text.split()
print()

print("total words %d " % len(words))



# searchword = input("Enter the word ")
# count = 0
# # words = text.lower()
# for w in words:
    
#     if w == searchword:
#         count = count + 1

# print("%s appears %d " %(searchword, count))
        

longest =""

for w in words:
    if len(w) > len(longest):
        longest = w

print("")

print("longest word %s (length %d)" %(longest, len(longest)))