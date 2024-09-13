from textblob import TextBlob

words = ["Machie", "Learnin"]
corrected_words = [ ]

for i in words:
    corrected_words.append(TextBlob(i))

print("wrong words :", words)
print("Corrected words are:")

for i in corrected_words:
    print(i.correct(), end= " ")

