import os
import nltk
from pathlib import Path
import matplotlib.pyplot as plt
from .loaders import read_files_into_string
from .books_info import corpus

BASE_DIR = Path(__file__).resolve().parent.parent

def mendenhall():
    for author in corpus.keys():
        fig = plt.figure(figsize = (20,20))
        author_tokens = {}
        author_length_distributions = {}
        uranga_texts = read_files_into_string(corpus[author])
        uranga_tokens = nltk.word_tokenize(uranga_texts)
        author_tokens[author] = ([token for token in uranga_tokens if any(c.isalpha() for c in token)])
        token_lengths = [len(token) for token in author_tokens[author]]
        author_length_distributions[author] = nltk.FreqDist(token_lengths)
        plt.ion()
        author_length_distributions[author].plot(15, title=author)
        fig.savefig(os.path.join(BASE_DIR,"output_mendenhall",f"{author}.png"), bbox_inches = "tight")
        plt.ioff()