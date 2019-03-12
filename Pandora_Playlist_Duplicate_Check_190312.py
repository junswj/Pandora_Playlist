#!/usr/bin/env python
# coding: utf-8

# In[1]:


#First_Code_190312_junswj

from urllib.request import urlopen as uReq
import pandas as pd
pd.set_option('display.max_rows', 500)


# In[2]:


my_url= input("Enter Pandora Playlist URL:")


# In[3]:


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_str=str(page_html)


# In[4]:


songinfo_list=[]
songinfo_one_each=[]
rep_count=1
rep_count_max=page_str.count('","shareableUrlPath":"/artist/')


# In[5]:


while rep_count <= rep_count_max: 
    si_index_1 = page_str.index('","shareableUrlPath":"/artist/')
    si_index_2 = len('","shareableUrlPath":"/artist/')
    si_index = si_index_1 + si_index_2
    songinfo=page_str[si_index:si_index+150]
    songinfo_list.append(songinfo[:songinfo.find('"')-15])
    page_str=page_str[si_index:]
    rep_count += 1


# In[6]:


songinfo_list.sort()
songinfo_one_each=[i.replace('-', ' ') for i in songinfo_list]
artist=[i.split('/', 3)[0] for i in songinfo_one_each]
album=[i.split('/', 3)[1] for i in songinfo_one_each]
song=[i.split('/', 3)[2] for i in songinfo_one_each]


# In[7]:


table = pd.DataFrame({'Artist Name':artist, 'Album Name':album, 'Song': song})


# In[8]:


table=table.drop(table[table.Song == ''].index)
table=table.drop_duplicates()
table=table.reset_index().drop(columns='index')


# In[9]:


table


# In[10]:


page_str=str(page_html)
track_ID=[]
dupli_track_ID=[]
list_count=1
list_count_max=page_str.count('","addedTimestamp":')


# In[11]:


while list_count <= list_count_max: 
    tr_index = page_str.index('","addedTimestamp":')
    track_ID.append(page_str[tr_index-11:tr_index]) 
    page_str=page_str[tr_index+1:]
    list_count +=1


# In[12]:


dupli_check= pd.DataFrame({'Track_ID':track_ID}).duplicated()


# In[13]:


dupli_track=dupli_check.index[dupli_check == True].tolist()


# In[14]:


for i in range(len(dupli_track)):
    dupli_track_ID.append(track_ID[(dupli_track[i])])


# In[15]:


dupli_songinfo_list=[]
dupli_count=1
dupli_count_max=len(dupli_track_ID)


# In[16]:


while dupli_count <= dupli_count_max: 
    page_str=str(page_html)
    dupli_index_1 = dupli_index=page_str.index('/'+dupli_track_ID[dupli_count-1])
    page_str=page_str[:dupli_index_1]
    dupli_index_2=page_str.rfind('/')
    dupli_songinfo_list.append(page_str[dupli_index_2+1:])
    dupli_count += 1


# In[17]:


dupli_songinfo_list=[i.replace('-', ' ') for i in dupli_songinfo_list]


# In[18]:


table_duplicated=0


# In[19]:


for i in range(len(dupli_songinfo_list)):
    table_duplicated=table_duplicated+(table['Song'].str.find(dupli_songinfo_list[i]))+1


# In[20]:


table['Duplicated']=table_duplicated


# In[21]:


dupli_checked_table=table.sort_values(by='Duplicated', ascending=False)
dupli_checked_table=dupli_checked_table.reset_index().drop(columns='index')


# In[22]:


dupli_checked_table


# In[23]:


dupli_checked_table.to_csv('Pandora_Playlist_Duplicate_Checked.csv')


# In[ ]:




