import requests
from models.job import Job


def search_hackernews(keyword="python"):

    jobs = []

    url = "https://hacker-news.firebaseio.com/v0/jobstories.json"

    ids = requests.get(url).json()

    for job_id in ids[:200]:

        item = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{job_id}.json"
        ).json()

        if not item:
            continue

        title = item.get("title", "")
        text = item.get("text", "")

        if keyword.lower() not in (title + text).lower():
            continue

        job = Job(
            title=title,
            company="HackerNews",
            url=item.get("url", ""),
            description=text
        )

        jobs.append(job)

    return jobs