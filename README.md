# Language Modeling and Text Classification

## About The Project

This project implements and evaluates various language modeling techniques and text classification methods, with a special focus on Azerbaijani language processing. The project combines n-gram language models with different smoothing techniques and implements text classification using Naive Bayes approaches. The models are trained and evaluated on a custom dataset scraped from popular Azerbaijani news channels on Telegram, providing a unique corpus of contemporary Azerbaijani language usage in news context.

### Key Features

* N-gram language models (unigram, bigram, trigram)
* Multiple smoothing implementations
* Azerbaijani language text classification
* Perplexity evaluation metrics
* Comprehensive comparison analysis

### Built With

* Python
* NLTK
* NumPy
* Scikit-learn
* Telethon (for Telegram data collection)
* Custom NLP tools

## Components

### 1. Language Modeling
* Unigram model implementation
* Bigram model implementation
* Trigram model implementation
* Perplexity calculation
* Model evaluation and comparison

### 2. Smoothing Techniques
* Laplace (Add-one) smoothing
* Interpolation smoothing
* Backoff smoothing
* Kneser-Ney smoothing
* Comparative analysis of smoothing methods

### 3. Text Classification
* Dataset translation pipeline for Azerbaijani
* Naive Bayes implementation
* Binary Naive Bayes implementation
* Polarity classification
* Subjectivity classification

## Dataset

### Data Collection
The project uses a custom dataset collected from Azerbaijani news channels on Telegram. The data collection process involved:
* Automated scraping of messages from news channels
* Text cleaning and preprocessing
* Message filtering and validation
* Dataset structuring for language modeling and classification tasks

### Dataset Statistics
* Source: Telegram news channels
* Language: Azerbaijani
* Content type: News articles and updates

### Data Preprocessing
* Removal of non-Azerbaijani content
* Cleaning of special characters and formatting
* Tokenization specific to Azerbaijani language
* Normalization of news-specific terms
* Handling of common abbreviations and symbols


## Experimental Results

### Language Model Performance

#### N-gram Models
The implementation included unigram, bigram, and trigram models, with frequency and probability calculations for each n-gram pattern in the dataset.

#### Perplexity Analysis
Perplexity scores were calculated for each model to evaluate their performance:
* Unigram Perplexity
* Bigram Perplexity
* Trigram Perplexity

#### Smoothing Techniques
Multiple smoothing methods were implemented and compared:
* Laplace Smoothing
* Interpolation Smoothing
* Backoff Smoothing
* Kneser-Ney Smoothing

### Classification Results

#### Sentiment Analysis (Positive/Negative)
Both classification approaches showed similar performance levels for sentiment analysis:
* Naive Bayes Accuracy: ~<b>67%</b>
* Binary Naive Bayes Accuracy: ~<b>67%</b>

Key observations:
* Moderate performance for binary sentiment classification
* Similar performance between standard and binary implementations
* Room for improvement in sentiment detection

#### Subjectivity Analysis (Objective/Subjective)
Both classifiers demonstrated strong performance in subjectivity detection:
* Naive Bayes Accuracy: ~<b>89%</b>
* Binary Naive Bayes Accuracy: ~<b>89%</b>

Key observations:
* High accuracy in distinguishing objective from subjective content
* Consistent performance across both implementation approaches
* Strong reliability for subjectivity classification


## Key Findings

1. N-gram Language Models
   * Successfully implemented unigram, bigram, and trigram models
   * Calculated comprehensive frequency and probability distributions
   * Evaluated model performance through perplexity metrics

2. Smoothing Methods
   * Implemented multiple smoothing techniques
   * Evaluated each method's impact on model performance
   * Compared effectiveness across different approaches

3. Classification Performance
   * Strong performance in subjectivity classification (89% accuracy)
   * Moderate performance in sentiment analysis (67% accuracy)
   * Consistent results between standard and binary implementations

## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Project Link: [https://github.com/Murad-Huseynli/language_modeling_and_text_classification.gitg](https://github.com/Murad-Huseynli/language_modeling_and_text_classification.git)

