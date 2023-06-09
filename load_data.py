from logging import getLogger

import pandas as pd

from utils import log_inout

TRAIN_DATA = "data/anime.csv"
TEST_DATA = "data/test.csv"

logger = getLogger("Log").getChild(__name__)


@log_inout
def read_csv(path):
    df = pd.read_csv(path)
    return df


@log_inout
def load_train_data():
    df = read_csv(TRAIN_DATA)
    df = df.dropna(subset=['genre'])
    return df


@log_inout
def load_test_data():
    df = read_csv(TEST_DATA)
    return df


if __name__ == "__main__":
    print(load_train_data().head())
    print(load_test_data().head())
