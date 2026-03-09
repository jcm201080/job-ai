import fitz

KNOWN_SKILLS = [
    "python",
    "flask",
    "fastapi",
    "sql",
    "docker",
    "linux",
    "pandas",
    "spark",
    "machine learning",
    "ai",
    "javascript",
    "html",
    "css",
    "git",
    "api",
    "backend",
    "data"
]


def extract_text_from_pdf(path):

    doc = fitz.open(path)

    text = ""

    for page in doc:
        text += page.get_text()

    return text.lower()


def detect_skills(text):

    skills_found = []

    for skill in KNOWN_SKILLS:

        if skill in text:
            skills_found.append(skill)

    return skills_found


def analyze_cv(path):

    text = extract_text_from_pdf(path)

    skills = detect_skills(text)

    return skills