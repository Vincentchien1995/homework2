f =open('/Users/vincentchien/Desktop/text.txt','r')
text = f.read()
text = text.replace(',','').replace('.','')
word=text.split()
print(len(word))

# #reads a text file containing some English text and counts all words that are:
# a) at least 4 letters long and
# b) start with a capital letter or are all capitalized (abbreviations etc.)
word_count = 0
for a in word:
  if len(a)>=4 and str.isupper(a) or str.istitle(a):
    word_count += 1
print(word_count)


