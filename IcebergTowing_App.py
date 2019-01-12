# -*- coding: utf-8 -*-
"""
Application to find icebergs and their towing ability
Author: Shahreen Muntaha Nawfee
Created on Wed Jan  9 00:01:25 2019
"""


""" Modules imported for the application"""
import csv # to read radar and lidar data
import matplotlib.pyplot as plt #to display radar and lidar data
import numpy as np #to convert list to array


"""Extract Radar data
Rdar data is saved from an html as a text file. It is then extracted using csv
reader code and the data is inserted into an empty list, which represents the 
pixel values as 2D array
"""
sea = [] #create an empty list for creating sea environment    
#extract values from radar file using csv reader code
with open ('white1.radar.txt') as rdr:
    radar = csv.reader(rdr, quoting=csv.QUOTE_NONNUMERIC)#convert values to float
    for row in radar:
        rowlist = []
        for value in row:
            rowlist.append(value)
        sea.append(rowlist) #creates a 2D list with radar pixel values
#print(sea)


""" Finding icebergs
Each iceberg is located based on their starting and ending row and column indexes
A value of 100 or above is assigned to be iceberg. To prevent edge effects the
indexes start from 1 and stops at 1 value before th length of the area
"""
# extract each iceberg
iceberg= []

icebergStartCol = []
icebergEndCol = []
icebergStartRow = []
icebergEndCol = []

value0 = 0.0
onBergLeft = False
onBergRight = False
onBergAbove = False
onBergBelow = False
onBerg = False


for rowindex in range(1, len(sea) - 1): #index value for rows within range 1 to 299
    rowabove = sea[rowindex - 1] #rows above iceberg
    row = sea[rowindex]
    rowbelow = sea[rowindex + 1] #rows below iceberg
    for colindex in range(1, len(row) - 1): #index value for column
        value = row[colindex - 1]
        if (100 <= value <= 256):
            onBergLeft = True  
        else:
            onBergLeft = False      
        #Right
        value = row[colindex + 1]
        if (100 <= value <= 256):
            onBergRight = True
        else:
            onBergRight = False
        #Above
        value = rowabove[colindex]
        if (100 <= value <= 256):
            onBergAbove = True
        else:
            onBergAbove = False
        #Below
        value = rowbelow[colindex]
        if (100 <= value <= 256):
            onBergBelow = True
        else:
            onBergBelow = False
        #Cell
        value = row[colindex]
        if (100 <= value <= 256):
            onBerg = True
        else:
            onBerg = False
        if (onBerg):
            if (onBergRight == False):
                icebergendcolindex = colindex
            if (onBergLeft == False):
                icebergstartcolindex = colindex
            if (onBergAbove == False):
                icebergstartrowindex = rowindex
            if (onBergBelow == False):
                icebergendrowindex = rowindex

#prints the value of range of iceberg index        
print("icebergstartrowindex ", icebergstartrowindex)                
print("icebergstartcolindex", icebergstartcolindex)                
print("icebergendrowindex", icebergendrowindex)                
print("icebergendcolindex", icebergendcolindex)


"""Extract lidar data using csv reader code
Lidar data is also stored as text file from an html source. It is extracted as a
2D list ino a file named: lidar_sea
"""
with open('white1.lidar.txt') as ldr:
    lidar = csv.reader(ldr, quoting=csv.QUOTE_NONNUMERIC)
    lidar_sea = []
    for row in lidar:
        list_row = []
        for value in row:
            list_row.append(value)
        lidar_sea.append(list_row)
#print(lidar_sea)


""" Display the radar and lidar data as images
The radar and lidar data imported above are displayed using matplotlib.pyplot
module. They are displayed as images and icebergs are marked in them
"""        
#plot an image of sea with iceberg using radar data
plt.subplot(1,2,1) #making 1X2 subplot
plt.ylim(0,300) #set the y axis in plot
plt.xlim(0,300)#set the x axis in plot
plt.text(200,220, 'Sea',fontsize=12)
#annotate for showing the iceberg with an arrow
plt.annotate("Iceberg", xy=(155,145), xytext=(180,100), arrowprops=dict(facecolor="red" ))
plt.title('Radar image of a sea with iceberg',fontsize=12,fontname='Times New Roman')
plt.imshow(sea, 'Blues_r')#display an image of sea using blue and white colour

#plot an image of a sea with iceberg using lidar data
plt.subplot(1,2,2)
plt.ylim(0,300) #set the y axis in plot
plt.xlim(0,300)#set the x axis in plot
plt.text(200,220, 'Sea',fontsize=12)
plt.annotate("Iceberg", xy=(155,145), xytext=(180,100), arrowprops=dict(facecolor="red" ))
plt.title('Lidar image of a sea with iceberg',fontsize=12,fontname='Times New Roman')
plt.imshow(lidar_sea, 'Blues_r')#display an image of sea using blue and white colour

plt.tight_layout()
plt.show()


"""Pulling out the height of iceberg from lidar data
By using pixel indexes from radar data, the height values of the iceberg is pulled
out of the lidar data for future calculation
"""   
#convert the lidar data to 2D array
np_lidar_sea = np.array(lidar_sea,dtype=int)
#print(np_lidar_sea)

#mask iceberg from the np_array
iceberg = np_lidar_sea[icebergstartrowindex:icebergendrowindex+1, icebergstartcolindex:icebergendcolindex+1]
#iceberg = np_lidar_sea[135:166, 135:166]
#print(iceberg) #show only the pixel values of the iceberg

    
""" The volume of iceberg calculation from lidar pixel values
1 unit of lidar data represents 10 cm of height of iceberg. 10 units of lidar value, 
represents 1m in height. So the pixel values are multiplied
by 0.1, to get height in meter. The area of iceberg is 1m2, as each pixel has 
length and breadth of 1 meter.The volume is calculated from area multiplied
by height. The total volume of iceberg is obtained from adding up individual 
element from the iceberg volume list
"""  
    
iceberg_vol_m3 = [] #list of iceberg volume in m3
for i in iceberg:
    rowlist = []
    for j in i:
        rowlist.append(j*0.1*1) #calculate volume by using volume = heightXarea
    iceberg_vol_m3.append(rowlist)
    
    
    total_iceberg_vol = 0.0 
    for row in iceberg_vol_m3:
        for element in row:
            total_iceberg_vol += element
            
print("Total iceberg volume:", total_iceberg_vol,"m3") 
        

"""Calculation of  iceberg mass above sea level
For mass calculation the equation used is mass = density * volume
The density of iceberg is 900kg/m3
"""

iceberg_mass = total_iceberg_vol*900 #iceberg_mass_above water


"""Total iceberg mass calculation 
Assuming only 10% of the ice is above sea level, the total iceber mass is assessed
fromt he iceberg mass
"""

total_iceberg_mass = iceberg_mass * 10 #considering 10% mass above water
print("Total iceberg mass:", total_iceberg_mass,"kg")


""" Assessing iceberg towing ability
Iceberg can be drag out in time if its mass is below 36million kg
""" 
Towing_ability = True   
if total_iceberg_mass >= 36000000:
    print("Dragging iceberg is not possible")
else:
    print("Dragging iceberg is possible") 
    