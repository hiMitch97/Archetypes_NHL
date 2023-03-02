import hockey_scraper

# Scrapes all games between of the 2021/2022 season with shifts and store the data in two separate csv files

games = hockey_scraper.scrape_seasons(seasons=[2021], if_scrape_shifts=True, data_format='csv', preseason=False)

