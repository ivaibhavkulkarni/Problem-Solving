s = input()

word = s.split()
first_word = min(word, key = lambda x:x.lower())
print(first_word)