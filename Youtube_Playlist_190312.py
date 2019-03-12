#!/usr/bin/env python
# coding: utf-8

# In[1]:


#First_Code_190312_junswj

from urllib.request import urlopen as uReq
import pandas as pd
pd.set_option('display.max_rows', 500)


# In[2]:


my_url= input("Enter Youtube Playlist URL:")


# In[3]:


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_str=str(page_html)


# In[4]:


songinfo_list=[]
songinfo_one_each=[]
rep_count=1
rep_count_max=page_str.count('data-video-title="')


# In[5]:


while rep_count <= rep_count_max: 
    si_index_1 = page_str.index('data-video-title="')
    si_index_2 = len('data-video-title="')
    si_index = si_index_1 + si_index_2
    songinfo=page_str[si_index:si_index+150]
    songinfo_list.append(songinfo[:songinfo.find('"')])
    page_str=page_str[si_index:]
    rep_count += 1


# In[6]:


songinfo_list.sort()
songinfo_one_each=[i.replace("&#39;", "'") for i in songinfo_list]
songinfo_one_each=[i.replace("&quot;", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("&amp;", "&") for i in songinfo_one_each]
songinfo_one_each=[i.replace(":", "-") for i in songinfo_one_each]
songinfo_one_each=[i.replace("\\xc3\\xa9", "e") for i in songinfo_one_each]
songinfo_one_each=[i.replace("(Official Video)", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("(Official)", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("[Official Audio]", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("(Official Lyric Video)", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("[Official Lyric Video]", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("[Official Music Video]", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("(Official Music Video)", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("[OFFICIAL MUSIC VIDEO]", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("(Official Audio)", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("[Official Video]", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("(Lyric Video)", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("(Audio)", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("(Lyrics)", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("(Lyric)", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("(lyric)", "") for i in songinfo_one_each]
songinfo_one_each=[i.replace("(lyrics)", "") for i in songinfo_one_each]


# In[7]:


artist=[i.split('-', 2)[0] for i in songinfo_one_each]


# In[8]:


yt_video_table = pd.DataFrame({'Artist Name':artist, 'Video': songinfo_one_each})


# In[9]:


yt_video_table


# In[10]:


yt_video_table.to_csv('Youtube_Playlist.csv')


# In[ ]:




