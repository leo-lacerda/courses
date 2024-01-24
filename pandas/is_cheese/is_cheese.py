import pandas as pd
import numpy as np

df_product = pd.read_csv("data/produto.csv")
df_product.head()

df_product['descItem'].unique()

# Using apply:
def is_cheese(item):
  return item.lower().startswith('queijo')


filter_is_cheese = df_product['descItem'].apply(is_cheese)
df_product[filter_is_cheese]

# Lambda Functions
df_product['descItem'].apply(lambda x: x.lower().startswith('queijo'))

# Using str methods:
df_product['descItem'].str.lower().str.startswith('queijo')
