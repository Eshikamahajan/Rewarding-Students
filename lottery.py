#IMPORTING NECESSARY LIBRARIES

import numpy as np
import operator
import random
import pandas as pd
import csv




#DEFINING FUNCTION TO SELECT RANDOM SAMPLES OF SIZE K FROM POPULATION="NAME"

def random_sample(name,numbers):
    sampling=random.sample(list(name),k=numbers)
    return(sampling)




#GETTING DIFFERENCE BETWEEN TWO LISTS

def diff(li1,li2):
    return (list(set(li1) - set(li2)))



#READING CSV FILE

df=pd.read_csv("awards.csv",encoding="ISO-8859-1")



##DEADLINEA i.e. MAY 30,2019,5:00:00PM ,STUDENTS SELECTED -->1 FOR THE GRAND AWARD

df_true_4=df.loc[operator.and_(df["Timestamp"] >"4/15/2019 12:11:05 PM" , df["Timestamp"] < "4/30/2019 5:00 PM")]
Products_list_4= df_true_4["Email Address"].tolist()
random_list_4=random_sample(Products_list_4,1)
print("DEADLINE A STUDENTS THE GRAND AWARD\n",random_list_4)



#DEADLINE1 i.e. APRIL 26,2019,5:00:00PM ,STUDENTS SELECTED-->9


#GETTING DF MEETING THE DEADLINE
df_true_1=df.loc[operator.and_(df["Timestamp"] >"4/15/2019 12:11:05 PM" , df["Timestamp"] < "4/26/2019 17:00:00")]

#CONVERTING THE DF["EMAIL ADDRESS"] COLUMN INTO LIST FOR PERFORMING LIST OPERATIONS LIKE DIFFERENCE,SAMPLING etc
Products_list_1= df_true_1["Email Address"].tolist()

next_list_3=diff(Products_list_1,random_list_4)
#SELECTING A SSAMPLE OF SIZE 9 FROM PRODUCTS_LISTS_1
random_list_1=random_sample(next_list_3,9)

#PRINTS THE EMAIL OF THE STUDENTS MATCHING THE RANDOM SAMPLE CREATED
print("DEADLINE 1 STUDENTS  \n",random_list_1)

#df_final_1=df_true_1.loc[random_list_1]



#------------------------------------------------------------------------------------------------------------------------------------------------------------


##DEADLINE2 i.e. APRIL 28,2019,5:00:00PM ,STUDENTS SELECTED -->4

df_true_2=df.loc[operator.and_(df["Timestamp"] >"4/15/2019 12:11:05 PM" , df["Timestamp"] < "4/28/2019 17:00:00 ")]
Products_list_2 = df_true_2["Email Address"].tolist()

#UPDATING LIST ELEIMINATING THE STUDENTS REWARDED UNDER DEADLINE1
next_list_2=diff(Products_list_2,random_list_1)

random_list_2=random_sample(next_list_2,7)
print("DEADLINE 2 STUDENTS \n",random_list_2)

#------------------------------------------------------------------------------------------------------------------------------------------------------------


##DEADLINE3 i.e. APRIL 30,2019,5:00:00PM ,STUDENTS SELECTED -->4

df_true_3=df.loc[operator.and_(df["Timestamp"] >"4/15/2019 12:11:05 PM" , df["Timestamp"] < "4/30/2019 17:00:00 ")]
Products_list_3 = df_true_3["Email Address"].tolist()
next_list_2=diff(Products_list_3,random_list_2)
random_list_3=random_sample(next_list_2,4)
print("DEADLINE 3 STUDENTS  \n",random_list_3)


#------------------------------------------------------------------------------------------------------------------------------------------------------------





final_list=random_list_1+random_list_2+random_list_3+random_list_4

for i in range(0,21):
    df_final=df[(df["Email Address"]==final_list[i])]
    print(df_final.to_string())
    print("\n",i,"\n")



