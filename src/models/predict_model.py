import pandas as pd
import joblib
from sklearn.metrics import precision_score, f1_score, recall_score
from src.config import *
import json

X_test = pd.read_pickle(X_test_path)
Y_test = pd.read_pickle(Y_test_path)
model = joblib.load(model_path)

y_predict = model.predict(X_test)

metric_result = {}
if score_metric == 'f1':
    metric_result['f1'] = f1_score(Y_test, y_predict, average='samples')
if score_metric == 'precision':
    metric_result['precision'] = precision_score(Y_test, y_predict, average='samples')
if score_metric == 'recall':
    metric_result['recall'] = recall_score(Y_test, y_predict, average='macro')

with open(score_path, 'w') as f:
    json.dump(metric_result, f)

