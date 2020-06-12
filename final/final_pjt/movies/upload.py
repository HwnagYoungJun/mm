import os
import pandas as pd
dataset = []
print(1)
for dirname, _, filenames in os.walk('/Users/Do/Desktop/Pro/dataset'):
    for filename in filenames:
        url = os.path.join(dirname, filename)
        data = pd.read_csv(url)
        dataset.append(data)

credits = dataset[0]
keywords = dataset[1]
links = dataset[2]
links_small = dataset[3]
meta = dataset[4]
ratings = dataset[5]
ratings_small = dataset[6]

print(meta.columns)