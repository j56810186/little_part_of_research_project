
import csv
import requests
from pyquery import PyQuery as pq

res = requests.get("https://www.researchgate.net/post/What_is_the_impact_of_COVID-19_on_your_Research_Academic_activities")
doc = pq(res.text)

# create dataList and set table title.
dataList = [["Name", "Background", "Date", "Comment", "Recommendations"]]

nameRecent = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.most-recent-answer.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-e-text.nova-e-text--size-m.nova-e-text--family-sans-serif.nova-e-text--spacing-none.nova-e-text--color-inherit.nova-v-activity-item__story-subject > a").text()
backgroundRecent = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.most-recent-answer.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-e-text.nova-e-text--size-m.nova-e-text--family-sans-serif.nova-e-text--spacing-none.nova-e-text--color-inherit.nova-v-activity-item__story-body").text()
dateRecent = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.most-recent-answer.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-l-flex__item.nova-l-flex.nova-l-flex--gutter-xs.nova-l-flex--direction-row\@s-up.nova-l-flex--align-items-center\@s-up.nova-l-flex--justify-content-flex-start\@s-up.nova-l-flex--wrap-nowrap\@s-up.nova-v-activity-item__context > div > div").text()
commentRecent = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.most-recent-answer.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div > div > div > div.nova-v-activity-item__entity-list > div > div > div > div > div > div.nova-o-stack__item").text()

# recommendation are not found
recentList = [nameRecent, backgroundRecent, dateRecent, commentRecent, 0]

dataList.append(recentList)


namePopular = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details-popular-answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-e-text.nova-e-text--size-m.nova-e-text--family-sans-serif.nova-e-text--spacing-none.nova-e-text--color-inherit.nova-v-activity-item__story-subject > a").text()
backgroundPopular = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details-popular-answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-e-text.nova-e-text--size-m.nova-e-text--family-sans-serif.nova-e-text--spacing-none.nova-e-text--color-inherit.nova-v-activity-item__story-body").text()
datePopular = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details-popular-answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-l-flex__item.nova-l-flex.nova-l-flex--gutter-xs.nova-l-flex--direction-row\@s-up.nova-l-flex--align-items-center\@s-up.nova-l-flex--justify-content-flex-start\@s-up.nova-l-flex--wrap-nowrap\@s-up.nova-v-activity-item__context > div > div").text()
commentPopular = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details-popular-answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div > div > div > div.nova-v-activity-item__entity-list > div > div > div > div > div > div.nova-o-stack__item").text()
recommendationPopular = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details-popular-answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div > div > div > div.nova-v-activity-item__entity-list > div > div > div > div > div > div.nova-l-flex__item.nova-l-flex.nova-l-flex--gutter-m.nova-l-flex--direction-row\@s-up.nova-l-flex--align-items-stretch\@s-up.nova-l-flex--justify-content-space-between\@s-up.nova-l-flex--wrap-wrap\@s-up > div:nth-child(2) > div > div").text()

popularList = [namePopular, backgroundPopular, datePopular, commentPopular, recommendationPopular]

dataList.append(popularList)

answerToken = 1

while True:
    # Get what content I want
    name = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details__answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div:nth-child(" + str(answerToken) + ") > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-e-text.nova-e-text--size-m.nova-e-text--family-sans-serif.nova-e-text--spacing-none.nova-e-text--color-inherit.nova-v-activity-item__story-subject > a").text()
    background = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details__answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div:nth-child(" + str(answerToken) + ") > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-e-text.nova-e-text--size-m.nova-e-text--family-sans-serif.nova-e-text--spacing-none.nova-e-text--color-inherit.nova-v-activity-item__story-body").text()
    date = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details__answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div:nth-child(" + str(answerToken) + ") > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-l-flex__item.nova-l-flex.nova-l-flex--gutter-xs.nova-l-flex--direction-row\@s-up.nova-l-flex--align-items-center\@s-up.nova-l-flex--justify-content-flex-start\@s-up.nova-l-flex--wrap-nowrap\@s-up.nova-v-activity-item__context > div > div").text()
    comment = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details__answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div:nth-child(" + str(answerToken) + ") > div > div > div.nova-v-activity-item__entity-list > div > div > div > div > div > div.nova-o-stack__item").text()
    recommendation = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details__answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div:nth-child(" + str(answerToken) + ") > div > div > div.nova-v-activity-item__entity-list > div > div > div > div > div > div.nova-l-flex__item.nova-l-flex.nova-l-flex--gutter-m.nova-l-flex--direction-row\@s-up.nova-l-flex--align-items-stretch\@s-up.nova-l-flex--justify-content-space-between\@s-up.nova-l-flex--wrap-wrap\@s-up > div:nth-child(2) > div > div").text()
    if name != '':
        answerList = [name, background, date, comment, recommendation]
        dataList.append(answerList)
        del answerList
        answerToken += 1
    else:
        break

