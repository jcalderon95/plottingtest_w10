# let's try plottoing stuff with matplotlib

import matplotlib.pyplot as plt

years = [1900, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
pops = [1.2, 1.4, 1.8, 2.2, 2.6, 3.0, 3.5, 4.0]

plt.plot(years, pops, color=(255 / 255, 100 / 255, 100 / 255), linewidth=6.0)
plt.ylabel("Population by Billions")
plt.xlabel("Growth by Year")
plt.title("Global Population Growth", pad=20)

plt.show()

# pie charts!
labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.legend(labels, loc=1)
plt.show()