#Fetch jobs from Greenhouse-hosted job boards using their public JSON feed.

import requests

def greenhouse_scraper(company, filters=None):
    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"
    response = requests.get(url)

    print("Status Code:", response.status_code)
    print(response.text[:1000])

greenhouse_scraper("okta")