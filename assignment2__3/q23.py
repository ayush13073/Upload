word_list = ["apple", "banana", "apple", "cherry",
             "banana", "apple", "mango", "cherry"]


# unique_words = set(word_list)

# for word in unique_words:
#     count = 0
#     for w in word_list:
#         if w == word:
#             count = count + 1
#     print("%-10s->  %d" % (word, count))

unique = set(word_list)

for word in unique:
    count = 0
    for w in word_list:
        if w == word:
            count = count + 1
    print("%-10s -> %d" % (word, count))