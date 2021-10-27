from nltk.tag.stanford import StanfordPOSTagger
import os

java_path = "C:\\Program Files\\Java\\jdk1.8.0_291\\bin\\java.exe"
os.environ['JAVAHOME'] = java_path

BASE_DIR = os.path.join(os.getcwd(),"stanford")
model_path = os.path.join(BASE_DIR, 'spanish-ud.tagger')
jar_path = os.path.join(BASE_DIR, 'stanford-postagger-3.9.2.jar')
spanish_postagger = StanfordPOSTagger(model_path, jar_path, encoding='utf8')

sentences = ['esta es una primera oracion de primavera', 'para destapar el tubo hay que usar drano', 'la fiesta fue en el zocalo de la ciudad']

for sent in sentences:
	words = sent.split()
	tagged_words = spanish_postagger.tag(words)

	for (word, tag) in tagged_words:
		print(word + ' ' + tag)
		