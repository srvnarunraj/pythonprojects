import pandas as pds
import seaborn as sb
import matplotlib.pyplot as mat

k = pds.read_csv("D:\Data Science\Marks Data.csv")
# lineplot
sb.lineplot(x=k["Roll"], y=k["Total"])
# Barplot
# sb.barplot(x=k["Roll"],y=k["Total"])
# Scatter plot
sb.scatterplot(x=k["Roll"], y=k["Total"])
mat.title("OS Marks")
mat.xlabel("Roll")
mat.ylabel("Total")
mat.show()
