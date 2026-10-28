filename = "sample.txt"

with open(filename, "r") as file:
    text = file.read()

# ---------- a) letter frequency (using isalpha) ----------
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
search_word = "the"
count = 0
for w in words:
    if w.lower() == search_word:
        count = count + 1
print("--- '%s' appears %d times ---" % (search_word, count))

# ---------- d) longest word ----------
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
print("")
print("--- Longest word = %s (length %d) ---" % (longest, len(longest)))
