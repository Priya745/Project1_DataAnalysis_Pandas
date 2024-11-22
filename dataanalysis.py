import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data2.csv')

# display First few rows of the data
# print(df.head())

# describe statistical data of all numerical columns
# print(df.describe())

# find missing values in each column
# mv = df.isnull().sum()
# print("Missing values in each column:\n", mv)


# calculate the average of a column
# avg = df['Age'].mean()
# print(f"Average of age: {avg}")

# count the Unique values
# uv = df['Age'].nunique()
# print(f"Unique values in age: {uv}")

# filter rows based on a condition, eg - filter all employees from Engineering Department
# eng_emp = df[df['Department'] == 'Engineering']
# print(eng_emp)

# sal = df[df['Salary'] >= 50000]
# print(sal)

# Find the max, eg- get the employee with highest salary
# max_salary = df['Salary'].max()
# print(max_salary)
# max_salary_emp = df[df['Salary'] == max_salary]
# print("Highest paid employee: \n", max_salary_emp)

# min_salary = df['Salary'].min()
# min_salary_emp = df[df['Salary'] == min_salary]
# print("Highest paid employee: \n", min_salary_emp)

# count frequency of each values in a column eg- count how many employees are in each department
dep_count = df['Department'].value_counts()
print("Number of employees in each department: ", dep_count)

# sort data by column
# sort = df.sort_values(by='Age', ascending=False)         # different syntax
# print("Senior to Junior employee: \n", sort)

# add a new column based on condition, eg- add xperience based on age
# df['Experience'] = df['Age'].apply(lambda x: 'Senior' if x>=30 else 'Junior')
# print("Data with experience column: \n",df)

# DATA VISUALISATION

# Plot a pie chart
plt.figure(figsize=(8, 6))
plt.pie(dep_count, labels=dep_count.index, autopct='%1.1f%%', startangle=140)
plt.title("Department")
plt.show()
