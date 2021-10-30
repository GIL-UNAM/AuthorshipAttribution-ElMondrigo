import csv
import os 
import re
import pandas as pd
from books_info import books, train_test_split_base
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_score

BASE_FOLDER = os.getcwd()

files = os.listdir(os.path.join(BASE_FOLDER,'data'))
autors = ['chimal','mondrigo']
marcadores = set(re.search(r'[a-z]+_(?P<name>[A-Z0-9]+)\.csv$',file).group("name") for file in files)
index = 1


#for type in marcadores:
for type in ["BC"]:
   os.chdir(BASE_FOLDER)
   print(f'-------------{type}------------')
   chimal = pd.read_csv(f'./data/{autors[0]}_{type}.csv')
   mondrigo = pd.read_csv(f'./data/{autors[1]}_{type}.csv')
   full_metrics = mondrigo.set_index('doc_id').combine_first(chimal.set_index('doc_id')).fillna(0)
   x_train, x_test, y_train, y_test = train_test_split_base(full_metrics)

   row_csv = {'marcador':type}
   best_cross_score = 0
   best_test_score = 0
   best_model_type = {}
   for kernel in ["linear","sigmoid","rbf","poly"]:
      param_grid = {
         'C': [0.001,0.01,0.1,1,10,100,1000],
         'gamma': [0.001,0.01,0.1,1,10,100,1000],
         'degree': [i for i in range(3,8)]
      }
      cv = StratifiedKFold(n_splits=2,shuffle=True)
      grid = GridSearchCV(SVC(kernel=kernel), param_grid, cv = cv, refit = True,scoring='precision_micro') 
      grid.fit(x_train, y_train)
      
      test_score = round(grid.score(x_test,y_test),4)
      cross_score = round(grid.best_score_,4)
      print('&'*40)
      print(test_score)
      print(cross_score)
      if kernel != 'poly':
         grid.best_params_.pop('degree')

      if (test_score - best_test_score) > 0.001:
         best_test_score = test_score
         best_cross_score = cross_score
         best_model_type = {"kernel":kernel} | grid.best_params_
      elif (test_score - best_test_score) >= 0.0 and (cross_score - best_cross_score) > 0.1:
         best_test_score = test_score
         best_cross_score = cross_score
         best_model_type = {"kernel":kernel} | grid.best_params_       

      message = ""
      i=1
      iterador = (
         grid.best_params_|\
         {'cross-validation-score':f'{cross_score*100}%'}| \
         {'test-score': f'{test_score*100}%'}
      ).items()
      for key,value in iterador:
         message+=f'{key}: {value}'
         if i != len(iterador):
            message+='\n'
         i+=1

      row_csv[kernel] = message
   
   final_model = SVC(**best_model_type,probability=True)
   mondrigo.set_index('doc_id',inplace=True)
   mask = mondrigo.index != 68787
   final_model.fit(mondrigo.loc[mask],[books[key][0] for key in mondrigo.loc[mask].index])
   print(best_model_type)
   print(final_model.classes_)
   print(final_model.predict_proba(mondrigo.loc[[68787]]))

   
   SVM_FOLDER = os.path.join(BASE_FOLDER,'ouput_SVM')
   if not os.path.exists(SVM_FOLDER):
      os.makedirs(SVM_FOLDER)
   os.chdir(SVM_FOLDER)
   
   with open('SVM_results_Original.csv', 'a',newline='') as f:
      writer_f = csv.DictWriter(f, fieldnames=["marcador","linear","sigmoid","rbf","poly"])
      if index == 1:
         writer_f.writeheader()
      writer_f.writerow(row_csv)
   
   index+=1