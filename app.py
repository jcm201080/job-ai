from agents.job_search_agent import JobSearchAgent
from database.db import create_table, save_job
from config import KEYWORDS


def main():

    create_table()

    agent = JobSearchAgent()

    for keyword in KEYWORDS:

        print(f"\n===== Buscando: {keyword} =====")

        jobs = agent.search(keyword)

        print("Trabajos encontrados:", len(jobs))

        for job in jobs:

            print("JOB:", job)

            save_job(job)


if __name__ == "__main__":
    main()