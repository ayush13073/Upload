"""
Question 1: Count below contents in file.
a. Count each letter Frequency in file
b. Words
c. Occurrences of specific words
d. Find longest word in file
"""
filename = input("Enter file name: ")

with open(filename, "r") as file:
    text = file.read()

# ---------- a) letter frequency using isalpha() ----------
print("")
print("--- Letter frequency ---")
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

# ---------- b) total words ----------
words = text.split()
print("")
print("--- Total words = %d ---" % len(words))

# ---------- c) occurrences of specific word ----------
search_word = input("Enter word to search: ")
count = 0
for w in words:
    if w == search_word:
        count = count + 1
print("--- '%s' appears %d times ---" % (search_word, count))

# ---------- d) longest word ----------
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
print("")
print("--- Longest word = %s (length %d) ---" % (longest, len(longest)))