from scrapers.remotive_api import search_remotive
from scrapers.remoteok_api import search_remoteok
from scrapers.hackernews_api import search_hackernews


class JobSearchAgent:

    def search(self, keyword):

        print(f"🔎 Searching jobs for: {keyword}")

        jobs = []

        r = search_remotive(keyword)
        print("Remotive:", len(r))
        jobs += r

        r = search_remoteok(keyword)
        print("RemoteOK:", len(r))
        jobs += r

        r = search_hackernews(keyword)
        print("HackerNews:", len(r))
        jobs += r

        print("Total encontrados:", len(jobs))

        return jobs