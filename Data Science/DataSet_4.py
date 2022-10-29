import pandas as pds
import matplotlib.pyplot as mat
x=pds.read_csv("D:\Data Science\Marks Data.csv")
mat.hist(x['Roll'])
mat.hist(x['Total'])
mat.title("OS Marks")
mat.xlabel("Roll")
mat.ylabel("Total")
mat.show()