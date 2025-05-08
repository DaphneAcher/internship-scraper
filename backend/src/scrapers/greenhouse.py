import requests
import json

def greenhouse_scraper(company,filters=None):
    if filters is None:
        filters = {}

    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Sorry! {company} not found!")
        return

    data = response.json()

    if "jobs" not in data:
        print(f"No jobs found at {company}")
        return
    
    for job in data["jobs"]:
        location_match = True
        if "location" in filters:
            location_match = filters["location"].lower() in job["location"]["name"].lower()


        keyword_match = True
        if "keyword" in filters:
            keyword_match = filters["keyword"].lower() in job["title"].lower()

            
        if location_match and keyword_match:
            print({company})
            print(job["title"], "-", job["location"]["name"])

    
    
greenhouse_scraper("spacex", filters={"location":"United States","keyword": "intern"})
greenhouse_scraper("robinhood", filters={"location":"United States","keyword": "intern"})
greenhouse_scraper("notion", filters={"location":"United States","keyword": "intern"})
greenhouse_scraper("stripe", filters={"location":"United States","keyword": "intern"})
greenhouse_scraper("airbnb", filters={"location":"United States","keyword": "intern"})
greenhouse_scraper("asana", filters={"location":"United States","keyword": "intern"})
greenhouse_scraper("cloverhealth", filters={"location":"United States","keyword": "intern"})
greenhouse_scraper("databricks", filters={"location":"United States", "keyword": "intern"})
