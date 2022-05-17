#!/usr/bin/env python
# coding: utf-8

# In[15]:


""" BEFORE THE START, YOU MUST REMOVE THE GFF STANDARD HEADER AND INPUT A NEW ONE:

Cromossomo    Genbank    regiao    pbinicio    pbfim    .    +    .    annotation

(you can adapt if you want, if so, remember to change the columns names in the loop lines of the code)."""

import pandas as pd

#read NCRF.summarynofilter archive (contains information about the sequence arrays localization);
df = pd.read_table("ameCgoSat75-21.noise20.summarynofilter")

#store the information of the NCRF archive into variables to utilize as index later;
var1 = df.iloc[:,2].tolist() #index of scaffold / chromosome.

var2 = df.iloc[:,3].tolist() #sequence array beginning base pair.

var3 = df.iloc[:,4].tolist() #sequence array ending base pair.


# In[16]:


#open annotation.GFF file;
df2 = pd.read_table("GCA_019721115.1_AMEX_1.1_genomic.GFF") #remember, it must have the new columns names!

df2 = df2.dropna(how="any", axis=0) #treatment for deleting lines with empty values.


# In[20]:


#extraction of data:
df5 = pd.DataFrame() #creating the final dataframe (empty by now)

"""  loop to find rows in df columns which contain something between a range of values;
     (find rows with a chromosome/scaffold and then look for row between base pairs).    """
for i in range(len(var1)):
    df3 = df2[df2['Cromossomo'] == var1[i]]
    df4 = df3[((var2[i]-10000) <= df3['pbinicio']) & (df3['pbfim'] <= (var3[i]+10000))]
    #here you can change the additional downstream/upstream base pair portion for extraction.
    df5 = df5.append(df4)

df5 = df5.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)

float_col = df5.select_dtypes(include=['float64']) #This will select float columns and store it in a var. for the loop below:
for col in float_col: #loop to transform the columns "pbinicio" and "pbfim" into integers
    df5[col] = df5[col].astype('int64')

df5.to_csv('GFFextractor1.csv', index=False) #save the final dataframe to an csv.


# In[ ]:




