import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Using loc to modify a specific element
df.loc[0, 'A'] = 10  # Set the value of the 'A' column in the first row to 10
