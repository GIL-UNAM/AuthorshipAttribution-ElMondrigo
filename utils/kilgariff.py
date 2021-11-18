import nltk
from .loaders import read_files_into_string
from .books_info import corpus

def kilgariff():
    author_tokens = {}
    for author in corpus.keys():
        texts = read_files_into_string(corpus[author])
        tokens = nltk.word_tokenize(texts)
        author_tokens[author] = ([token.lower() for token in tokens if any(c.isalpha() for c in token)])

    for author in corpus.keys():
        joint_corpus = (author_tokens[author] + author_tokens["El Mondrigo"])
        joint_freq_dist = nltk.FreqDist(joint_corpus)
        most_common = list(joint_freq_dist.most_common(500))
        author_share = (len(author_tokens[author]) / len(joint_corpus))
        chisquared = 0
        for word,joint_count in most_common:
            author_count = author_tokens[author].count(word)
            disputed_count = author_tokens["El Mondrigo"].count(word)
            
            expected_author_count = joint_count * author_share
            expected_disputed_count = joint_count * (1-author_share)
            
            chisquared += ((author_count-expected_author_count) * 
                        (author_count-expected_author_count) / 
                        expected_author_count)
                        
            chisquared += ((disputed_count-expected_disputed_count) *
                        (disputed_count-expected_disputed_count) 
                        / expected_disputed_count)

        print(author, chisquared)