import pandas as pd
hotelreviews= pd.read_csv('/Users/HavyaN/Downloads/train.csv' ,usecols=['Description'])
print(hotelreviews)
hotelreviews['Description'] = hotelreviews['Description'].astype(str)
#review = hotelreviews["Description"]
#https://www.kaggle.com/anu0012/hotel-review/data
from textblob import TextBlob
#txt=input("Input your movie Review:")
newtext=TextBlob(hotelreviews)
sp=newtext.sentiment.polarity
if sp<0:
    print("This is a good review")
elif sp==0:
    print("The customer is neutral")
elif sp>0 & sp<=1:
    print("This customer is bad")

