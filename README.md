# Ankara-House-Prices-Prediction

<p>This is an end-to-end Machine Learning project which includes scrapy to collect data, scikit learn to implement Machine Learning on collected data, and flask to deploy ML model as a product.
I also built a front-end HTML form to input values to predict the price of whatever house we like.</p>

# Prerequisites

Scrapy, Scikit Learn, Pandas, Numpy, Pickle and Flask (for API) are needed to implement this project.

# Project Structure

This project has 3 main parts(also 3 main folders):
  1) Scraping the data that we need. 
  2) Implementing Machine Learning Model
  3) Deploying the project using Flask.
  
I will get into detail of each part below.

Scraping: I scraped a website which lists real estate prices in Turkey. I collected 15 features of each house in Ankara. 
Some of the features are like the area of a house, the age of it, whether it has furniture or not and stuff like this.
The directory that has scraping related folders is called newscraper. First, you will find a screenshot picture in it which shows the statistics that was brought right after scraping was done.
I collected more than 20.000 different house observations in the end and saved as a csv file.  

Machine Learning: I uploaded the data on jupyter notebook. I did some exploratory data analysis, some feature engineering etc to build a robust ML model. 
I was lucky to have some domain knowledge about houses in Ankara, which facilitated my job during data cleansing. 
I tried a few different models and decided to keep Random Forest Regression as it gave me the best accuracy score. Accuracy score in jupyter notebook is seen as 0.817. 
However I built the same model with %100 of the data for deployment so the final accuracy score should be slightly higher than 0.817. 
Each cell in jupyter notebook has its own explanation so I will keep it short here.

Deployment: This part is under houseprices directory.You will see templates and static folders, which contain the front end html and css files.
There is an HTML form to input values of a house to learn the price of it. All you need to do is click predict button after entering the features of the house. 
I also inserted a screen shot of html page for you to take a look at the final user interface(html page) without implementing all necessary stuff. 
csv file here is a clean version of the dataset and only has numeric values. Therefore, when you enter values to predict the price of a house on html, you need to enter corresponding numeric values.

Do not enter string values in html form, use corresponding numeric values below instead.

Age:  -1 < x < 100

Area: 0 < x < 1000

CreditAvlb: Available:2 / Unknown:1 / Not Available:0

Firsthand: Yes: 2 / No: 1 / Under Constraction:0

FloorCount: -1 < x < 40

FloorNumber:  0 < x < 40 Also, Ground floor:0/ basement floor:-1 

Frontage(Direction): North-faced : 1 / South-faced : 0

Fuel: Natural gas: 3 / Electricity:2 / Fuel Oil: 1 / Coal: 0 

Furniture: With Furniture: 1 / Without Furniture: 0

MaintenanceFee: -1 < x < 2500

Room: 0 < x < 10 (including living room, exluding bathroom and toilet)

Town: 'Gölbaşı' : 10, 'Çankaya': 9, 'Yenimahalle': 8, 'Etimesgut':7, 'Keçiören':6, 'Pursaklar':5, 'Altındağ':4, 'Mamak': 3, 'Sincan':2, Others: 1, 

Le_Heating: Unknown:0 / No Heating: 1 / Geotermic: 2 /  Room Heater:3 / Air Conditioner: 4 / Combi Boiler:5 / Central Heating Boiler:6 / Heat Cost Allocator: 7 / Stove:8
