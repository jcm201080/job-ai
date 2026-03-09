import sqlite3


DB_PATH = "database/jobs.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        company TEXT,
        url TEXT UNIQUE,
        description TEXT,
        source TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


#Función para guardar trabajos
def save_job(job):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT INTO jobs (title, company, url, description, source)
        VALUES (?, ?, ?, ?, ?)
        """, (
            job.title,
            job.company,
            job.url,
            job.description,
            "remotive"
        ))

        conn.commit()

        print("💾 Guardando:", job.title)

    except sqlite3.IntegrityError:

        print("⚠️ Ya existe:", job.title)

    conn.close()