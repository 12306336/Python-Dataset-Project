import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

#  Load dataset with encoding fix
df_fatalities = pd.read_csv("C:\\Users\\sonuk\\OneDrive\\Documents\\Desktop\\Deaths_by_Police_US.csv", encoding='ISO-8859-1')

print("\n Dataset Overview:")
print(df_fatalities)

print("\n Head of the dataset:")
print(df_fatalities.head())

print("\n Tail of the dataset:")
print(df_fatalities.tail())
 
print("\n Summary Statistics:")
print(df_fatalities.describe())

print("\n Information:")
print(df_fatalities.info())

print("\n Column Names:")
print(df_fatalities.columns)

print("\n Shape of Dataset:")
print(df_fatalities.shape)

# -------------------------
# Objective 1: Deaths by Gender
# -------------------------
gender_counts = df_fatalities['gender'].value_counts()
plt.figure(figsize=(6, 4))
sns.barplot(x=gender_counts.index, y=gender_counts.values, hue=gender_counts.index, palette='Set2', legend=False)
plt.title('Total Number of Deaths by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Deaths')
plt.tight_layout()
plt.savefig('gender_deaths.png')
plt.show()

# -------------------------
# Objective 2: Age vs Manner of Death by Gender
# -------------------------
plt.figure(figsize=(10, 6))
sns.boxplot(x='manner_of_death', y='age', hue='gender', data=df_fatalities)
plt.title('Age Distribution by Manner of Death and Gender')
plt.xlabel('Manner of Death')
plt.ylabel('Age')
plt.tight_layout()
plt.savefig('age_manner_gender_boxplot.png')
plt.show()

# -------------------------
# Objective 3: Age Summary
# -------------------------
print("===== Age Summary Statistics =====")
print(df_fatalities['age'].describe())

print("\nTop 10 Most Common Ages:")
print(df_fatalities['age'].value_counts().head(10))

top_ages = df_fatalities['age'].value_counts().head(10).reset_index()
top_ages.columns = ['age', 'count']
plt.figure(figsize=(8, 4))
sns.barplot(x='age', y='count', hue='age', data=top_ages, palette='coolwarm', legend=False)
plt.title('Top 10 Most Common Ages of People Killed')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('age_summary.png')
plt.show()

# -------------------------
# Objective 4: Histogram + KDE of Age
# -------------------------
plt.figure(figsize=(10, 6))
sns.histplot(df_fatalities['age'].dropna(), kde=True, bins=30, color='skyblue')
plt.title('Age Distribution (Histogram + KDE)')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('age_distribution.png')
plt.show()

# -------------------------
# Objective 5: Race of People Killed
# -------------------------
race_counts = df_fatalities['race'].value_counts().reset_index()
race_counts.columns = ['race', 'count']
plt.figure(figsize=(8, 5))
sns.barplot(x='race', y='count', hue='race', data=race_counts, palette='muted', legend=False)
plt.title('Total Number of People Killed by Race')
plt.xlabel('Race')
plt.ylabel('Number of Deaths')
plt.tight_layout()
plt.savefig('race_deaths.png')
plt.show()
