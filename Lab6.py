import matplotlib.pyplot as plt
import pandas as pd

# Загрузка данных из файла CSV
данные_зарплаты = pd.read_csv('Salary_Data.csv')

# Проверка первых строк данных
print("Первые строки данных:")
print(данные_зарплаты.head())

# Определение факторов (X) и целевой переменной (y)
X = данные_зарплаты.iloc[:, :-1].values
y = данные_зарплаты.iloc[:, -1].values

# Вывод первых 5 записей матрицы факторов и целевой переменной
print("Матрица факторов:")
print(X[:5])
print("Целевая переменная:")
print(y[:5])

# Разделение данных на обучающую и тестовую выборки
from sklearn.model_selection import train_test_split
X_обучающая, X_тестовая, y_обучающая, y_тестовая = train_test_split(X, y, test_size=0.25, random_state=0)

# Обучение модели линейной регрессии
from sklearn.linear_model import LinearRegression
регрессор = LinearRegression()
регрессор.fit(X_обучающая, y_обучающая)

# Прогнозирование значений на тестовой выборке
y_прогноз = регрессор.predict(X_тестовая)
print("Прогнозируемые значения:")
print(y_прогноз)

# Создание областей для графиков
fig, (график1, график2) = plt.subplots(1, 2, figsize=(12, 5))

# График для обучающей выборки
график1.scatter(X_обучающая, y_обучающая, color='red')
график1.plot(X_обучающая, регрессор.predict(X_обучающая), color='blue')
график1.set_title('Зарплата vs Опыт (Обучающая выборка)')
график1.set_xlabel('Опыт (лет)')
график1.set_ylabel('Зарплата')

# График для тестовой выборки
график2.scatter(X_тестовая, y_тестовая, color='red')
график2.plot(X_обучающая, регрессор.predict(X_обучающая), color='blue')
график2.set_title('Зарплата vs Опыт (Тестовая выборка)')
график2.set_xlabel('Опыт (лет)')
график2.set_ylabel('Зарплата')

# Отображение обоих графиков
plt.show()