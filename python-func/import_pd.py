import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(iris.head(3))

print(iris.shape)
print("===================================================================")
iris['rounded_sepal_length'] = iris[['sepal_length']].apply(pd.Series.round)
print(iris.head())
print(iris.shape)
print("===================================================================")

def multiply_by_100(x):

    res = x * 100
    print(f"This was passed in:=> {x}, and this result was generated:=> {res}")
    return res

iris['100x_sepal_length'] = iris[['sepal_length']].apply(multiply_by_100)
print(iris.head())