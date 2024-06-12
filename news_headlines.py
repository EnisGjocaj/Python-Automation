from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#for headless automatrion mode
from selenium.webdriver.chrome.options import Options

import pandas as pd #for creating a dataframe

#Start of the code to make the script run everyday
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()

#We want the format MMDDYYYY, so we get the code from the website strftime.org
month_day_year = now.strftime("%m%d%Y") # string from time


website = "https://www.thesun.co.uk/sport/football/"
path = r"C:\Users\Admin\Downloads\chromedriver-win64\chromedriver-win64/chromedriver.exe"



#head-less mode
options = Options()
# options.headless = True #This should work but its not working
options.add_argument("--headless")



service = Service(executable_path=path)
# driver = webdriver.Chrome(service=service) # this is how we create the driver without headless mode 
driver = webdriver.Chrome(service=service, options=options) #This is headless mode

driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser-item teaser__small  theme-football"]/div[@class = "teaser__copy-container"]')
# if we user the method find_element. itll get us only the forst element , but if we want to get more elements that have the same attribut we cant do that, thats why we use the plural elements


#We can select the headers like this , but since we can iterate through the containers therer a better eway to write this syntax.
# driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]/a/span')


#exporting data to csv
titles = []
subtitles = []
links = []


#Like this :

for container in containers:
	title = container.find_element(by='xpath', value='./a/span').text #we can use the . here since instead of the actual driver , ere using the container, so we are selecteing the current node weith the .
	subtitle = container.find_element(by='xpath', value='./a/h3').text
	link = container.find_element(by="xpath", value='./a').get_attribute("href") #we get the link

	titles.append(title)
	subtitles.append(subtitle)
	links.append(link)


#exporting the data to csv

my_dictionary = {
	'title': titles,
	'subtitle': subtitles,
	'link': links
}


df_headlines = pd.DataFrame(my_dictionary)


file_name = f'headline-{month_day_year}.csv'

final_path = os.path.join(application_path, file_name)

#df_headlines.to_csv('headline-headless.csv') with headless
df_headlines.to_csv(final_path)  #with time automating

driver.quit()

