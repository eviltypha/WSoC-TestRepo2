from functions import *
import matplotlib.pyplot as plt

data = open_pkl('../Level 2/Challenge 1/Data.pkl')

print(type(data))

sub = []
stud = []
for keys, values in data.items():
	#print(keys)
	sub.append(keys)
	#print(values)
	stud.append(values)
#print(sub, stud)

# Bar Graph
plt.figure(figsize = (10, 5))
plt.bar(sub, stud, width = 0.7)
for x,y in zip(sub,stud):

    label = "{:.0f}".format(y)

    plt.annotate(label, (x,y), textcoords="offset points",
                 xytext=(0,10),
                 ha='center')
plt.xlabel("Subjects")
plt.ylabel("No. of Passed Students(out of 50)")
plt.show()

# Pie Chart
plt.figure(figsize = (10, 5))
plt.pie(stud, labels = sub, autopct = '%.1f%%')
plt.show()