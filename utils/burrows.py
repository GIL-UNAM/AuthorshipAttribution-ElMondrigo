import math
import nltk
import matplotlib.pyplot as plt
from .loaders import read_files_into_string
from .books_info import corpus

def burrows():
    author_tokens = {}
    for author in corpus.keys():
        texts = read_files_into_string(corpus[author])
        tokens = nltk.word_tokenize(texts)
        author_tokens[author] = ([token.lower() for token in tokens if any(c.isalpha() for c in token)])

    whole_corpus = []
    for author in corpus.keys():
        whole_corpus += author_tokens[author]

    whole_corpus_freq_dist = list(nltk.FreqDist(whole_corpus).most_common(30))

    features = [word for word,freq in whole_corpus_freq_dist]
    feature_freqs = {}

    for author in corpus.keys():
        feature_freqs[author] = {} 
        
        overall = len(author_tokens[author])
        
        for feature in features:
            presence = author_tokens[author].count(feature)
            feature_freqs[author][feature] = presence / overall

    corpus_features = {}

    # For each feature...
    for feature in features:
        # crear el diccionario con el promedio y la desviacion estandar
        corpus_features[feature] = {}
        
        # promedio de ocurrencias
        feature_average = 0
        for author in corpus.keys():
            feature_average += feature_freqs[author][feature]
        feature_average /= len(corpus.keys())
        corpus_features[feature]["Mean"] = feature_average
        
        # Desviacion estandar
        feature_stdev = 0
        for author in corpus.keys():
            diff = feature_freqs[author][feature] - corpus_features[feature]["Mean"]
            feature_stdev += diff*diff
        feature_stdev /= (len(corpus.keys()) - 1)
        feature_stdev = math.sqrt(feature_stdev)
        corpus_features[feature]["StdDev"] = feature_stdev

    feature_zscores = {}
    for author in corpus.keys():
        feature_zscores[author] = {}
        for feature in features:
            
            # Calcular Z
            feature_val = feature_freqs[author][feature]
            feature_mean = corpus_features[feature]["Mean"]
            feature_stdev = corpus_features[feature]["StdDev"]
            feature_zscores[author][feature] = ((feature_val-feature_mean) / 
                                                feature_stdev)

    # tokenize
    mondrigo = read_files_into_string(corpus["El Mondrigo"])
    testcase_tokens = nltk.word_tokenize(mondrigo)
        
    # lowercase
    testcase_tokens = [token.lower() for token in testcase_tokens 
                    if any(c.isalpha() for c in token)]
    
    # Calcular atributos de prueba
    overall = len(testcase_tokens)
    testcase_freqs = {}
    for feature in features:
        presence = testcase_tokens.count(feature)
        testcase_freqs[feature] = presence / overall
        
    # Calcular Z de prueba
    testcase_zscores = {}
    for feature in features:
        feature_val = testcase_freqs[feature]
        feature_mean = corpus_features[feature]["Mean"]
        feature_stdev = corpus_features[feature]["StdDev"]
        testcase_zscores[feature] = (feature_val - feature_mean) / feature_stdev
        # print("Test case z-score for feature", feature, "is", testcase_zscores[feature])

    for author in corpus.keys():
        delta = 0
        for feature in features:
            delta += math.fabs((testcase_zscores[feature] - 
                                feature_zscores[author][feature]))
        delta /= len(features)
        print(author, delta)