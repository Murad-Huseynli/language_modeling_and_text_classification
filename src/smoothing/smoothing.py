import io
import nltk
from nltk import ngrams
from collections import Counter
import math

# Read the dataset from a file
with io.open("tokens.txt", encoding='utf8') as file: 
  text = file.read()
corpus = text.split("\n")

# Define a function to calculate n-gram frequencies
def calculate_ngram_freqs(n, corpus):
    ngrams = nltk.ngrams(corpus, n)
    freqs = Counter(ngrams)
    return freqs

# Calculate unigram, bigram, and trigram frequencies
unigram_freqs = calculate_ngram_freqs(1, corpus)
bigram_freqs = calculate_ngram_freqs(2, corpus)
trigram_freqs = calculate_ngram_freqs(3, corpus)

# Define a function to apply Laplace smoothing
def laplace_smoothing(ngram_freqs, vocabulary_size, alpha=1):
    smoothed_freqs = {}
    for ngram, freq in ngram_freqs.items():
        smoothed_freqs[ngram] = (freq + alpha) / (sum(ngram_freqs.values()) + alpha * vocabulary_size)
    return smoothed_freqs

# Calculate Laplace-smoothed unigram, bigram, and trigram frequencies
unigram_laplace = laplace_smoothing(unigram_freqs, len(set(corpus)))
bigram_laplace = laplace_smoothing(bigram_freqs, len(set(corpus)))
trigram_laplace = laplace_smoothing(trigram_freqs, len(set(corpus)))

# Define a function to apply Interpolation smoothing
def interpolation_smoothing(ngram_freqs, n_minus_1_freqs, n_minus_2_freqs, lambda_1=0.5, lambda_2=0.3, lambda_3=0.2):
    smoothed_freqs = {}
    for ngram in ngram_freqs.keys():
        n_minus_1 = tuple(ngram[:-1])
        n_minus_2 = tuple(ngram[:-2])
        smoothed_freqs[ngram] = lambda_1 * ngram_freqs[ngram] / n_minus_1_freqs[n_minus_1] + lambda_2 * n_minus_1_freqs[n_minus_1] / n_minus_2_freqs.get(n_minus_2, 1) + lambda_3 * ngram_freqs[ngram[:-3:-1]] / len(ngram_freqs)
    return smoothed_freqs

# Calculate Interpolation-smoothed unigram, bigram, and trigram frequencies
unigram_interpolation = interpolation_smoothing(unigram_freqs, unigram_freqs, unigram_freqs)
bigram_interpolation = interpolation_smoothing(bigram_freqs, unigram_freqs, bigram_freqs)
trigram_interpolation = interpolation_smoothing(trigram_freqs, bigram_freqs, trigram_freqs)

def backoff(tokens, n, model, alpha=0.4):
    if n == 0:
        return model['']
    token_len = len(tokens)
    if token_len < n:
        return backoff(tokens, n - 1, model, alpha = alpha)
    history = ' '.join(tokens[token_len - n + 1 : token_len])
    token = tokens[token_len - 1]
    if history in model and token in model[history]:
        return model[history][token]
    else:
        return alpha * backoff(tokens, n - 1, model, alpha = alpha)

def kneser_ney(tokens, n, model, alpha = 0.75):
    token_len = len(tokens)
    lambda_weight = alpha / (token_len - n + 1)
    history = ' '.join(tokens[token_len - n + 1 : token_len])
    token = tokens[token_len-1]
    count = 0
    discount = 0
    if history in model:
        for t in model[history]:
            if model[history][t] > 0:
                count += 1
            else:
                discount += 1
        if token in model[history]:
            numerator = max(model[history][token] - discount, 0)
            denominator = sum(model[history].values())
            return numerator/denominator + lambda_weight * kneser_ney(tokens, n - 1, model, alpha = alpha)
        else:
            return lambda_weight * kneser_ney(tokens, n - 1, model, alpha = alpha)
    else:
        return backoff(tokens, n - 1, model, alpha=alpha)
