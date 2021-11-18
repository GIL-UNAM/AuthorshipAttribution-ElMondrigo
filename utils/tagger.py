from nltk.tag.stanford import StanfordPOSTagger
from pathlib import Path
import os

def tagger():
    BASE_DIR = os.path.join(Path(__file__).resolve().parent.parent,"stanford")
    model_path = os.path.join(BASE_DIR, 'spanish-ud.tagger')
    jar_path = os.path.join(BASE_DIR, 'stanford-postagger-3.9.2.jar')
    spanish_postagger = StanfordPOSTagger(model_path, jar_path, encoding='utf8')

    sentences = [
		'esta es una primera oracion de primavera',
		'para destapar el tubo hay que usar drano',
		'la fiesta fue en el zocalo de la ciudad'
	]

    for sent in sentences:
        words = sent.split()
        tagged_words = spanish_postagger.tag(words)

        for (word, tag) in tagged_words:
            print(word + ' ' + tag)