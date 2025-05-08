import requests
import json
import re

def job_type(title):
    title = title.lower()
    if re.search(r'\bintern(ship|ships|ing)?\b', title) or re.search(r'\bco[- ]?op\b', title):
        return "internship"
    elif re.search(r'\bnew grad(uate)?\b', title) or re.search(r'\bearly career\b', title):
        return "new grad"
    else:
        return "other"


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

        classify = job_type(job["title"])
        if classify == "other":
            continue
        
        location_match = True
        if "location" in filters:
            location_match = filters["location"].lower() in job["location"]["name"].lower()

        keyword_patterns = []

        if "keywords" in filters:
          for keyword in filters["keywords"]:
              keyword = keyword.lower()
              pattern = re.compile(rf'\b{re.escape(keyword)}\b', re.IGNORECASE)
              keyword_patterns.append(pattern)

              


        keyword_match = True
        if keyword_patterns:
            keyword_match = all(regex_patt.search(job["title"]) for regex_patt in keyword_patterns)


        if keyword_match and location_match:    
             print(f"{company} | {classify.upper()} | {job['title']} - {job['location']['name']}")
             job_details_url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs/{job['id']}"
             job_details = requests.get(job_details_url).json()
             description = job_details.get("description", "[No description provided]")
             print("DESCRIPTION:\n", description)
             print("LINK:", job.get("absolute_url", "[No link found]"))
             print("-" * 80)


    
# greenhouse_scraper("spacex", filters={"keywords": ["intern","engineering"]})    
# greenhouse_scraper("robinhood", filters={"keywords": ["intern"]})
greenhouse_scraper("notion", filters={"location":"New York", "keywords": ["market"]})
greenhouse_scraper("stripe", filters={"keywords": ["engineer"]})
greenhouse_scraper("airbnb", filters=None)
greenhouse_scraper("asana", filters=None)
# greenhouse_scraper("cloverhealth", filters={"keywords": ["intern"]})
# greenhouse_scraper("databricks", filters={"keywords": ["intern"]})

 