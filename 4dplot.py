#We need to find the roots of f(F) = F^2 which happens only when 
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from mpl_toolkits.mplot3d.axes3d import get_test_data
import numpy as np
fig, ax = plt.subplots(figsize = [16,12],subplot_kw={'projection': '3d'})
X,Y,T = get_test_data(0.05)
#T means nothing it just returns tuple of 3 elememts
#f(x,y) = x+iy = F
#f(z,c) = z+ic = F**2
# z =  X**2 - Y**2
# c = 2*X*Y
def z(X,Y):
  return (X**2 - Y**2) 
Z = z(X,Y)
def c(X,Y):
  return (2*X*Y)
C = c(X,Y)

scamap = plt.cm.ScalarMappable(cmap='jet')
fcolors = scamap.to_rgba(C)
ax.plot_surface(X, Y, Z, facecolors=fcolors, cmap='jet',alpha = 0.6)
ax.plot_surface(X, Y, Z*0,alpha = 1)
fig.colorbar(scamap)
ax.set_xlabel('X',fontsize=16)
ax.set_ylabel('Y',fontsize=16)
ax.set_zlabel('Z',fontsize=16)
plt.show()
