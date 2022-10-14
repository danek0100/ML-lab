import pandas as pd
import joblib

from sklearn.model_selection import *

from catboost import Pool
from catboost import CatBoostClassifier

from src.config import *

train = pd.read_pickle(processed_data_for_train_pkl)
target = pd.read_pickle(target_data_train_pkl)

# train = pd.read_pickle("../../" + processed_data_for_train_pkl)
# target = pd.read_pickle("../../" +target_data_train_pkl)

X_train, X_test, Y_train, Y_test = train_test_split(train, target, train_size=train_size, random_state=seed)
pool = Pool(X_train, Y_train, cat_features=CATEGORIES_COL)
model = CatBoostClassifier(iterations=iterations, loss_function=loss_function,
                           eval_metric=eval_metric, learning_rate=learning_rate,
                           bootstrap_type=bootstrap_type, boost_from_average=boost_from_average,
                           leaf_estimation_iterations=leaf_estimation_iterations,
                           leaf_estimation_method=leaf_estimation_method)
model.fit(pool)
joblib.dump(model, model_path)
