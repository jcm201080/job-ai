from playwright.sync_api import sync_playwright
from models.job import Job


def search_infojobs(keyword="python"):

    jobs = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context()
        page = context.new_page()

        # abrir la web normal primero
        page.goto("https://www.infojobs.net")

        page.wait_for_timeout(5000)

        api_url = f"https://www.infojobs.net/webapp/offers/search?keyword={keyword}&countryIds=17&page=1&sortBy=RELEVANCE"

        response = context.request.get(api_url)

        print("STATUS:", response.status)

        if response.status != 200:
            print("Bloqueado por InfoJobs")
            browser.close()
            return []

        data = response.json()

        offers = data.get("offers", [])

        print("Ofertas detectadas:", len(offers))

        for offer in offers[:10]:

            link = offer.get("link", "")

            if link.startswith("//"):
                link = "https:" + link

            job = Job(
                title=offer.get("title"),
                company=offer.get("companyName"),
                url=link,
                description=offer.get("description", "")
            )

            jobs.append(job)

        browser.close()

    return jobs