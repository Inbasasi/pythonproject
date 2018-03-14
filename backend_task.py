# -*- coding: utf-8 -*0
"""
Created on Mon Mar 12 23:46:50 2018

@author: Inba
"""

import urllib.request, json,re
         #imported modules for importing an url and usage of regular expression
with urllib.request.urlopen("https://gist.githubusercontent.com/murtuzakz/4bd887712703ff14c9b0f7c18229b332/raw/d0dd1c59016e2488dcbe0c8e710a1c5df9c3672e/season7.json") as url:
   data = json.loads(url.read().decode())
#with open('C:\\Users\\Inba\\Desktop\\file.json') as json_data:
  #data = json.load(json_data)
j=0
main=[]  #which gonna contain the investor and company values
epi = ['Episode 1','Episode 2','Episode 3','Episode 4','Episode 5','Episode 6','Episode 7','Episode 8','Episode 9','Episode 10','Episode 11','Episode 12','Episode 13','Episode 14','Episode 15','Episode 16','Episode 17','Episode 18','Episode 19','Episode 20','Episode 21','Episode 22','Episode 23','Episode 24']

for ep in epi:
    for v1 in data[ep]:      
            cmpy=[]
            v2= v1['investors']
            v3=re.split(' and |, |and |\n',v2)
            re.sub('\n', '',str(v3))
            t2=v1['company']
            t3=t2['title'] 
            cmpy.append(t3)
            for i in v3:
               invest=[] 
               if i != '':   #empty investor names are left
                 invest.append(i)   
                 invest.append(t3)
                 main.append(invest)
       #declaration of a dictionary
result = dict() 
       #investor as the key, collected all the company name for the respective key as a values to that key 
for indvl in main:
    if indvl[0] in result:
        result[indvl[0]].append(indvl[1])
    else:      
        result[indvl[0]] = [indvl[1]]
      #using sorted function on length of the values of the dictionary
for k in sorted(result, key=lambda k: len(result[k]), reverse=True):
        j=j+1
        print(str(j),".",k,":",result[k])
    
