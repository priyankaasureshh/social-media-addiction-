#importing all the essential tools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import warnings
import plotly.express as px
import pandas as pd
# Load dataset
df = pd.read_csv("Data/Students Social Media Addiction.csv")
print("🔍 DATA CLEANLINESS REPORT")
print("="*25)
print("___________________________________")
# 1. Shape
print("\n1️⃣ Dataset Shape (Rows, Columns):")
print(df.shape)
print("_____________________________________")
# 2. Column info & datatypes
print("\n2️⃣Column Info & Data Types:")
print(df.info())
print("________________________________")
# 3. Missing values
print("\n3️⃣ Missing Values Check:")
missing = df.isnull().sum()
print(missing[missing > 0] if missing.sum() > 0 else "No missing values ✅")
print("__________________________________")
# 4. Duplicate rows
print("\n4️⃣ Duplicate Rows Check:")
duplicates = df.duplicated().sum()
print(f"Duplicate rows found: {duplicates}" if duplicates > 0 else "No duplicates ✅")
print("______________________________________")
# 5. Inconsistent categorical values
print("\n5️⃣ Categorical Column Check:")
categorical_cols = ['Most_Used_Platform', 'Relationship_Status', 'Academic_Level', 'Country']
for col in categorical_cols:
    if col in df.columns:
        print(f"{col}: {df[col].unique()}")
        print("_____________________________________________")
 # 6. Invalid numeric values
print("\n6️⃣ Invalid Numeric Values Check:")
if 'Age' in df.columns:
    print("Invalid Age values:")
    print(df[(df['Age'] < 10) | (df['Age'] > 100)][['Student_ID', 'Age']])
if 'Sleep_Hours_Per_Night' in df.columns:
    print("\nInvalid Sleep Hours:")
    print(df[(df['Sleep_Hours_Per_Night'] < 0) | (df['Sleep_Hours_Per_Night'] > 24)]
          [['Student_ID', 'Sleep_Hours_Per_Night']])
    print("_____________________________________________________")
    # 7. Logical consistency check
print("\n7️⃣ Logical Consistency Check:")
if all(col in df.columns for col in ['Avg_Daily_Usage_Hours', 'Sleep_Hours_Per_Night']):
    inconsistent = df[
        (df['Avg_Daily_Usage_Hours'] > 10) &
        (df['Sleep_Hours_Per_Night'] > 9)
    ]
    print(inconsistent[['Student_ID', 'Avg_Daily_Usage_Hours', 'Sleep_Hours_Per_Night']]
          if not inconsistent.empty else "No logical inconsistencies ✅")
print("\n✅ Data quality check completed.")
print("________________________________________________________________")
import pandas as pd
df = pd.read_csv("Data/Students Social Media Addiction.csv")
print(df.head(3))
print("_________________________________________________________________")
# To describe the Dataset
print(df.describe())
print("________________________________________________________________")
# To count total count of each academic level
print("\n df['Academic_Level'].value_counts()")
print("_______________________________________________________________")
# to show the count of most used platform in a bar chart
import matplotlib.pyplot as plt
df['Most_Used_Platform'].value_counts().plot(kind='bar', color='grey')
plt.title('Count by Most Used Platform')
plt.xlabel('Platform')
plt.ylabel('Number of Students')
plt.show()
print("______________________________________________________________")
 #Classifying the Age into different groups using IF condition
def age_group(age):
    if age < 20:
        return 'Teen'
    elif age <= 25:
        return 'Young Adult'
    else:
        return 'Adult'

df['Age_Group'] = df['Age'].apply(age_group)
print(df[['Student_ID', 'Age', 'Age_Group']])
print("____________________________________________________________________")
#Representing Each Academic Levels using a Pie Chart
df['Academic_Level'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Academic Levels')
plt.ylabel('')
plt.show()
print("______________________________________________________________________")
#Students aged 18–25 using more than 5 hours daily
for _, row in df.iterrows():
    if 18 <= row['Age'] <= 25 and row['Avg_Daily_Usage_Hours'] > 5:
        print(f"Student {row['Student_ID']} heavy user ({row['Avg_Daily_Usage_Hours']} hrs)")
        print("______________________________________________________________")
  # To Analyze how relationship status and age relate to the most used social media app.
rel_app_count = (
    df.groupby(['Relationship_Status', 'Most_Used_Platform'])
      .size()
      .reset_index(name='Total_Users')
)
print("______________________________________________________")
print(rel_app_count)
#App-wise count for Three countries
selected_countries = ['India', 'USA', 'UK']

filtered_df = df[df['Country'].isin(selected_countries)]

app_country_pivot = filtered_df.pivot_table(
    index='Most_Used_Platform',
    columns='Country',
    aggfunc='size',
    fill_value=0
)

print(app_country_pivot)