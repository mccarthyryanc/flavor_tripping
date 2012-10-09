#!/usr/bin/env python
#
# Just a little plotting code for some data
#

import csv, random,matplotlib
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.mlab as mlab

filename = "flavor_tripping_poll.csv"

# Read in the data
data = {'person_id':[],'red_wine_vinegar':[],'balsamic_vinegar':[],'salt_and_vinegar_chips':[],'lime':[],'lemon':[],'grapefruit':[],'orange':[],'goat_cheese':[],'blue_cheese':[],'jalapeno':[],'hot sauce':[],'tomato':[],'guinness':[],'granny_smith_apples':[],'strawberries':[],'kiwi':[],'white_onion':[],'banana':[],'grape':[],'cider_vinegar':[],'ipa':[]}
with open( filename, "rb" ) as theFile:
    reader = csv.DictReader( theFile )
    [data[item].append(float(row[item])) for row in reader for item in row if "NA" not in row[item]]

#Make the plot
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
cm = matplotlib.cm.get_cmap('RdYlBu')

y_pos = 0.5
step = 1.0

x = []
y = []
z = []

for item in data:
    if "person_id" in item: continue
    
    ax.text(-0.1,y_pos,item.replace('_'," ").title(),horizontalalignment='right')
    plt.plot([-0.1,10.4],[y_pos+0.1,y_pos+0.1],c='k',linestyle='--',alpha=0.5)
    
    for point in data[item]:
        x.append(point)
        y.append(y_pos + random.random()/5.0)
        z.append(point)
    
    y_pos += step

sc = ax.scatter(x,y, s=70, c=z,alpha=0.7,cmap=cm)

# Add text
ax.text(1.0, y_pos, "BAD",horizontalalignment='center')
ax.text(5.0, y_pos, "NO CHANGE",horizontalalignment='center')
ax.text(10.4, y_pos, "GREAT",horizontalalignment='right')

#Draw box
plt.plot([0.0,10.4],[0.1,0.1],c='k')
plt.plot([0.0,10.4],[y_pos-0.2,y_pos-0.2],c='k')
plt.plot([0.0,0.0],[0.1,y_pos-0.2],c='k')
plt.plot([10.4,10.4],[0.1,y_pos-0.2],c='k')

ax.set_axis_off()
fig.savefig('figure.svg', bbox_inches='tight', pad_inches=0.01)
