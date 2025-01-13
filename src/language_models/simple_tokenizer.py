import io
import re
import time

start_time = time.time()

input_file = "sample.txt"
tokens_file = "sample_tokens.txt"

general_regex = r"[^\w.,-:]"
hyphen_regex = r"(?<=[^\w])-|-(?=[^\w])"
coma_regex = r"(?<=[^0-9]),|,(?=[^0-9])"
semicolon_regex = r"(?<=[^0-9]):|:(?=[^0-9])"
period_regex = r"(?<=[\W])\.|\.(?=[\W])|(?<=\d)\.(?=[^\W\d])|(?<=[^\W\d])\.(?=\d)|(?<=[\w].)\."

with io.open(input_file, encoding='utf8') as file: 
  text = file.read()
  file.close()

text = text.replace("”-", "")
text = text.replace("\"-", "")
text = text.replace("”", "")
text = text.replace("\"", "")
text = text.replace("\'", "")

tokens = re.split(general_regex + "|" + hyphen_regex + "|" + coma_regex + "|" + period_regex + "|" + semicolon_regex, text)
tokens = list(filter(None, tokens))

with io.open(tokens_file, 'w', encoding="utf8") as file:
  for token in tokens:
    file.write(token + "\n")
  file.close()

end_time = time.time()

print("Time spent: " + str(end_time - start_time) + " seconds")