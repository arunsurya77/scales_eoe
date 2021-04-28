import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-2.8985,2.8986,0.341)
y=np.arange(-2.8985,2.8986,0.341)

#plt.scatter(0,0,s=200)
for i in x:
	for j in y:
		plt.scatter(i,j,s=2)
		i_left=i-(0.341/2)
		j_left=j-(0.341/2)
		rectangle = plt.Rectangle((i_left,j_left), 0.341, 0.341, fc='blue',ec="red",alpha=.2)
		plt.gca().add_patch(rectangle)

offset=(27+55)*.341		

x=np.arange(-18.5845,18.5845,0.341)
y=np.arange(-18.5845,18.5845,0.341)
x_mesh,y_mesh=np.meshgrid(x+offset,y)


plt.scatter(x_mesh,y_mesh,s=2)
#for i in x:
#	for j in y:
#		plt.scatter(i,j)
#		i_left=i-(0.341/2)
#		j_left=j-(0.341/2)
		#rectangle = plt.Rectangle((i_left,j_left), 0.341, 0.341, fc='red',ec="red",alpha=.5)
		#plt.gca().add_patch(rectangle)


start_x=2.8985
dis=21
x=(np.arange(dis)+1)*0.341+start_x
y=np.ones(dis)*(0.341/2)
for i in x:
	for j in y:
		
		i_left=i-(0.341/2)
		j_left=j-(0.341/2)
		rectangle1 = plt.Rectangle((i_left,j_left), 0.341, 0.341, ec="red",alpha=0.2)
		plt.gca().add_patch(rectangle1)
        plt.scatter(i,j,s=2,c='red')
plt.title('Lenslet Geometry')
plt.xlabel('mm')
plt.ylabel('mm')		
plt.show()		
