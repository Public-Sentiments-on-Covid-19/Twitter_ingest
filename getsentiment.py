import jsonlines,csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
d={"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05"}
reader=jsonlines.open("data/tweet_idno4.jsonl")
count=0
analyzer=SentimentIntensityAnalyzer()
writer=csv.writer(open('tweet_sentiment.csv', 'w', encoding='utf-8', newline=''))
for obj in reader:

    # obj=reader.read()
    vs=analyzer.polarity_scores(obj['full_text'])
    time=obj['created_at'].split()
    writer.writerow([vs['compound'],obj['full_text'],"2020-"+d[time[1]]+"-"+time[2]])
    # x=float(vs['compound'])
    #
    # print(time)
    # if x>0:
    #     print(x,"positive")
    # elif x==0:
    #     print(x,"neutral")
    # else:
    #     print(x,"negative")

    count+=1
    if count%10000==0:
        print(count)