# sentimentanalysis
Package Summary
TextBlob is a python library that looks at text analysis offers a simple API to access its methods and perform basic NLP tasks based on the text given. Its able to perform tasks such as sentiment analysis, language translation, spelling corrections, etc.

Install and Run Instructions.
Install Textblob with : pip install textblob 
1.from textblob import TextBlob -- imports the TextBlob function from the package
2.txt=input("Input your movie Review:") -- lets the user input text and converts that into input
3.def rev(txt):-- The fuction rev uses the txt input from above and performs .sentimentpolarity, looking at the keywords of the text and produces a number from -1 to 1 which passes through the fuction and prints text based on if its positive or not, grater than 0 being positive.  

Future idea. What if I asked you to use this package in your final class project? Describing one idea, including explaining what this package would do in that project.
Textblob has a lot of potential to analyze text, a possible final project idea is to look at live twitter feed that is relating to the COVID vaccine with tweety and analyze the tweets to see if they are positive or negative overall with textblob. 
