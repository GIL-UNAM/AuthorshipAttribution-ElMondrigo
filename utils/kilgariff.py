import nltk

def read_files_into_string(filenames):
    strings = []
    for filename in filenames:
        with open(f'../data/corpus/{filename}.txt',encoding="utf-8") as f:
            strings.append(f.read())
    return '\n'.join(strings)

corpus = {}
corpus["Emilio Uranga"] = ["uranga1", "uranga2", "uranga3", "uranga4", "uranga5", "uranga6", "uranga7", "uranga8", "uranga9"]
corpus["Blanco Moheno"] = ["blancomoheno1", "blancomoheno1b", "blancomoheno2", "blancomoheno2b", "blancomoheno3", "blancomoheno4"]
corpus["Jorge Joseph"] = ["jorgejoseph1", "jorgejoseph2", "jorgejoseph3", "jorgejoseph4", "jorgejoseph5"]
corpus["Ortega Molina"] = ["ortegamolina1", "ortegamolina2", "ortegamolina3"]
corpus["Ortega Hernandez"] = ["ortegahernandez1", "ortegahernandez2", "ortegahernandez3"]
corpus["El Mondrigo"] = ["mondrigo"]
corpus["Alberto Chimal"] = [f'albertochimal{i}' for i in range(1,10)]

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
 












