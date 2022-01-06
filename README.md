# yelp-web-scraper

Requires BeautifulSoup4 and ScraperAPIClient

Script runs on the first page of every city then recurses down page numbers if there are multiple numbers. For cities that do not have an output, there are no restaurants fitting the criteria. If the txt_to_xlsw script is being used, a "None" should be added below the city without any output, followed by a newline. 

It is recommended to run the sript separately for each query and migrate the data before going onto the next query. 

The script also requires the use of a ScraperAPIClient account to web-scrape without being blacklisted.

The token should be inputted where TOKEN is written on line 100.
