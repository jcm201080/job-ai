import requests
from models.job import Job


BASE_URL = "https://www.infojobs.net/webapp/offers/search"


def search_infojobs(keyword="python", page=1):

    params = {
        "keyword": keyword,
        "searchByType": "country",
        "countryIds": 17,
        "page": page,
        "sortBy": "RELEVANCE"
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    response = requests.get(BASE_URL, params=params, headers=headers)

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text[:500])
    data = response.json()

    jobs = []

    for item in data.get("offers", [])[:10]:

        link = item.get("link", "")
        if link.startswith("//"):
            link = "https:" + link

        job = Job(
            title=item.get("title"),
            company=item.get("companyName"),
            url=link,
            description=item.get("description", "")
        )

        jobs.append(job)

    return jobs