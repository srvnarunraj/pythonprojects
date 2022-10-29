import pandas as pds
import seaborn as sb
import matplotlib.pyplot as mat
k=pds.read_csv("D:\Data Science\Marks Data.csv")
sb.barplot(x=k["Roll"],y=k["Total"])
mat.title("OS Marks")
mat.xlabel("Roll")
mat.ylabel("Total")
mat.show()