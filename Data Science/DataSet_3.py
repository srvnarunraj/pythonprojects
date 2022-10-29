import pandas as pds
import matplotlib.pyplot as mat
x=pds.read_csv("D:\Data Science\Marks Data.csv")
# Bar Diagram
# mat.bar(x["Roll"],x["Total"])
mat.title("OS Marks")
mat.xlabel("Roll")
mat.ylabel("Total")
mat.show()
#pie Chart
# mat.pie(x["Total"],labels=x["Roll"])
# mat.show()


#Bar Graph : mat.bar
#Pie Chart : mar.pie
#Scatter