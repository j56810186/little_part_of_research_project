import pandas as pd
import stanza

nlp = stanza.Pipeline(lang='en', processors='tokenize, sentiment')

df = pd.read_csv('researchGate_Covid19ImpactAcademic.csv')
textsList = []
for comment in df['Comment']:
    textsList.append(comment)

docList = []
for text in textsList:
    docList.append(nlp(text))

resultList = []
for doc in docList:
    tmpResultList = []
    for sentence in doc.sentences:
        tmpResultList.append(sentence.sentiment)
    resultList.append(tmpResultList)

for result in resultList:
    totalScore = 0
    for eachScore in result:
        totalScore += eachScore
    resultList[resultList.index(result)] = round(totalScore/len(result) - 1, 3) * 10

df['SentimentOfComment'] = resultList

df.to_csv('sentimentAnalysis_researchGate.csv', encoding='UTF-8')
