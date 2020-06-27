import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import os
mytree=ET.parse('Annotations/2007_000272.xml')
root=mytree.getroot()

df=pd.DataFrame(index=range(0,17125),data=np.zeros((17125,21)),columns=['filename','aeroplane','bicycle','bird','boat','bottle','bus','car','cat','chair','cow','diningtable','dog','horse','motorbike','person','pottedplant','sheep','sofa','train','tvmonitor'],dtype=np.int32)
files=os.listdir('Annotations/')

print(len(files),'files detected')

for i,file in enumerate(files):
    if(i%500==0):
        print(f'working on {i} file')
    mytree=ET.parse('Annotations/'+file)
    root=mytree.getroot()
    for x in root:
        if(x.tag=='object'):
            df[x[0].text][i]+=1
        if(x.tag=='filename'):
            df['filename'][i]=x.text

# df.to_csv('Info.csv')       
# for x in root:
#     if x.tag=='object':
#         for j in x.findall('bndbox'):
#             print(j[1].tag)
            
