import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("D:\PyCharm Community Edition 2024.2\mainconfigjob\datasets\DataScience_salaries_2024.csv")

print(df.head()) # просмотр первых строк данных
print(df.info()) # основная информация

print(df.describe())

print(df.isnull().sum())# проверка на пропущенные значения
df_cleaned = df.dropna()# удаление строк с пропущенными значениями

print(df_cleaned.isnull().sum())# проверка на пропущенные значения
print(df_cleaned.duplicated().sum()) # дубликаты
df_cleaned = df_cleaned.drop_duplicates() # удаление дубликатов
print(df_cleaned.duplicated().sum()) # проверка дубликатов после удаления

salary_by_year = df_cleaned.groupby('work_year')['salary_in_usd'].mean()# cредняя зарплата в USD по годам

plt.figure(figsize=(10, 5))
plt.plot(salary_by_year.index, salary_by_year.values, marker='o')
plt.title('Средняя зарплата в USD по годам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата (USD)')
plt.grid(True)
plt.show()

# распределение зарплат в USD
plt.figure(figsize=(10, 5), edgecolor='black')
plt.hist(df_cleaned['salary_in_usd'], bins=30, edgecolor='red')
plt.title('Распределение зарплат в USD')
plt.xlabel('Зарплата (USD)')
plt.ylabel('Частота') # количество людей с такой зарплатой
plt.grid(True)
plt.show()