res = requests.get("https://www.researchgate.net/post/What_is_the_impact_of_COVID-19_on_your_Research_Academic_activities/2")
doc = pq(res.text)

nameRecent = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.most-recent-answer.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-e-text.nova-e-text--size-m.nova-e-text--family-sans-serif.nova-e-text--spacing-none.nova-e-text--color-inherit.nova-v-activity-item__story-subject > a").text()
backgroundRecent = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.most-recent-answer.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-e-text.nova-e-text--size-m.nova-e-text--family-sans-serif.nova-e-text--spacing-none.nova-e-text--color-inherit.nova-v-activity-item__story-body").text()
dateRecent = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.most-recent-answer.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-l-flex__item.nova-l-flex.nova-l-flex--gutter-xs.nova-l-flex--direction-row\@s-up.nova-l-flex--align-items-center\@s-up.nova-l-flex--justify-content-flex-start\@s-up.nova-l-flex--wrap-nowrap\@s-up.nova-v-activity-item__context > div > div").text()
commentRecent = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.most-recent-answer.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div > div > div > div.nova-v-activity-item__entity-list > div > div > div > div > div > div.nova-o-stack__item").text()

# recommendation are not found
recentList = [nameRecent, backgroundRecent, dateRecent, commentRecent, 0]

dataList.append(recentList)

answerToken = 1

while True:
    # Get what content I want
    name = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details__answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div:nth-child(" + str(answerToken) + ") > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-e-text.nova-e-text--size-m.nova-e-text--family-sans-serif.nova-e-text--spacing-none.nova-e-text--color-inherit.nova-v-activity-item__story-subject > a").text()
    background = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details__answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div:nth-child(" + str(answerToken) + ") > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-e-text.nova-e-text--size-m.nova-e-text--family-sans-serif.nova-e-text--spacing-none.nova-e-text--color-inherit.nova-v-activity-item__story-body").text()
    date = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details__answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div:nth-child(" + str(answerToken) + ") > div > div > div.nova-v-activity-item__stack > div > div > div.nova-l-flex__item.nova-l-flex__item--grow.nova-v-activity-item__story-content > div.nova-l-flex__item.nova-l-flex.nova-l-flex--gutter-xs.nova-l-flex--direction-row\@s-up.nova-l-flex--align-items-center\@s-up.nova-l-flex--justify-content-flex-start\@s-up.nova-l-flex--wrap-nowrap\@s-up.nova-v-activity-item__context > div > div").text()
    comment = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details__answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div:nth-child(" + str(answerToken) + ") > div > div > div.nova-v-activity-item__entity-list > div > div > div > div > div > div.nova-o-stack__item").text()
    recommendation = doc("#lite-page > main > section.lite-page__content > div.nova-c-card.nova-c-card--spacing-none.nova-c-card--elevation-1-above.post-details__answers-list.post-details__section > div.nova-c-card__body.nova-c-card__body--spacing-none > div > div:nth-child(" + str(answerToken) + ") > div > div > div.nova-v-activity-item__entity-list > div > div > div > div > div > div.nova-l-flex__item.nova-l-flex.nova-l-flex--gutter-m.nova-l-flex--direction-row\@s-up.nova-l-flex--align-items-stretch\@s-up.nova-l-flex--justify-content-space-between\@s-up.nova-l-flex--wrap-wrap\@s-up > div:nth-child(2) > div > div").text()
    if name != '':
        answerList = [name, background, date, comment, recommendation]
        dataList.append(answerList)
        del answerList
        answerToken += 1
    else:
        break

with open("researchGate_Covid19ImpactAcademic.csv", "w", newline="", encoding="UTF-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(dataList)
