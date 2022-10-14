import pandas as pd
from src.features.functions import feature_generation
from src.config import *
from src.utils import save_as_pickle


train = pd.read_pickle(interim_data_for_train_pkl)
test = pd.read_pickle(interim_test_pkl)

train = feature_generation(train)
test = feature_generation(test)

save_as_pickle(test, processed_test_pkl)
save_as_pickle(train, processed_data_for_train_pkl)
