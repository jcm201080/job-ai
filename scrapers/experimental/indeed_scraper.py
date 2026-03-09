import requests
from bs4 import BeautifulSoup
from models.job import Job


def search_indeed(keyword="python"):

    jobs = []

    url = f"https://www.indeed.com/jobs?q={keyword}&l=remote"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    offers = soup.select("div.job_seen_beacon")

    for offer in offers:

        title_tag = offer.select_one("h2.jobTitle")

        if not title_tag:
            continue

        title = title_tag.text.strip()

        company_tag = offer.select_one("span.companyName")

        if company_tag:
            company = company_tag.text.strip()
        else:
            company = "Unknown"

        link_tag = offer.select_one("a")

        if not link_tag:
            continue

        link = link_tag.get("href")

        if not link:
            continue

        job_url = "https://www.indeed.com" + link

        job = Job(
            title=title,
            company=company,
            url=job_url,
            description=""
        )

        jobs.append(job)

    print(response.status_code)
    print(response.text[:500])
    return jobs