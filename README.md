# 🎓 GradPathway API

GradPathway is a RESTful API that helps international students discover and compare master's degree programmes worldwide.  
It allows users to upload their academic transcript or GPA and receive tailored programme recommendations based on eligibility, preferences, and programme data.

---

## 🚀 Features

### 👤 Accounts
- Register and log in using token-based authentication.
- Manage profile and preferred countries.

### 🏫 Catalog
- View and search universities and programmes.
- Data seeded from the **U.S. College Scorecard API** for American institutions.

### 📄 Transcripts & Matching
- Submit transcripts or GPA information.
- Rule-based recommendation engine (prototype) that suggests eligible programmes.

### ⭐ Favourites
- Save and manage favourite programmes.
- Each user sees only their own favourites.

### 🔒 Permissions
- Secure endpoints: only authenticated users can create or modify resources.

### ⚙️ Admin Panel
- Add or update universities and programmes manually.

---

## 🧱 Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend Framework** | Django 5 + Django REST Framework |
| **Database** | PostgreSQL (Heroku Postgres) |
| **Authentication** | Token-based via `rest_framework.authtoken` |
| **API Docs** | Swagger / drf-yasg |
| **Hosting** | Heroku |
| **External API** | U.S. Department of Education College Scorecard API |

---

## 🧩 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|-----------|-------------|
| `POST` | `/api/auth/register/` | Register a new user |
| `POST` | `/api/auth/login/` | Obtain auth token |

### Catalog
| Method | Endpoint | Description |
|--------|-----------|-------------|
| `GET` | `/api/catalog/universities/` | List or create universities |
| `GET` | `/api/catalog/programmes/` | List or create programmes |
| `GET` | `/api/catalog/programmes/<id>/` | Programme details |

### Favourites
| Method | Endpoint | Description |
|--------|-----------|-------------|
| `POST` | `/api/favourites/` | Add a favourite programme |
| `DELETE` | `/api/favourites/<id>/` | Remove a favourite |

---

## 🧠 How It Works

1. A new user registers and logs in to obtain a token.  
2. The user browses available universities and programmes.  
3. The user can:
   - Upload a transcript (coming in Week 3 implementation).
   - Add favourites for quick access later.  
4. The system provides programme details including tuition, duration, and GPA requirements.  
5. Admins can seed U.S. university data via the College Scorecard API.

---

## 🧰 Installation (for local development)

```bash
git clone https://github.com/pdadzie/gradpathway_api.git
cd gradpathway_api
python -m venv venv
source venv/bin/activate   
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
