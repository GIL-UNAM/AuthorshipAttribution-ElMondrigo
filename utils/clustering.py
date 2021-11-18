import os
import nltk
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from .loaders import read_files_into_string
from .books_info import corpus

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tag.stanford import StanfordPOSTagger

BASE_DIR = os.path.join(Path(__file__).resolve().parent.parent,"stanford")
model_path = os.path.join(BASE_DIR, 'spanish-ud.tagger')
jar_path = os.path.join(BASE_DIR, 'stanford-postagger-3.9.2.jar')
spanish_postagger = StanfordPOSTagger(model_path, jar_path, encoding='utf8')

def token_to_pos(t):
    print(t)
    return [p[1] for p in spanish_postagger.tag(t)]

def clustering():
    fvs_lexical = np.zeros((len(corpus.keys()), 3), np.float64)
    fvs_punct = np.zeros((len(corpus.keys()), 3), np.float64)

    full_text_list = []
    author_tokens_words_only = {}
    author_tokens_with_punctuation = {}
    author_sentences = {}
    author_vocabulary = {}
    author_tokens_per_sentence = {}
    author_words_per_sentence = {}
    authors = []
    for e, author in enumerate(corpus.keys()):
        authors.append(author)
        text = read_files_into_string(corpus[author])
        full_text_list.append(text)
        author_tokens_with_punctuation[author] = nltk.word_tokenize(text.lower())
        author_tokens_words_only[author] = ([token.lower() for token in author_tokens_with_punctuation[author] 
            if any(c.isalpha() for c in token)])
        author_sentences[author] = nltk.sent_tokenize(text)
        author_vocabulary[author] = set(author_tokens_words_only[author])

        author_tokens_per_sentence[author] = [nltk.word_tokenize(s.lower()) for s in author_sentences[author]]	
        author_words_per_sentence[author] = np.array([len(sentence) for sentence in author_tokens_per_sentence[author]])
        fvs_lexical[e,0] = author_words_per_sentence[author].mean()
        fvs_lexical[e,1] = author_words_per_sentence[author].std()
        fvs_lexical[e,2] = len(author_vocabulary[author])/float(len(author_tokens_words_only[author]))

        fvs_punct[e,0] = author_tokens_with_punctuation[author].count(',') / float(len(author_sentences[author]))
        fvs_punct[e,1] = author_tokens_with_punctuation[author].count(';') / float(len(author_sentences[author]))
        fvs_punct[e,2] = author_tokens_with_punctuation[author].count(':') / float(len(author_sentences[author]))

    NUM_TOP_WORDS = 10
    all_tokens = []
    for author in corpus.keys():
        all_tokens = all_tokens + author_tokens_words_only[author]
        
    fdist = nltk.FreqDist(all_tokens)
    vocabulary_most_common = list(fdist.most_common(NUM_TOP_WORDS))
    vocabulary = [word for (word,freq) in vocabulary_most_common]

    vectorizer = CountVectorizer(vocabulary = vocabulary, tokenizer = nltk.word_tokenize)
    fvs_bow = vectorizer.fit_transform(full_text_list).toarray().astype(np.float64)
    fvs_bow /= np.c_[np.apply_along_axis(np.linalg.norm, 1, fvs_bow)]

    print(authors)

    k_means = KMeans(n_clusters=6, init='k-means++', n_init=10, verbose=0)
    k_means.fit(fvs_lexical)
    k_means_labels = k_means.labels_
    print(k_means_labels)

    k_means = KMeans(n_clusters=6, init='k-means++', n_init=10, verbose=0)
    k_means.fit(fvs_punct)
    k_means_labels = k_means.labels_
    print(k_means_labels)

    k_means = KMeans(n_clusters=6, init='k-means++', n_init=10, verbose=0)
    k_means.fit(fvs_bow)
    k_means_labels = k_means.labels_
    print(k_means_labels)