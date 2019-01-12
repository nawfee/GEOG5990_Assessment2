The program contains code to run a data analysis software . The source code are within a single file named, IcebergTowing_App in (.py) format. The relavant data for the data analysis are present as two text files named, white1.radar and white1.lidar. Whitin the folder is also a licence file. The documentation and comments for the code are written in the python file. The codes were witten in an object-oriented programminglanguage- i.e, python, version 3.7. Spyder IDE was used for code editing and viewing. The code development was done in Windows 10. The details of the code file is as follows:

###IcebergTowing_App.py: This file has to be open in python IDE, Spyder. It contains code that read in the lidar and radar data using csv code reader. They can be printed to show the pixel values, in 2D list format. These data has also been displayed using matplotlib.pyplot module.
The iceberg is located using the radar file data, setting a condition that on or over 100 pixel values represent iceberg. This data is then passed to the lidar data using the start and end index of rows and column.
The height of the iceberg in meter is calculated from the lidar pixel values of the iceberg. The volume of the iceberg is then calculated using the formula, volume = height x area. the area of each pixel is 1m2, as the area of the sea is 300m x300m. The sum of the elements in the iceberg volume list than gave the total volume of iceberg.
The total mass of the iceberg above water is calculated using, iceberg mass = volume x density, here density of ice is 900 kg/m3. 
Assuming only 10% of the iceberg is above water, the total volume of iceberg is calculated.
Then the towing ability of the iceberg is assessd by setting up the condition that, if the iceberg is equal or above 36 million kg it can't be drag out in time. 

------------------------------------------------------------------------------------------------------------------------------------------
### Running the application
To run the data analysis application, the IcebergTowing_App has to be open in Spyder. The 'Run' button has to be pressed to get the output in Ipython console.
Running the app once prints the following:
The start and end index of row and column of the radar data, to locate the iceberg.
The images of radar and lidar data are displayed as matplotlib subplots. The iceberg and sea water is identified in it.
The results of calculation, the total iceberg volume and mass is also printed out in the IPython console. And most importantly the result of iceberg towing ability is printed out. 

-----------------------------------------------------------------------------------------------------------------------------------------
### Warnings: The IcebergTowing_App.py file, the white1.radar.txt file and the white1.lidar.txt file should be present in the same directory. Hereall the files have to be opened from the folder named: GEOG5990M_[201277909]_Assessment2 folder. 
Otherwise the code will not run

----------------------------------------------------------------------------------------------------------------------------------------
### Licence
The model code has been licenced using : MIT License

Copyright (c) 2019 Nawfee. A text file, detailing the licence terms and conditions has been attached in the application folder.
