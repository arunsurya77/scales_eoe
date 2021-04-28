import numpy as np
import matplotlib.pyplot as plt
import re
from shapely.geometry.polygon import LinearRing, Polygon
from descartes import PolygonPatch
import math
import matplotlib.cm as cm
import matplotlib.patches as patches

col_cont=[]
col_arr=['red','green','blue','yellow','purple','orange']
for i in range(6):
    for j in range(51):
	col_cont.append(col_arr[i])
col_cont=np.array(col_cont)	



from random import randint
colors = []

for i in range(18):
    colors.append('#%06X' % randint(0, 0xFFFFFF))
xx=[]
yy=[]
arr=[]
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.set_xlim([-1248,1248])
ax.set_ylim([-1248,1248])
count_in=0
count_out=0
cnt=0

def ismissing(x,y):
    if np.logical_and(np.logical_and(x<1024,x>-1024),np.logical_and(y<1024,y>-1024)):
        return 0
    else:
        return 1

#wave_samp=np.arange(1.9600,2.0604,.002)
wave_samp=np.array([2.000,2.2000,2.4000])
wave_samp=np.array([4.5000,5.2000])
wave_samp=np.arange(4.5000,5.2000,0.1750) #M
wave_samp=np.arange(1.95,2.451,0.1250) #K
#wave_samp=np.arange(2.9000,4.15,0.3125) #L
#wave_samp=np.arange(2.0,2.41,0.1) #deno
xlis=[]
ylis=[]
xlis_field=[]
ylis_field=[]


miss_arr=np.zeros([18,18])
missing=0
for j in wave_samp:
        arr_x=[]
        arr_y=[]
        arr_x_field=[]
        arr_y_field=[]
        slice_color=[]
        for i in range(1,19,1): #
            for k in range(1,18,1): #19 for full field 6 for half
                    arr=[]
                    wave='{:01.4f}'.format(j)

                    filename= 'slenslet/K_pdr/ls_'+str(i)+'.0000'+'_'+str(k)+'.0000'+'_'+wave+'.dat'
                    print filename
                    with open(filename) as f:
                            for line in f:
                                    result=line.split()
                                    if len(result)>2:
                                            if ((result[0]=='Image') & (result[1]=='coordinate')):
                                                    xx.append(np.float(result[3]))
                                                    yy.append(np.float(result[4]))
                                                    cnt=cnt+1
                                                    plt.scatter(np.float(result[3])*1000/18,np.float(result[4])*1000/18,c=colors[i-1])
                                                    #plt.text(np.float(result[3])*1000/18, np.float(result[4])*1000/18, '('+str(i)+' '+str(k)+')', fontsize=10)
#                                                    arr_x.append(np.float(result[3])*1000/18)
#                                                    arr_y.append(np.float(result[4])*1000/18)

                                                    #arr_x.append(np.float(result[3])*1000/18)
                                                    #arr_y.append(np.float(result[4])*1000/18)
                                                    
                                                    arr_x.append(np.float(result[3])*1000/18)
                                                    arr_y.append(np.float(result[4])*1000/18)                                                    

                                                    flag=ismissing(np.float(result[3])*1000/18,np.float(result[4])*1000/18)
                                                    if flag==1:
                                                        miss_arr[k-1,i-1]=1
                                                    arr.append(((np.float(result[3])*1000/15),(np.float(result[4])*1000/15)))
                                            if ((result[0]=='Field') & (result[1]=='coordinate')):
                                                    arr_x_field.append(np.float(result[3]))
                                                    arr_y_field.append(np.float(result[4]))
                                                    #plt.scatter(np.float(result[3]),np.float(result[4]),c=colors[i-1])
                                                    #plt.show()
                                                    #plt.pause(.1)
                                                    slice_color.append((colors[i-1]))
        arr_x=np.array(arr_x)
        arr_y=np.array(arr_y)
        #plt.plot(arr_x,arr_y)
        xlis.append(arr_x)
        ylis.append(arr_y)

        arr_x_field=np.array(arr_x_field)
        arr_y_field=np.array(arr_y_field)
        #plt.plot(arr_x,arr_y)
        xlis_field.append(arr_x_field)
        ylis_field.append(arr_y_field)

