import pandas as pd
from yaml import safe_load

with open('invoice.yaml', 'r') as f:
    df = pd.json_normalize(safe_load(f))

print(df.head())