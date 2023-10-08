from textblob import TextBlob

print("*** Enter the view and check which class it comes under positive or negative or neutral***")

Input = input('Enter The Review :')

sent = TextBlob(Input)

score = sent.sentiment

if score.polarity > 0.5 :
    print('Positive Sentiment')

elif score.polarity<0:
    print('Negative Sentiment')

else :
    print('Neutral Sentiment')


