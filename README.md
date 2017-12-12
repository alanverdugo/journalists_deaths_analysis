Correlations between ruling political parties and journalist assassinations
====================================================

Abstract
-----------------
This research uses a dataset provided by the Committee to Protect Journalists in order to analyze the number of journalists’ deaths in Mexico and the US from 1992 to 2016, it compares both results, and tries to find out if the ruling political party is regarded as an important factor that could be the root cause of said deaths.
The analysis points out that the ruling political party cannot be directly linked to the cause of the deaths, but the political strategies implemented by the government could be related indirectly.


Motivation
-----------------
Mexico is widely regarded as one of the most dangerous countries for journalists, even comparing to countries in a state of war. Added to that, the mexican government is also famous for being corrupt and untrustworthy, either by bribing the media or by threating it. This has happened since the 1910s, and the involvement of Mexico in illegal drug traffic has only added to the dangers the journalists face.

Since the mexican government has been known to bride or to threaten journalists, I wanted to get actual data that could show a correlation between the ruling political parties of the past and the amount of violence towards media workers. This could help the mexican citizens to make a decision before the presidential election of 2018.

Dataset
-----------------
The dataset that will be used is a comma-separated file provided by the Committee to Protect Journalists (https://cpj.org). It contains data about journalists assassinations committed from 1992 to 2016. The dataset contains 1782 records with 18 variables: *Type, Date, Name, Sex, Country_killed, Organization, Nationality, Medium, Job, Coverage, Freelance, Local_Foreign, Source_fire, Type_death, Impunity_for_murder, Taken_captive, Threatened, Tortured*.

The dataset can be downloaded from Kaggle.com:
https://www.kaggle.com/cpjournalists/journalists-killed-worldwide-since-1992


Data preparation and cleaning
-----------------
Some of the records did not have a date for the death of the journalist (it was either labeled “Unknown” or “Date unknown”), this prevent me from assigning it to a year and thus to a presidential administration, so, sadly, I had to ignore them. Besides, the date format was relatively hard to parse since it was not in a very standard format. For example, the date was in the form “February 9, 1998”, instead of the much more international and easy to use “1998-02-09”.

Research questions
-----------------
Is there a correlation between the ruling political party and the number of journalists assassinations?

Can we identify a corrupt government by analyzing the acts of violence against journalists occurred during its administration?

Methods
-----------------
I filtered all records that belong to the interesting countries, then I grouped them by year and built charts according to the length of each presidential administration. This allowed me to show visualizations that can easily convey any increase or decrease of journalist assassinations by the ruling political party in each period.
After that, I built a pie chart showing the distribution of the “Source_fire” variable, which provides a better idea of the reason behind the assassination. This could help to understand if the death was a deliberate targeted attack on the journalists or if it could be regarded as a work-related accident.

The entire script that processed the data and generated the visualizations can be found here:
https://github.com/alanverdugo/journalists_deaths_analysis/blob/master/cpj.py


Findings
--------
![alt text]( https://github.com/alanverdugo/journalists_deaths_analysis/blob/master/Mexico.png?raw=true "Number of journalists killed in Mexico")
*Figure 1: Number of journalists killed in Mexico.*

In this chart we see the two parties that have been in power in Mexico (in different colors). An increase in journalists’ deaths occurred during the mid 2000s, then appeared to decrease but now seems to be increasing again.

----------

![alt text]( https://github.com/alanverdugo/journalists_deaths_analysis/blob/master/USA.png?raw=true "Number of journalists killed in USA")
*Figure 2: Number of journalists killed in USA.*

For comparison purposes, this is the same chart, but using US data. It can be seen that the US is much safer for journalists, and that there is no clear correlation between the political party in power and journalists’ deaths.

----------

![alt text]( https://github.com/alanverdugo/journalists_deaths_analysis/blob/master/Mexico2.png?raw=true "Number of journalists killed in USA")
*Figure 3: Source of fire for journalists deaths in Mexico.*

This is a pie chart of the source of the fire that caused the journalists deaths in Mexico. We can clearly see that most of the deaths were caused by criminal groups (very probably drug cartels).

Limitations
----------

The dataset is fairly small. This is one of the rare cases where not having a lot of data is a good thing (after all, even a single assassination is a tragic event). However, the relative low number of deaths makes it hard to safely find patterns or correlations. Due to the mystery and inherent danger behind some of the deaths, it may be probable that many of them are not reported to the authorities and even then, acts of corruption could hinder the reach or veracity of the data. In other words, we may probably be working with incomplete data.

Conclusions
----------

Practicing journalism in Mexico has been, and still is, a dangerous activity. Compared against other countries, we can see the relative dangerous situation that journalists located in Mexico experience every day. A change  in the mexican political status quo did not solve the problem, in fact, it appeared to have increased it. This could mean that just changing the political party in power is not enough and that serious strategic changes in security, transparency and drug-related politics need to be done in order to ensure the safety of the journalists and of the mexican citizens in general.

The war on drugs military campaign that started in 2006 was one of the main triggers for the increased amount in violence during the late 2000s. Drug cartels fought against the military and against each other for the control of the territories. However, that does not mean that journalists did not experience attacks before the war on drugs or that they will not experience them in the future. It is unknown how many bribes or threats the journalists receive from corrupt officials or from criminal organizations, so these findings should not be regarded as definitive. 

The geo-political and socio-economic situation of each country is also a complex subject that cannot be fully grasped using such a small set of data. For these reasons, a more complete analysis should be conducted to safely identify the possible correlation between a country ruler and the acts of violence towards the media.



References
----------

 1. Timeline of the Mexican Drug War. (2017, December 4). In Wikipedia, The Free Encyclopedia. Retrieved
04:52, December 9, 2017, from https://en.wikipedia.org/w/index.php?title=Timeline_of_the_Mexican_Drug_War&oldid=813681343
 2. List of Presidents of the United States. (2017, December 7). In Wikipedia, The Free Encyclopedia.
Retrieved 05:09, December 8, 2017, from
https://en.wikipedia.org/w/index.php?title=List_of_Presidents_of_the_United_States&oldid=814280717
 3. Mexican Drug War. (2017, December 4). In Wikipedia, The Free Encyclopedia. Retrieved 04:52,
December 9, 2017, from
https://en.wikipedia.org/w/index.php?title=Mexican_Drug_War&oldid=813724408
 4. List of journalists and media workers killed in Mexico. (2017, November 28). In Wikipedia, The Free
Encyclopedia. Retrieved 17:38, December 9, 2017, from
https://en.wikipedia.org/w/index.php?title=List_of_journalists_and_media_workers_killed_in_Mexico&old
id=812565094
