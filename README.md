job_ai
│
├── agents
│   └── job_search_agent.py
│
├── ai
│   ├── job_matcher.py
│   └── market_analyzer.py
│
├── cv_analysis
│   └── analyze_cv.py
│
├── scrapers
│   ├── remotive_api.py
│   ├── remoteok_api.py
│   └── hackernews_api.py
│
├── database
│   └── jobs.db
│
├── profile
│   └── profile_data.py
│
├── templates
│   └── jobs.html
│
├── web
│   └── app_web.py
│
├── app.py
├── config.py

Cada parte tiene una responsabilidad clara.

📦 Qué hace cada módulo
scrapers/

Se encarga de extraer ofertas de sitios web.

Ejemplo:

InfoJobs
LinkedIn
agents/

Aquí vive la lógica inteligente.

job_search_agent

busca ofertas

job_analyzer_agent

analiza si encajan contigo

job_apply_agent

genera candidatura
database/

Guarda las ofertas.

models/

Define la estructura de un trabajo.

app.py

Es el orquestador del sistema.



# Job AI

AI-powered system to search and analyze job offers automatically.

Features:
- Job scraping
- AI job analysis
- Automated applications