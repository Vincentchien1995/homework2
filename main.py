# reads a text file containing some English text and counts all words that are:
# a) at least 4 letters long and
# b) start with a capital letter or are all capitalized (abbreviations etc.)

f =open('/Users/vincentchien/Desktop/text.txt','r')
text = f.read()
text = text.replace(',','').replace('.','')
word=text.split()

# word_count = 0
# for a in word:
#   if len(a)>=4 and str.isupper(a) or str.istitle(a):
#     word_count += 1
# print(word_count)

# Print a list of those words and the number of their occurrences
word_dic={}
for i in word:
  if i in word_dic and len(i)>=4 and str.isupper(i) or str.istitle(i):
    word_dic[i] += 1
  else:
    word_dic[i] = 1
print(word_dic)

# Use matplotlib or plotly and generate a bar chart showing the top 10 most common words (same conditions 1a) and 1b) apply) with the number of their occurrences in descending order.
