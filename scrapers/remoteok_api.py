import requests
from models.job import Job


def search_remoteok(keyword="python"):

    url = "https://remoteok.com/api"

    response = requests.get(url)

    data = response.json()

    jobs = []

    for offer in data:

        title = offer.get("position", "")

        if keyword.lower() in title.lower():

            job = Job(
                title=title,
                company=offer.get("company"),
                url=offer.get("url"),
                description=offer.get("description", "")
            )

            jobs.append(job)

    return jobs[:10]