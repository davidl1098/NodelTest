# NodelTest
David Lucero

Repository in which the application test project for Nodel is located

EXCERCISE 1.-

The link of the used file is the following one: https://docs.google.com/spreadsheets/d/1nUvkzOWmONQ71hYP6EwLoR06cJkqtN1YlrZy31S_AKo/edit#gid=0 

The project will ask you to login into your Google Account for the first time and will request two permissions to access Drive and Google Sheets.

Once you login the access tokens will be save on a "tokens" file, so will not be necessary to login again later for a certain amount of time. 

If you want to use other Google account to login into the project you must delete "tokens" file. 

  *IMPORTANT: Be sure to only have one sheet tab with the name PivotResults. 
  
  
EXCERCISE 2.-

The original Monty Hall problem and the requested variant were replicated and the following results were obtained:

*For 100000 attempts

![image](https://user-images.githubusercontent.com/63079496/196948943-b471faeb-3e4f-4f65-ad2a-eddce1e1fbb5.png)

*For 1000000 attempts

![image](https://user-images.githubusercontent.com/63079496/196949538-0a1c9b0e-de11-41c9-9fef-54f937404738.png)


This results prove that in fact the probability of success if you change your selection increases about 66.6%, that is because at the beginning each one door has the same probability of success (about 33.3%). When the host opens a wrong door the probabilities change, if you stick on your decision the probability will keep the same for that door (33.3%) but for the othe door the probabilities increase to 2/3 instead of 1/3.

So yes, it would be much better if you change your decision after the host opens the incorrect door.

Regarding the variant with an extra door we can see that as you and the host didnt know where is the prize both of you will have almost the same probabilites of hit the winner (about 25%). But supposing none of you select the correct door, taking into account that now we have 4 doors the probability of success gets reduced (about 50%), but even so it is still the best option to change the door.



EXERCISE 3.-

Using Selenium the code is able to pass through all the pages.
