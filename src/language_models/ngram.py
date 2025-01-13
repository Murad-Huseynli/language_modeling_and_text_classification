import io
from nltk.util import ngrams

input_file = "tokens.txt"
unigram_file = "unigram.txt"
bigram_file = "bigram.txt"
trigram_file = "trigram.txt"

with io.open(input_file, encoding='utf8') as file: 
  text = file.read()
  file.close()
tokens = text.split("\n")

unigrams=ngrams(tokens, 1)
bigrams=ngrams(tokens, 2)
trigrams=ngrams(tokens, 3)

unigram_dict = {}
bigram_dict = {}
trigram_dict = {}

for uni in unigrams:
  if uni not in unigram_dict:
    unigram_dict[uni] = 0
  unigram_dict[uni] += 1

for bi in bigrams:
  if bi not in bigram_dict:
    bigram_dict[bi] = 0
  bigram_dict[bi] += 1

for tri in trigrams:
  if tri not in trigram_dict:
    trigram_dict[tri] = 0
  trigram_dict[tri] += 1

with io.open(unigram_file, 'w', encoding="utf-8") as file:
  for uni in unigram_dict:
    file.write(uni[0] + " " + str(unigram_dict[uni]) + " " + str(unigram_dict[uni] / len(tokens)) + "\n")
  file.close()

with io.open(bigram_file, 'w', encoding="utf-8") as file:
  for bi in bigram_dict:
    file.write(bi[0] + " " + bi[1] + " " + str(bigram_dict[bi]) + " " + str(bigram_dict[bi] / unigram_dict[(bi[0],)]) + "\n")
  file.close()

with io.open(trigram_file, 'w', encoding="utf-8") as file:
  for tri in trigram_dict:
    file.write(tri[0] + " " + tri[1] + " " + tri[2] + " " + str(trigram_dict[tri]) + " " + str(trigram_dict[tri] / bigram_dict[(tri[0],tri[1],)]) + "\n")
  file.close()

sorted_uni = sorted(unigram_dict.items(), key=lambda kv: kv[1], reverse=True)
sorted_bi = sorted(bigram_dict.items(), key=lambda kv: kv[1], reverse=True)
sorted_tri = sorted(trigram_dict.items(), key=lambda kv: kv[1], reverse=True)

for i in range(0, 5):
  uni = sorted_uni[i][0]
  print(" " + uni[0] + " " + str(unigram_dict[uni]) + " " + str(unigram_dict[uni] / len(tokens)))
print()

for i in range(0, 5):
  bi = sorted_bi[i][0]
  print(" " + bi[0] + " " + bi[1] + " " + str(bigram_dict[bi]) + " " + str(bigram_dict[bi] / unigram_dict[(bi[0],)]))
print()

for i in range(0, 5):
  tri = sorted_tri[i][0]
  print(" " + tri[0] + " " + tri[1] + " " + tri[2] + " " + str(trigram_dict[tri]) + " " + str(trigram_dict[tri] / bigram_dict[(tri[0],tri[1],)]))
print()

unigram_perplexity = 1
for word, frequency in unigram_dict.items():
  probability = frequency / len(tokens)
  unigram_perplexity *= probability ** (-1 / len(unigram_dict))

bigram_perplexity = 1
for bigram, frequency in bigram_dict.items():
  probability = frequency / unigram_dict[(bigram[0],)]
  bigram_perplexity *= probability ** (-1 / len(bigram_dict))

trigram_perplexity = 1
for trigram, frequency in trigram_dict.items():
  probability = frequency / bigram_dict[(trigram[0],trigram[1])]
  trigram_perplexity *= probability ** (-1 / len(trigram_dict))

print(" Unigram Perplexity: " + str(unigram_perplexity))
print(" Bigram Perplexity: " + str(bigram_perplexity))
print(" Trigram Perplexity: " + str(trigram_perplexity))
print()
