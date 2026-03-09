from user_profile.profile_data import PROFILE


def calculate_match(title, description):

    text = (title + " " + description).lower()

    score = 0

    for skill in PROFILE["skills"]:

        if skill in text:
            score += 15

    # bonus por Python backend
    if "python" in text and "backend" in text:
        score += 20

    # bonus por data
    if "data" in text:
        score += 10

    return min(score, 100)