#!/home/ml1/projectt/env1/bin/python

from catboost.datasets import titanic

train, test = titanic()

train.to_csv("../../data/raw/train.csv", index=False)

test.to_csv("../../data/raw/test.csv", index=False)
