import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# Filter data based on a condition (e.g., age greater than 30)
filtered_df = df[df['Age'] > 30]
print(filtered_df)
# Create a sample DataFrame with additional column
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
        'Age': [25, 30, 35, 40, 25, 30],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'New York', 'Chicago'],
        'Salary': [50000, 60000, 70000, 80000, 55000, 65000]}
df = pd.DataFrame(data)

# Group data by City and calculate mean salary for each city
grouped_df = df.groupby('City').mean()
print(grouped_df)
