import requests
from bs4 import BeautifulSoup
from models.job import Job


def search_wework(keyword="python"):

    jobs = []

    url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"

    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    offers = soup.select("section.jobs li")

    for offer in offers:

        link = offer.find("a", href=True)

        if not link:
            continue

        company = offer.select_one(".company")
        title = offer.select_one(".title")

        if not title:
            continue

        title = title.text.strip()

        if company:
            company = company.text.strip()
        else:
            company = "Unknown"

        job_url = "https://weworkremotely.com" + link["href"]

        job = Job(
            title=title,
            company=company,
            url=job_url,
            description=""
        )

        jobs.append(job)

    return jobs