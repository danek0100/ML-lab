import yaml
import os

print(os.getcwd())

with open('params.yaml', encoding='utf-8') as conf_file:
    config = yaml.safe_load(conf_file)

train_csv = config['data_load']['train_csv']
test_csv = config['data_load']['test_csv']
TARGET_COLS = config['preprocess_category']['TARGET_COLS']
ID_COL = config['preprocess_category']['ID_COL']
EDU_COL = config['preprocess_category']['EDU_COL']
SEX_COL = config['preprocess_category']['SEX_COL']
CAT_COLS = config['preprocess_category']['CAT_COLS']
OHE_COLS = config['preprocess_category']['OHE_COLS']
REAL_COLS = config['preprocess_category']['REAL_COLS']
target_data_train_pkl = config['preprocess_paths']['target_data_train_pkl']
data_for_train_pkl = config['preprocess_paths']['data_for_train_pkl']
test_pkl = config['preprocess_paths']['test_pkl']
