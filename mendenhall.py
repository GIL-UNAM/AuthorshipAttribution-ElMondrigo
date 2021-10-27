import nltk
import matplotlib.pyplot as plt

def read_files_into_string(filenames):
	strings = []
	for filename in filenames:
		with open(f'corpus/{filename}.txt',encoding="utf-8") as f:
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

for author in corpus.keys():
	author_tokens = {}
	author_length_distributions = {}
	uranga_texts = read_files_into_string(corpus[author])
	uranga_tokens = nltk.word_tokenize(uranga_texts)
	author_tokens[author] = ([token for token in uranga_tokens if any(c.isalpha() for c in token)])
	token_lengths = [len(token) for token in author_tokens[author]]
	author_length_distributions[author] = nltk.FreqDist(token_lengths)
	author_length_distributions[author].plot(15, title=author)
    
    