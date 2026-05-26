# 🌿 Breathe ESG Carbon Tracking System

[![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-blue?logo=render)](https://breathe-esg-carbon-tracking-3.onrender.com/)
[![Django Version](https://img.shields.io/badge/Django-6.0.5-green)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A production-ready **multi-tenant carbon emissions data ingestion, normalization, and review system** built for the Breathe ESG Tech Intern Assignment. It handles real-world SAP data with German headers, calculates tCO2e emissions, and provides a complete audit trail and review workflow.

---

## 🚀 Live Demo

| Interface | URL |
|-----------|-----|
| **Welcome Page** | [https://breathe-esg-carbon-tracking-3.onrender.com/](https://breathe-esg-carbon-tracking-3.onrender.com/) |
| **Admin Panel** | [https://breathe-esg-carbon-tracking-3.onrender.com/admin/](https://breathe-esg-carbon-tracking-3.onrender.com/admin/) |
| **API Root** | [https://breathe-esg-carbon-tracking-3.onrender.com/api/](https://breathe-esg-carbon-tracking-3.onrender.com/api/) |
| **Normalized Records** | [https://breathe-esg-carbon-tracking-3.onrender.com/api/normalized-records/](https://breathe-esg-carbon-tracking-3.onrender.com/api/normalized-records/) |

**Demo Login Credentials**
- **Username:** `admin`
- **Password:** `admin123`

---

## 📊 Key Features

- **Multi-tenant Architecture** – Separate data per organization.
- **SAP Data Ingestion** – Parses CSV exports with **German headers** (`Menge`, `ME`, `Datum`).
- **Automatic Normalization** – Converts activity data to standard units (kg, kWh) and calculates **tCO2e** using configurable emission factors.
- **Review Workflow** – Approve or flag records with full audit trail.
- **REST API** – Fully browsable API built with Django REST Framework.
- **Professional Admin Panel** – Django admin with custom configurations.
- **Live Dashboard** – Welcome page shows real-time statistics (record count, total tCO2e).

---

## 🛠️ Technology Stack

- **Backend:** Django 6.0.5, Django REST Framework
- **Database:** SQLite (development) / PostgreSQL (production)
- **Deployment:** Render.com (free tier)
- **Server:** Gunicorn
- **Static Files:** WhiteNoise
- **Version Control:** Git & GitHub

---

## 🏗️ Data Model

The system uses six core tables:

| Table | Purpose |
|-------|---------|
| `Organization` | Multi-tenant tenant setup. |
| `DataSource` | Tracks source type (SAP/UTILITY/TRAVEL) and ingestion method. |
| `RawEmissionRecord` | Stores original ingested data as JSON. |
| `NormalizedEmissionRecord` | Stores normalized data with calculated `tCO2e`. |
| `ReviewStatus` | Manages the approval workflow (PENDING, APPROVED, FLAGGED, REJECTED). |
| `AuditLog` | Complete history of all changes. |

Detailed schema is available in [`MODEL.md`](MODEL.md).

---

## 📂 Documentation

All decision-making and research are documented in the repository:

- [`MODEL.md`](MODEL.md) – Complete database schema design.
- [`DECISIONS.md`](DECISIONS.md) – Key architectural choices and tradeoffs.
- [`TRADEOFFS.md`](TRADEOFFS.md) – What was intentionally not built and why.
- [`SOURCES.md`](SOURCES.md) – Research on SAP, Utility, and Travel data formats.

---

## 🔧 Local Development Setup

### Prerequisites
- Python 3.13+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/breathe-esg-carbon-tracking.git
   cd breathe-esg-carbon-tracking


2.  Create and activate a virtual environment

  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
  pip install -r requirements.txt

4.Run migrations
  python manage.py migrate

5. Create a superuser
   python manage.py createsuperuser

6. Start the development server
  python manage.py runserver


7. Access the application
   Admin panel: http://127.0.0.1:8000/admin/
   API root: http://127.0.0.1:8000/api/

Testing the SAP Data Ingestion
A sample SAP file is included. Upload it using the API endpoint:

curl -X POST http://127.0.0.1:8000/api/upload/1/SAP/ -F "file=@sample_sap.csv"

🌐 Deployment on Render
The project is configured for one-click deployment on Render.com.

Push the code to a GitHub repository.

Create a new Web Service on Render and connect the repository.

Use the following settings:

Build Command: ./build.sh

Start Command: gunicorn breathe_esg.wsgi:application

Add environment variables:

PYTHON_VERSION=3.13.2

DJANGO_SECRET_KEY (Generate one)

Render will automatically run migrations and collect static files.

🧪 Sample API Responses
GET /api/normalized-records/

json
[
    {
        "id": 1,
        "scope": 1,
        "category": "fuel_combustion",
        "activity_value": "15000.500000",
        "unit": "kg",
        "calculated_emissions": "0.037501",
        "period_start": "2024-01-01",
        "period_end": "2024-12-31"
    }
]
GET /api/dashboard/1/

json
{
    "organization_id": 1,
    "summary": {
        "pending": 0,
        "flagged": 0,
        "approved": 6,
        "rejected": 0,
        "total": 6
    }
}
📁 Project Structure
text
breathe-esg-carbon-tracking/
├── breathe_esg/           # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── ingestion/             # Main application
│   ├── models.py          # All database models
│   ├── admin.py           # Admin interface registration
│   ├── serializers.py     # API serializers
│   ├── views.py           # API viewsets
│   ├── upload_views.py    # File upload endpoints
│   ├── normalization_views.py
│   ├── review_views.py
│   └── urls.py
├── templates/             # Custom HTML templates
├── staticfiles/           # Collected static files
├── requirements.txt       # Python dependencies
├── build.sh              # Render build script
├── render.yaml           # Render configuration
└── sample_sap.csv        # Test data
📞 Submission
This project was submitted as part of the Breathe ESG Tech Intern Assignment (May 2026).

Submitted by: [Eerla Venkatesh]

Email: [venkatesheerla799@gmail.com]

Deployed URL: https://breathe-esg-carbon-tracking-3.onrender.com

GitHub Repository: https://github.com/EERLA-VENKATESH/breathe-esg-carbon-tracking

👏 Acknowledgments
Built with Django and Django REST Framework

Deployed on Render.com free tier

Inspired by real-world ESG reporting requirements

📄 License
This project is for demonstration purposes as part of a job application assignment.

Made with ❤️ for Breathe ESG

text

---

### How to Add This `README.md` to Your Project

1.  On your local computer, navigate to your project folder: `cd D:\breathe-esg`
2.  Open a new file named `README.md` in Notepad: `notepad README.md`
3.  **Copy the entire template above** and paste it into Notepad.
4.  **Fill in the bracketed `[ ]` sections** with your actual name, email, and any other personal details you want to include.
5.  Save the file (`Ctrl+S`) and close Notepad.
6.  Run the following commands in your terminal to push the new `README.md` to GitHub:

```bash
git add README.md
git commit -m "Add professional README.md"
git push origin master
