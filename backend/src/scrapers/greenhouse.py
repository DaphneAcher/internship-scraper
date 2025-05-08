import requests
import json
import re

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

        keyword_patterns = []

        if "keywords" in filters:
            for keyword in filters["keywords"]:
                keyword = keyword.lower()

                if keyword == "intern":
                    # Special pattern: match intern, internship, internships, interning
                    pattern = re.compile(r'\bintern(ship|ships|ing)?\b', re.IGNORECASE)
                else:
                    # For other keywords, match the full word
                    pattern = re.compile(rf'\b{re.escape(keyword)}\b', re.IGNORECASE)

                keyword_patterns.append(pattern)


        keyword_match = True
        if keyword_patterns:
            keyword_match = all(regex_patt.search(job["title"]) for regex_patt in keyword_patterns)


        if keyword_match and location_match:    
            print(company, job["title"], "-", job["location"]["name"])

    
greenhouse_scraper("spacex", filters={"keywords": ["intern","engineering"]})    
greenhouse_scraper("robinhood", filters={"keywords": ["intern"]})
greenhouse_scraper("notion", filters={"keywords": ["intern"]})
greenhouse_scraper("stripe", filters={"keywords": ["intern"]})
greenhouse_scraper("airbnb", filters={"keywords": ["intern"]})
greenhouse_scraper("asana", filters={"keywords": ["intern"]})
greenhouse_scraper("cloverhealth", filters={"keywords": ["intern"]})
greenhouse_scraper("databricks", filters={"keywords": ["intern"]})

 