f =open('/Users/vincentchien/Desktop/text.txt','r')
text = f.read()
text = text.replace(',','').replace('.','')
word=text.split()
print(len(word))

word_count = 0
for a in word:
  if len(a)>4:
    word_count += 1
  return word_count

print(word_count)


