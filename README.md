Instructions

Disclaimer:
The following project has been made for study purposes so the scrapping has been limited to 10 pages (http requests) only which is more then enough for the other parts of this project. 
In a real world scenario is extremelly important to obseve the etics of performing scrapping and take extra caution to not harm the servers.

To create a new Scrap project
1 - Navigate to the folder where you want to create the project for example cd .\projeto_etl\
2 - Run the command line: scrapy startproject extract

To simulate the Scrapping before you code:
1 - Add the variable "USER_AGENT" on settings.py
1.1 - You can google for "My user Agent" and this will give you the correct value for it
2 - Inside your scrapping project folder run the command scrapy shell
3 - Inside the shell you can run the command fetch("URL")
Note: this will create a variable called response which you can use to navigate as you would regularly do with scrapping, there are several methods you can use so refer to: https://scrapy.org/

To Run the Scrapping
1 - To run the scrapping, you'll navigate to: cd .\projeto_etl\extract\extract\
2 - Then run the command : scrapy crawl mercadolivre -o ["path"]/data.jsonl
3 - In my case the comand will be scrapy crawl mercadolivre -o ../../../data/data.jsonl


GOALS:
1 - check if there is a way to add a bash comand do run scrapy without the need of