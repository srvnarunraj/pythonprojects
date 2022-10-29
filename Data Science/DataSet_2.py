import pandas as pds
import matplotlib.pyplot as mat
x=pds.read_csv("D:\Data Science\california_housing_train.csv")
mat.scatter(x['total_bedrooms'],x['total_rooms'])
mat.scatter(x['population'],x['households'],c=x["median_house_value"],s=x["median_income"])
mat.title("Oyo Rooms")
mat.xlabel("Motham BedRooms")
mat.ylabel("Motham Rooms")
mat.colorbar()
mat.show()
