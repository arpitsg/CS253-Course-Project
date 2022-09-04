
# In[529]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import datetime
pd.options.mode.chained_assignment = None  # default='warn'
import seaborn as sns
from matplotlib.pyplot import figure
from scipy.stats import norm
plt.rcParams.update({'font.size': 22})
plt.rcParams['axes.titlesize'] = 22


# In[530]:


df = pd.read_csv('./disneyMoviesDataset.csv')


# In[ ]:





# In[531]:



# In[554]:


dft=df[df['imdb'].notna()]
plt.figure(figsize=(14,7)) 
plt.style.use('seaborn-whitegrid') 
plt.hist(dft['imdb'], bins='auto', facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
plt.title('IMDB HISTOGRAM') 
plt.xlabel('IMDB Rating') 
plt.ylabel('Number of Movies') 
plt.savefig('figures/1.png', bbox_inches='tight')
plt.show()


# In[533]:


# In[557]:


df['rotten_tomatoes'] = df['rotten_tomatoes'].str.replace('%','')
df['rotten_tomatoes']=df.rotten_tomatoes.replace('',np.nan).astype(float)

dft=df[df['rotten_tomatoes'].notna()]
plt.figure(figsize=(14,7)) 
plt.style.use('seaborn-whitegrid') 
plt.hist(dft['rotten_tomatoes'], bins='auto', facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
plt.title('Rotten Tomatoes Histogram') 
plt.xlabel('Rotten tomatoes Rating') 
plt.ylabel('Number of Movies')
plt.xticks(rotation=90)
plt.savefig('figures/3.png', bbox_inches='tight')

plt.show()


# In[ ]:

plt.rcParams.update({'font.size': 10})

dft=df[df['Release date (datetime)'].notna()]
dft['Release date (datetime)'] = pd.to_datetime(dft['Release date (datetime)'], format='%Y-%m-%d %H:%M:%S')

dft['Release date (datetime)'] = dft['Release date (datetime)'].dt.month
explode = (0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0.15)  # only "explode" the 2nd slice (i.e. 'Hogs')

xi=dft['Release date (datetime)'].value_counts()
labels=['Jan' ,'Feb', 'Mar' ,'Apr', 'May' ,'Jun', 'Jul' ,'Aug' ,'Sep' ,'Oct' ,'Nov', 'Dec']
plt.pie(x=xi, autopct="%.1f%%", pctdistance=0.7, shadow = True,explode=explode,labels=labels)    
plt.savefig('figures/5.png', bbox_inches='tight')
plt.show()


# In[564]:

plt.rcParams.update({'font.size': 22})

#content made every year scatter plot
dft=df[df['Release date (datetime)'].notna()]
dft['Release date (datetime)'] = pd.to_datetime(dft['Release date (datetime)'], format='%Y-%m-%d %H:%M:%S')

dft['Release date (datetime)'] = dft['Release date (datetime)'].dt.year

x=dft['Release date (datetime)'].value_counts()
plt.figure(figsize=(14,7)) 
plt.style.use('seaborn-whitegrid') 
plt.title('Movies made Per year') 
plt.xlabel('Year') 
plt.ylabel('No. of movies')
plt.scatter(x.index,x)
plt.savefig('figures/4.png', bbox_inches='tight')


# In[568]:




# In[537]:





# In[ ]:





# In[617]:


dft=df[df['Box office (float)'].notna()]
dft=dft[dft['imdb'].notna()]
dft=dft[dft['Budget (float)'].notna()].sort_values('imdb',ascending=False).head(15).reset_index()

x = dft['title']
y2 = dft['Budget (float)']
y1 = dft['Box office (float)']
plt.style.use('seaborn-whitegrid') 




width = 0.33
    
plt.figure(figsize=(15,7))

plt.bar(dft.index, y1, width) 

plt.bar(dft.index +width, y2, width) 

plt.xticks(dft.index, dft['title'], rotation=90)


plt.ylabel('Amount in Billion dollor')
plt.xlabel(' Movies ')

plt.title('Box Office and Budget  Of Top 10 movies by IMDB Rating')

plt.legend(['Box Office', 'Budget'])

plt.grid()
plt.savefig('figures/6.png', bbox_inches='tight')

plt.show()


# In[616]:


dft=df[df['Box office (float)'].notna()]
dft=dft[dft['imdb'].notna()]
dft=dft[dft['Budget (float)'].notna()].sort_values('imdb',ascending=True).head(15).reset_index()

x = dft['title']
y2 = dft['Budget (float)']
y1 = dft['Box office (float)']
plt.style.use('seaborn-whitegrid') 



width = 0.33
    
plt.figure(figsize=(15,7))

plt.bar(dft.index, y1, width) 

plt.bar(dft.index +width, y2, width) 

plt.xticks(dft.index, dft['title'], rotation=90)


plt.ylabel('Amount in 100 million dollor')
plt.xlabel(' Movies ')

plt.title('Box Office and Budget  Of Worst 10 movies by IMDB Rating')

plt.legend(['Box Office', 'Budget'])

plt.grid()
plt.savefig('figures/7.png', bbox_inches='tight')

plt.show()


# In[571]:

dft=df[df['Running time (int)'].notna()]

plt.figure(figsize=(15,7))
plt.style.use('seaborn-whitegrid') 

sns.distplot(dft['Running time (int)'],fit=norm,kde=False, color=['red'])

plt.xlabel(' Duration of movies ')

plt.title('Normal Distribution of movies')
plt.savefig('figures/8.png', bbox_inches='tight')

plt.show()


# In[620]:


dft=df[df['Country'].notna()]
dft.Country = dft.Country.str.replace('[', '')
dft.Country = dft.Country.str.replace(']', '')
dft.Country = dft.Country.str.replace('\'', '')
dft.Country = dft.Country.str.replace(' ', '')
plt.figure(figsize=(14,7)) 
plt.style.use('seaborn-whitegrid') 
dft=dft.Country.str.get_dummies(',').stack().sum(level=1).sort_values(ascending=False).head(10)
plt.title("Top 10 countries where Disney movies are produced")
plt.xlabel('Country') 
plt.ylabel('Number of movies')
ax=dft.plot(kind='bar',facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
plt.legend(['Country'])

for p in ax.patches:
    ax.annotate(format(p.get_height()), (p.get_x()+0.15, p.get_height()), bbox=dict(boxstyle="round", fc="w", ec="gray"),)
plt.savefig('figures/9.png', bbox_inches='tight')


# In[ ]:





# In[ ]:





# In[621]:


dft=df[df['Language'].notna()]
dft.Language = dft.Language.str.replace('[', '')
dft.Language = dft.Language.str.replace(']', '')
dft.Language = dft.Language.str.replace('\'', '')
dft.Language = dft.Language.str.replace(' ', '')
plt.figure(figsize=(14,7)) 
plt.style.use('seaborn-whitegrid') 
dft=dft.Language.str.get_dummies(',').stack().sum(level=1).sort_values(ascending=False).head(10)
plt.title("Top 10 Languages in which Disney movies are produced")
plt.xlabel('Language') 
plt.ylabel('Number of movies')
ax=dft.plot(kind='bar',facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
plt.legend(['Language'])

for p in ax.patches:
    ax.annotate(format(p.get_height()), (p.get_x()+0.15, p.get_height()), bbox=dict(boxstyle="round", fc="w", ec="gray"),)
plt.savefig('figures/10.png', bbox_inches='tight')


# In[622]:


dft=df[df['Directed by'].notna()]
dft['Directed by'] = dft['Directed by'].str.replace('[', '')
dft['Directed by'] = dft['Directed by'].str.replace(']', '')
dft['Directed by'] =  dft['Directed by'].str.replace('\'', '')
dft['Directed by'] =  dft['Directed by'].str.replace(' ', '')
plt.figure(figsize=(14,7)) 
plt.style.use('seaborn-whitegrid') 
dft=dft['Directed by'].str.get_dummies(',').stack().sum(level=1).sort_values(ascending=False).head(10)
plt.title("Top 10 Director making highest disney movies")
plt.xlabel('Director') 
plt.ylabel('Number of movies')
ax=dft.plot(kind='bar',facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
plt.legend(['Director'])

for p in ax.patches:
    ax.annotate(format(p.get_height()), (p.get_x()+0.15, p.get_height()), bbox=dict(boxstyle="round", fc="w", ec="gray"),)
plt.savefig('figures/11.png', bbox_inches='tight')


# In[ ]:





# In[623]:


dft=df[df['Produced by'].notna()]
dft['Produced by'] = dft['Produced by'].str.replace('[', '')
dft['Produced by'] = dft['Produced by'].str.replace(']', '')
dft['Produced by'] =  dft['Produced by'].str.replace('\'', '')
dft['Produced by'] =  dft['Produced by'].str.replace(' ', '')
plt.figure(figsize=(14,7)) 
plt.style.use('seaborn-whitegrid') 
dft=dft['Produced by'].str.get_dummies(',').stack().sum(level=1).sort_values(ascending=False).head(10)
plt.title("Top 10 Producer of highest disney films")
plt.xlabel('Producer of movie') 
plt.ylabel('Number of movies')
ax=dft.plot(kind='bar',facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
plt.legend(['Producer'])

for p in ax.patches:
    ax.annotate(format(p.get_height()), (p.get_x()+0.15, p.get_height()), bbox=dict(boxstyle="round", fc="w", ec="gray"),)
plt.savefig('figures/12.png', bbox_inches='tight')
  


# In[ ]:





# In[597]:


dft=df[df['Box office (float)'].notna()]
dft=dft[dft['imdb'].notna()]
dft=dft[dft['Budget (float)'].notna()]

dft['Revenue']=(dft['Box office (float)']-dft['Budget (float)'])
dft['Revenue']

plt.figure(figsize=(14,7)) 
plt.style.use('seaborn-whitegrid') 
plt.title("Revenue vs IMDB rating")
plt.xlabel('Revenue in Billion Dollar') 
plt.ylabel('IMDB Rating')
plt.scatter(dft['Revenue'], dft['imdb'], color='r')
plt.savefig('figures/13.png', bbox_inches='tight')

plt.show()


# In[599]:


#content made every year vs imdb avg

dft=df[df['imdb'].notna()]
dft=df[df['Release date (datetime)'].notna()]
dft['Release date (datetime)'] = pd.to_datetime(dft['Release date (datetime)'], format='%Y-%m-%d %H:%M:%S')

dft['year'] = dft['Release date (datetime)'].dt.year
dft=dft.sort_values('year',ascending=True)
a=dft.groupby(['year'])['imdb'].mean().reset_index()
plt.figure(figsize=(14,7)) 

plt.style.use('seaborn-whitegrid') 

plt.title("Average IMBD rating per year")
plt.xlabel('Year') 
plt.ylabel('IMDB Rating')
plt.plot(a['year'],a['imdb'], color = 'r')
plt.legend(['Average IMDB Rating per year'])
plt.savefig('figures/14.png', bbox_inches='tight')

plt.show()


# In[624]:





# In[ ]:dft=df[df['imdb'].notna()]

plt.figure(figsize=(25,7)) 
plt.style.use('seaborn-whitegrid') 
plt.title('Movies IMDB and (Rotten tomato score)/10') 
plt.xlabel('Movie Index') 
plt.ylabel('Normalized score out of 10')

plt.scatter(dft.index,dft['imdb'])

plt.scatter(dft.index,(dft['rotten_tomatoes']/10))

plt.legend(['IMDB','Rotten Tomatoes/10'])
plt.savefig('figures/2.png', bbox_inches='tight')

plt.show()





# In[547]:


dft=df[df['imdb'].notna()].sort_values('imdb',ascending=False).head(10)

plt.figure(figsize=(14,7)) 
plt.style.use('seaborn-whitegrid')
ax = dft['imdb'].plot(kind='bar',facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
ax.set_title('IMDB TOP 10')
ax.set_xlabel('Movies/ Tv Shows')
ax.set_ylabel('IMDB RATING')
ax.set_xticklabels( dft['title'])


for p in ax.patches:
    ax.annotate(format(p.get_height()), (p.get_x()+0.15, p.get_height()), bbox=dict(boxstyle="round", fc="w", ec="gray"),)
plt.savefig('figures/15.png' , bbox_inches='tight')


# In[548]:


dft=df[df['imdb'].notna()].sort_values('imdb',ascending=True).head(10)

plt.figure(figsize=(14,7)) 
plt.style.use('seaborn-whitegrid')
ax = dft['imdb'].plot(kind='bar',facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
ax.set_title('IMDB WORST 10 MOVIES')
ax.set_xlabel('MOVIES')
ax.set_ylabel('IMDB RATING')
ax.set_xticklabels( dft['title'])


for p in ax.patches:
    ax.annotate(format(p.get_height()), (p.get_x()+0.15, p.get_height()), bbox=dict(boxstyle="round", fc="w", ec="gray"),)
plt.savefig('figures/16.png', bbox_inches='tight')


# In[630]:


r=7.5
#content made every year scatter plot
dft=df[df['Release date (datetime)'].notna()]
dft=dft[dft['imdb'].notna()]

dft['Release date (datetime)'] = pd.to_datetime(dft['Release date (datetime)'], format='%Y-%m-%d %H:%M:%S')

dft['year'] = dft['Release date (datetime)'].dt.year
dft=dft.sort_values('year',ascending=False)


a=dft.groupby(['year'])['imdb'].mean().reset_index().tail(20)
x=dft[dft['imdb'] <=r ].groupby('year')['imdb'].count().to_frame('x')
y=dft[dft['imdb'] > r].groupby('year')['imdb'].count().to_frame('y')
plt.figure(figsize=(14,7)) 
plt.style.use('seaborn-whitegrid')
result = pd.concat([x, y], axis=1, sort=False).tail(20)
result = result.fillna(0)
plt.bar(result.index,result.x )
plt.bar(result.index,result.y, bottom = result.x)
plt.xticks(rotation=90)
plt.xticks(result.index, a['year'], rotation=90)
plt.title('Count of last 20 Years movies with Imdb Rating below and above 7.5')
plt.xlabel('Years')
plt.ylabel('No. of movies released per year')
plt.legend(['IMDB <=' +str(r) , 'IMDB > '+str(r)],loc='upper left', bbox_to_anchor=(0.5, 1.05),
           fancybox=True, shadow=True)
plt.savefig('figures/17.png', bbox_inches='tight')

plt.show()



