import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-2.8985,2.8986,(2*2.8985/17))*-1
x=np.arange(-10.77498,-16.57199,-.341)
y=np.arange(-2.7280,3.2,(2*2.7280/16))*-1

count=1
for x_val in x:
    x_arr=np.ones(len(y))*x_val
    y_arr=y
    fname_x=str(count)+'.0000_x.txt'
    fname_y=str(count)+'.0000_y.txt'
    np.savetxt(fname_x,x_arr)
    np.savetxt(fname_y,y_arr)
    count=count+1
    plt.scatter(x_arr,y_arr)
plt.show()  
