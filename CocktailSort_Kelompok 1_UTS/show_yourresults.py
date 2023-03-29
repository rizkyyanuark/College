import pandas
from skimage import color
import matplotlib.pylab as plt
df = pandas.read_csv('PikachuCocktail.csv')
df.drop(columns=['indeks'])
plt.imshow(df, cmap=plt.cm.orange, vmin=0, vmax=1)
plt.show()