xlis=np.array(xlis)
ylis=np.array(ylis)
xlis_field=np.array(xlis_field)
ylis_field=np.array(ylis_field)

sort_len=[]
ind=np.load('ind.npy')
#dist=np.load('dist.npy')
dist_arr=[]

for k in range(5):
    x=xlis[k,ind]
    dist1=(abs((x[:-1]-np.roll(x,-1)[:-1])))
    dist2=(abs((x[:-1]-np.roll(x,1)[:-1])))
    
    dist1=(abs((x-np.roll(x,-1))))
    dist2=(abs((x-np.roll(x,1))))
    
    dist=[]
    for i in range(len(dist1)):
	dist.append(np.min([dist1[i],dist2[i]]))
    dist=np.array(dist)
    dist_arr.append(dist)
dist_arr=np.array(dist_arr)
dist=dist_arr.mean(axis=0)
min, max = (dist.min(), dist.max())


for k in range(5):
	x=xlis[k,ind]
	y=ylis[k,ind]
	#x=x[:-1]
	#y=y[:-1]
	slice_color=np.array(slice_color)
	colors=slice_color[ind]
	#plt.scatter(x,y,dist,c=colors)
	plt.scatter(x,y,c=slice_color)
	for i in range(x.shape[0]):
		plt.text(x[i],y[i],str(int(dist_arr[k,i])),fontsize=10)

plt.show()



for it in range(xlis.shape[1]):
    i=ind[it]
    #r = (float(dist[it])-min)/(max-min)
    #g = 0
    #b = 1-r
    sort_len.append((xlis[0,i]+2000)**2)#+(ylis[0,i])**2)
    #plt.scatter(xlis[:,i],ylis[:,i])
    plt.plot(xlis[:,i],ylis[:,i],c=slice_color[i])
    #plt.pause(.1)
plt.plot([-1024,-1024],[-1024,1024],c='r',linewidth=4)
plt.plot([1024,1024],[-1024,1024],c='r',linewidth=4)
plt.plot([-1024,1024],[-1024,-1024],c='r',linewidth=4)
plt.plot([-1024,1024],[1024,1024],c='r',linewidth=4)
plt.title('SCALES slenslet K grating')
#plt.xlabel('pixels')
plt.ylabel( 'Dispersion Direction '+ "{:.4f}".format(wave_samp[-1]) +' <--- '+ "{:.4f}".format(wave_samp[0]))
plt.show()



    

plt.figure()
x=arr_x_field[ind]
y=arr_y_field[ind]

x=xlis[0,ind]
y=ylis[0,ind]
x=x[:-1]
y=y[:-1]
slice_color=np.array(slice_color)
colors=slice_color[ind]
plt.scatter(x,y,dist,c=colors)
#plt.scatter(x,y,c=slice_color)
for i in range(x.shape[0]):
    plt.text(x[i],y[i],str(int(dist[i])),fontsize=10)
plt.show()
plt.title('Distance between Spectra')
plt.xlabel('pixels')
plt.ylabel('pixels')

plt.figure()
x=arr_x_field[ind]
y=arr_y_field[ind]

slice_color=np.array(slice_color)
colors=slice_color[ind]
#plt.scatter(x,y,dist**2,c=col_cont)
plt.scatter(x,y,dist**2.3,c=colors)
for i in range(x.shape[0]):
    plt.text(x[i],y[i],str(int(dist[i])),fontsize=10)
plt.show()
plt.title('Distance between Spectra')
plt.xlabel('mm')
plt.ylabel('mm')

plt.figure()
plt.imshow(np.fliplr(miss_arr[:-1,:]))
plt.title('Lenslets with spectra falling out')
plt.show()

table=np.array([xlis_field[0,:],ylis_field[0,:],xlis[0,:],ylis[0,:],xlis[1,:],ylis[1,:],xlis[2,:],ylis[2,:],xlis[3,:],ylis[3,:],xlis[4,:],ylis[4,:]])
#np.savetxt('L_band_trace.csv',np.transpose(table),fmt='%1.4f')

# ind=range(xlis.shape[1])
# X=sort_len
# Y=ind
# Z = [x for _,x in sorted(zip(X,Y))]
# ind=Z
# np.save('ind.npy',ind)
