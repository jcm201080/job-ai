import requests
from bs4 import BeautifulSoup
from models.job import Job


def search_infojobs(keyword="python"):
    url = f"https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword={keyword}"

    response = requests.get(url)
    print(response.status_code)
    print(response.text[:1000])
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for item in soup.select("a.ij-OfferCardContent-description-title-link")[:10]:

        title = item.text.strip()
        job_url = "https://www.infojobs.net" + item["href"]

        job = Job(
            title=title,
            company="Unknown",
            url=job_url,
            description=""
        )

        jobs.append(job)

    return jobs