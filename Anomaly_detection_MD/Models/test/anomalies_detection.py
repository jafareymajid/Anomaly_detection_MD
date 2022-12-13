from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import numpy as np
from analysis import *

"""
This script is used to detect anomalies in the RMSD values of a trajectory by using IsolationForest. 
The script takes a file containing the RMSD values of the trajectory and plots the data with the detected anomalies.
"""

path4= path3 + '/' + 'rmsd.txt'
if os.path.isfile(path4):
    shutil.copy(path4, path)
    print(f"The RMSD file is being copied to the {path} directory!")
else:
    print(f"rmsd.txt: No such file or directory!")
time.sleep(3)

# read the data file
f = open('rmsd.txt', 'r')
lines = f.readlines()
f.close()
# remove column title
title='#Frame'
title2='ToFirst'
lines[0] = lines[0].replace(title, '')
lines[0] = lines[0].replace(title2, '')
# re-write file
f = open('rmsd_new.txt', 'w')
f.writelines(lines)
f.close()

#Create an Isolation Forest object
clf = IsolationForest(random_state=0)
data = np.loadtxt("rmsd_new.txt")
#Fit the IsolationForest model to the data 
clf.fit(data)
#Predict the labels for the data using the model
labels = clf.predict(data)
# identifies the anomalies by looping through the labels array and finding the indices of the elements that are given -1 by the model
anomalies = [i for i, x in enumerate(labels) if x == -1]
#Find the index of the maximum value in the second column
max_index = np.argmax(data[anomalies,1])
min_index = np.argmin(data[anomalies,1])
#Plot the data
#Create a figure with two panels
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14,5))
#Plot the data in the first panel
ax1.plot(data[:,0], data[:,1], c='blue')
ax1.set_title('Original data')
ax1.set_xlabel('Steps')
ax1.set_ylabel('RMSD(Angstrom)')
#Plot the anomalies in the second panel
ax2.scatter(data[:,0], data[:,1], c=labels, cmap='rainbow')
#Plot the anomalies
ax2.scatter(data[anomalies,0], data[anomalies,1], c='black', s=100, marker='x')
#Highlight the worst anomaly
ax2.scatter(data[anomalies[max_index],0], data[anomalies[max_index],1], c='green', s=200, marker='x')
ax2.scatter(data[anomalies[min_index],0], data[anomalies[min_index],1], c='green', s=200, marker='x')
ax2.set_title('Data with anomalies')
ax2.set_xlabel('Steps')
ax2.set_ylabel('RMSD(Angstrom)')
#Save the figure
plt.savefig('detected_anomalies.tif', dpi=300)
#Show the figure
#plt.show()

#saving the anomaly points in a file
#Calculate the percentage of anomalies
percentage = len(anomalies) / len(data) * 100
#Write the percentage to the file
with open('detected_anomalies.txt', 'w') as f:
    #f.write('Anomalies percentage: ' + str(percentage) + '%\n')
    f.write('Time RMSD\n')
    for i in anomalies:
        f.write(str(data[i,0]) + ' ' + str(data[i,1]) + '\n')   
#the percentage of the anomalies in the data
print('The percentage of anomalies in the data is: %.2f%%' % percentage)

with open('detected_anomalies.txt', 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write('Anomaly Percentage: ' + str(len(anomalies)/len(data)*100) + '%\n' + content)
    