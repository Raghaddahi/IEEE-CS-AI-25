sentence=input()
words= sentence.split()
reversed_words=[]
for i in words:
    reversed_words.append(i[::-1])
reversed_sentence=" ".join(reversed_words)
print(reversed_sentence)
