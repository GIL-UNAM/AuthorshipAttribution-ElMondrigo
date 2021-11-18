import os 
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent.parent)
def read_files_into_string(filenames):
	strings = []
	for filename in filenames:
		with open(os.path.join(BASE_DIR,"data","corpus",f"{filename}.txt"),encoding="utf-8") as f:
			strings.append(f.read())
	return '\n'.join(strings)