import pandas as pd

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

print("\n\nTrain dataset\n\n")
print(train.head())

print("\n\nTest dataset\n\n")
print(test.head())
