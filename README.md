Hacklytics 2025 Project! mama bear
Creators: Sanika Karode, Ruhi Patel, Rachel John

A web application that eases the mind of expecting mothers. It allows the user to input basic health info and it will output the level of risk the user is at as well as see past data and risk levels.

## Inspiration
As a group of women, we wanted to create something that could have an impact on our gender. We had already known that we wanted to go into the health track, so we wanted to create a project that had an impact on women's health. Initially, we did some research on uterine cancer, but we quickly realized that the data we needed was not available to us, so we had to switch gears. This led us to find a good dataset about pregnancy risk factors, leading us to the creation of mama bear.
## What it does
Our app provides health insights helping pregnant women keep track of vital metric, such as heart rate, blood pressure, and blood sugar. It helps women make informed decisions by providing their health risk based on their metrics, so they can have healthier and stress-free pregnancies. Our web application aims to ease the minds of pregnant women by trying to reduce the stress of potential changes in risk during pregnancy.
## How we built it
First, we trained a Extreme Gradient Boosting (XGBoost) machine learning model with an open source dataset with over 1000 entries. We tested different pre-trained models accuracies with the dataset in order to determine which model we would integrate into our web application. This allowed for our model to have an 85% accuracy with a 2% variance depending on the randomness of the data. Then we integrated the model into Streamlit so that users could input their own data to receive a risk factor of high,  medium, or low. After the integration, we set up user profiles so that personal data can be stored in each account. 
## Challenges we ran into
The main challenge we had with our project was finding a database that was large enough and had all of the factors that we were looking for. With out initial project idea revolving around uterine cancer, we quickly realized that we did not have access to the type of data that we needed. The datasets that we did find were too small and lacked enough features to be efficiently used with a machine learning model. We also had challenges with setting up a database so user accounts could be stored and data could be stored for each user. An issue we came across after creating the database was that each time a user entered data, the past stored information was being overwritten. We had to figure out how to reconfigure the database so that new entries could be logged.
## Accomplishments that we're proud of
At our last hackathon, we were not able to integrate our back-end, so we did not have as clean of a final product. This time, we were able to integrate our back-end onto a web application across different IDEs. We also learned how to properly use GitHub so that we could all simultaneously work on the project.
## What we learned
We learned a lot about database configuration, integration of back-end and front-end, and the integration of ML models.
## What's next for mama bear
Our model was based on one dataset with a lot of entries. To make the predictions more accurate, we would like to train the model with more data. Furthermore, providing a graphic to represent the user's past information would be helpful for the users as well.
