import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan], 'C':[1,2,3]}
df = pd.DataFrame(d)

print(df)

# Drops rows or columns with null or missing values
# Rows are at axis 0, columns are at axis 1
df.dropna()

# Can set threshold for non na values
# At least 2 non NA values
df.dropna(thresh=2)

#Fills NaN with something
df.fillna(value='FILL VAL')
df['A'].fillna(value=df['A'].mean())