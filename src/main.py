import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./res/MentalHealthDataset.csv')
print(len(df))

print(df.columns)
# Pie Chart for Gender Distribution
gender_counts = df['Gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
plt.title('Data distribution by gender')
plt.show()

# Occupations with More Prevalent Mental Health Conditions
occupation_counts = df['Occupation'].value_counts().head(10)  # Top 10 occupations
sns.barplot(x=occupation_counts.values, y=occupation_counts.index)
plt.title('Top 10 Occupations with Mental Health Conditions')
# Customize further as needed
plt.show()

