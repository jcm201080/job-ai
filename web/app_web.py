from flask import Flask, render_template
import sqlite3
import sys
import os
import sqlite3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import main

from ai.job_matcher import calculate_match
from ai.market_analyzer import analyze_market, missing_skills

app = Flask(__name__, template_folder="../templates", static_folder="../static")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "jobs.db")


def get_jobs():

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

    # 🔥 ordenar por compatibilidad
    jobs = sorted(jobs, key=lambda x: x["match"], reverse=True)

    return jobs

@app.route("/")
def home():

    jobs = get_jobs()

    # analizar mercado
    market = analyze_market(jobs)

    # detectar skills faltantes
    missing = missing_skills(market)

    return render_template(
        "jobs.html",
        jobs=jobs,
        missing=missing
    )

@app.route("/update")
def update_jobs():

    main()

    return "<h2>Scraper ejecutado 👍</h2><a href='/'>Volver</a>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8010, debug=True)