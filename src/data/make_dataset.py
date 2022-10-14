# -*- coding: utf-8 -*-
import click
import logging
import os
import pandas as pd

from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from src.data.preprocess import preprocess, extract_target, preprocess_target
from src.config import *
from src.utils import save_as_pickle


@click.command()
@click.argument('output_target_filepath', type=click.Path())
def main(output_target_filepath=None):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    train = pd.read_csv(train_csv)
    test = pd.read_csv(test_csv)

    train = preprocess(train)
    test = preprocess(test)

    if output_target_filepath:
        train, target = extract_target(train)
        target = preprocess_target(target)
        save_as_pickle(target, target_data_train_pkl)

    save_as_pickle(train, interim_data_for_train_pkl)
    save_as_pickle(test, interim_test_pkl)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
