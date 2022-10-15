import yaml
import os

print(os.getcwd())

with open('params.yaml', encoding='utf-8') as conf_file:
    config = yaml.safe_load(conf_file)

# Data load
train_csv = config['data_load']['train_csv']
test_csv = config['data_load']['test_csv']

# Pre-process category
TARGET_COLS = config['preprocess_category']['TARGET_COLS']
ID_COL = config['preprocess_category']['ID_COL']
EDU_COL = config['preprocess_category']['EDU_COL']
SEX_COL = config['preprocess_category']['SEX_COL']
CAT_COLS = config['preprocess_category']['CAT_COLS']
OHE_COLS = config['preprocess_category']['OHE_COLS']
REAL_COLS = config['preprocess_category']['REAL_COLS']

# Data pre-process output
target_data_train_pkl = config['processed_paths']['target_data_train_pkl']
interim_data_for_train_pkl = config['interim_paths']['data_for_train_pkl']
interim_test_pkl = config['interim_paths']['test_pkl']

# Feature generation output
processed_test_pkl = config['processed_paths']['processed_test_pkl']
processed_data_for_train_pkl = config['processed_paths']['processed_data_for_train_pkl']

# Training
seed = config['base']['seed']
CATEGORIES_COL = config['train']['CATEGORIES_COL']
train_size = config['train']['train_size']
iterations = config['train']['iterations']
loss_function = config['train']['loss_function']
eval_metric = config['train']['eval_metric']
learning_rate = config['train']['learning_rate']
bootstrap_type = config['train']['bootstrap_type']
boost_from_average = config['train']['boost_from_average']
leaf_estimation_iterations = config['train']['leaf_estimation_iterations']
leaf_estimation_method = config['train']['leaf_estimation_method']

model_path = config['train']['model_path']
X_test_path = config['train']['X_test_path']
Y_test_path = config['train']['Y_test_path']

# Evaluate
score_metric = config['evaluate']['score_metric']
score_path = config['evaluate']['score_path']
