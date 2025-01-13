import io
import math
import re
import random

def tokenize(text : str) -> list:
  tokens = []

  general_regex = r"[^\w.,-:]"
  hyphen_regex = r"(?<=[^\w])-|-(?=[^\w])"
  coma_regex = r"(?<=[^0-9]),|,(?=[^0-9])"
  semicolon_regex = r"(?<=[^0-9]):|:(?=[^0-9])"
  period_regex = r"(?<=[\W])\.|\.(?=[\W])|(?<=\d)\.(?=[^\W\d])|(?<=[^\W\d])\.(?=\d)|(?<=[\w].)\."

  text = text.replace("”-", "")
  text = text.replace("\"-", "")
  text = text.replace("”", "")
  text = text.replace("\"", "")
  text = text.replace("\'", "")

  tokens = re.split(general_regex + "|" + hyphen_regex + "|" + coma_regex + "|" + period_regex + "|" + semicolon_regex, text)
  return tokens

input_file = "sample_tokens.txt"
pos_file = "txt_sentoken/obj.txt"
neg_file = "txt_sentoken/subj.txt"

with io.open(pos_file, encoding='utf8') as file: 
  text = file.read()
  file.close()
pos = text.split("\n")

with io.open(neg_file, encoding='utf8') as file: 
  text = file.read()
  file.close()
neg = text.split("\n")

pos_dict = {}
neg_dict = {}
pos_cnt_train = round(0.8 * len(pos))
neg_cnt_train = round(0.8 * len(neg))
pos_word_cnt = 0
neg_word_cnt = 0
total_cnt = pos_cnt_train + neg_cnt_train

# pos_train = []
pos_test = []
tmp_cnt = 0
i = 0
for sent in pos:  
  i += 1
  tokens = tokenize(sent)
  tmp = random.random()
  if len(pos) - i < pos_cnt_train or tmp_cnt == pos_cnt_train or tmp <= 0.2:
    pos_test.append(sent)
    continue
  pos_word_cnt += len(tokens)
  tmp_cnt += 1
  used = []
  for token in tokens:
    if token == "":
      continue
    if token not in pos_dict:
      pos_dict[token] = 0
    if token not in used:
      pos_dict[token] += 1
      used.append(token)

# neg_train = []
neg_test = []
tmp_cnt = 0
i = 0
for sent in neg:
  i += 1
  tokens = tokenize(sent)
  tmp = random.random()
  if len(neg) - i < pos_cnt_train or tmp_cnt == neg_cnt_train or tmp <= 0.2:
    neg_test.append(sent)
    continue
  tmp_cnt += 1
  neg_word_cnt += len(tokens)
  used = []
  for token in tokens:
    if token == "":
      continue
    if token not in neg_dict:
      neg_dict[token] = 0
    if token not in used:
      neg_dict[token] += 1
      used.append(token)

# with io.open(input_file, encoding='utf8') as file: 
#   text = file.read()
#   file.close()
# words = text.split("\n")

corr, tot = 0, 0
for sent in pos_test:
  tot += 1
  prob_pos = math.log(pos_cnt_train / total_cnt)
  prob_neg = math.log(neg_cnt_train / total_cnt)

  words = tokenize(sent)
  for word in words:
    if word == "":
      continue
    if word in pos_dict:
      prob_pos += math.log((pos_dict[word] + 1) / (pos_word_cnt + len(pos_dict)))
    else:
      prob_pos += math.log(1 / (pos_word_cnt + len(pos_dict)))

    if word in neg_dict:
      prob_neg += math.log((neg_dict[word] + 1) / (neg_word_cnt + len(neg_dict)))
    else:
      prob_neg += math.log(1 / (neg_word_cnt + len(neg_dict)))
    
  if (prob_pos > prob_neg):
    corr += 1

for sent in neg_test:
  tot += 1
  prob_pos = math.log(pos_cnt_train / total_cnt)
  prob_neg = math.log(neg_cnt_train / total_cnt)

  words = tokenize(sent)
  for word in words:
    if word == "":
      continue
    if word in pos_dict:
      prob_pos += math.log((pos_dict[word] + 1) / (pos_word_cnt + len(pos_dict)))
    else:
      prob_pos += math.log(1 / (pos_word_cnt + len(pos_dict)))

    if word in neg_dict:
      prob_neg += math.log((neg_dict[word] + 1) / (neg_word_cnt + len(neg_dict)))
    else:
      prob_neg += math.log(1 / (neg_word_cnt + len(neg_dict)))
    
  if (prob_pos < prob_neg):
    corr += 1

print("Accuracy: " + str(corr / tot))
print()

while True:
  sent = input()
  words = tokenize(sent)
  
  prob_pos = math.log(pos_cnt_train / total_cnt)
  prob_neg = math.log(neg_cnt_train / total_cnt)

  for word in words:
    if word == "":
      continue
    if word in pos_dict:
      prob_pos += math.log((pos_dict[word] + 1) / (pos_word_cnt + len(pos_dict)))
    else:
      prob_pos += math.log(1 / (pos_word_cnt + len(pos_dict)))

    if word in neg_dict:
      prob_neg += math.log((neg_dict[word] + 1) / (neg_word_cnt + len(neg_dict)))
    else:
      prob_neg += math.log(1 / (neg_word_cnt + len(neg_dict)))
    
  print(prob_neg)
  print(prob_pos)

  if prob_neg < prob_pos:
    print("Obj")
  else:
    print("Subj")