import pandas as pd
import os

folder = os.path.dirname(os.path.abspath(__file__))

data = pd.read_csv(os.path.join(folder, "stu.csv"))

print(data)
print(data.head())
print(data.shape)
print(data.columns)
data["Average"] = (
    data["Math"] +
    data["Science"] +
    data["English"]
) / 3

print(data)
topper = data.loc[data["Average"].idxmax()]

print("Class Topper:")
print(topper)
class_average = data["Average"].mean()

print("Class Average:", round(class_average, 2))
marks = [80, 90, 70]

print(sum(marks) / len(marks))

import matplotlib.pyplot as plt

plt.bar(data["Student"], data["Average"])

plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance Analysis")

plt.show()
