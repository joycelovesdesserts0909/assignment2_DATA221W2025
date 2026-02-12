import pandas as pd
import numpy as np
# Load the dataset
df_crime = pd.read_csv("crime.csv")
# Create a new column 'risk' based on crime level
df_crime['risk'] = np.where(df_crime['ViolentCrimesPerPop'] >= 0.50, 'HighCrime', 'LowCrime')
# Group by risk and calculate average unemployment rate
avg_unemployment = df_crime.groupby("risk")["PctUnemployed"].mean()
# Print results
print(f"High-Crime areas average unemployment: {avg_unemployment['HighCrime']:.2f}")
print(f"Low-Crime areas average unemployment: {avg_unemployment['LowCrime']:.2f}")