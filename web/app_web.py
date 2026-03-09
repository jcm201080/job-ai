from flask import Flask, render_template
import sqlite3
import sys
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from app import main
from ai.job_matcher import calculate_match
from ai.market_analyzer import analyze_market, missing_skills

app = Flask(__name__, template_folder="../templates", static_folder="../static")

DB_PATH = os.path.join(BASE_DIR, "database", "jobs.db")


def get_jobs():

    from database.db import create_table
    create_table()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT title, company, url, description
    FROM jobs
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    jobs = []

    for job in rows:

        title = job[0]
        company = job[1]
        url = job[2]
        description = job[3]

        match = calculate_match(title, description)

        jobs.append({
            "title": title,
            "company": company,
            "url": url,
            "match": match
        })

    conn.close()

    jobs = sorted(jobs, key=lambda x: x["match"], reverse=True)

    return jobs


@app.route("/")
def home():

    jobs = get_jobs()

    market = analyze_market(jobs)
    missing = missing_skills(market)

    return render_template(
        "jobs.html",
        jobs=jobs,
        missing=missing
    )


@app.route("/update")
def update_jobs():

    subprocess.Popen(["python3", "app.py"], cwd=BASE_DIR)

    return "<h2>Scraper lanzado 👍</h2><a href='/job-ai/'>Volver</a>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8010, debug=True)