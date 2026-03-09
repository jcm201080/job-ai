from playwright.sync_api import sync_playwright
from models.job import Job


def search_infojobs(keyword="python"):

    jobs = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        url = f"https://www.infojobs.net/ofertas-trabajo?keyword={keyword}"

        page.goto(url)

        page.wait_for_timeout(5000)

        offers = page.query_selector_all("a[data-testid='offer-title']")

        print("Ofertas detectadas:", len(offers))

        for offer in offers[:10]:

            title = offer.inner_text().strip()
            href = offer.get_attribute("href")

            if href.startswith("http"):
                job_url = href
            else:
                job_url = "https://www.infojobs.net" + href

            job = Job(
                title=title,
                company="InfoJobs",
                url=job_url,
                description=""
            )

            jobs.append(job)

        browser.close()

    return jobs