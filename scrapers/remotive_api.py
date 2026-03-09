import requests
from models.job import Job


def search_remotive(keyword="python"):

    url = "https://remotive.com/api/remote-jobs"

    response = requests.get(url)

    data = response.json()

    jobs = []

    for offer in data["jobs"]:

        title = offer["title"].lower()

        if keyword.lower() in title:

            job = Job(
                title=offer["title"],
                company=offer["company_name"],
                url=offer["url"],
                description=offer["description"]
            )

            jobs.append(job)

    return jobs[:10]