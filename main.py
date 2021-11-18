import sys
from utils.burrows import burrows
from utils.clustering import clustering
from utils.kilgariff import kilgariff
from utils.mendenhall import mendenhall
from utils.tagger import tagger
from utils.SVM_Chimal import SVM_Chimal
from utils.SVM import SVM

if __name__ == "__main__":
    args = sys.argv
    if 'burrows' in args:
        print('-'*40,' BURROWS ','-'*40)
        burrows()
    if 'clustering' in args:        
        print('-'*40,' CLUSTERING ','-'*40)
        clustering()
    if 'kilgariff' in args:
        print('-'*40,' KILGARIFF ','-'*40)
        kilgariff()
    if 'mendenhall' in args:
        print('-'*40,' MENDENHALL ','-'*40)
        mendenhall()
    if 'tagger' in args:
        print('-'*40,' TAGGER ','-'*40)
        tagger()
    if 'svm_Chimal' in args:
        print('-'*40,' SVM_CHIMAL ','-'*40)
        SVM_Chimal()
    if 'svm' in args:
        print('-'*40,' SVM ','-'*40)
        SVM()