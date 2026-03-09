from user_profile.profile_data import PROFILE

COMMON_SKILLS = [
    "python",
    "flask",
    "fastapi",
    "docker",
    "kubernetes",
    "aws",
    "redis",
    "sql",
    "postgres",
    "mongodb",
    "spark",
    "pandas",
    "machine learning",
    "ai"
]

def analyze_market(jobs):

    skill_counter = {}

    for job in jobs:

        text = (job["title"] + " " + job.get("description", "")).lower()

        for skill in COMMON_SKILLS:

            if skill in text:

                skill_counter[skill] = skill_counter.get(skill, 0) + 1

    return skill_counter


def missing_skills(market):

    missing = []

    for skill in market:

        if skill not in PROFILE["skills"]:
            missing.append(skill)

    return missing