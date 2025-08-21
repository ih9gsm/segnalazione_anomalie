from fastapi import FastAPI, HTTPException

from .models import AppSettings, Report, ReportCreate, SMTPSettings, User
from .report_utils import generate_docx, generate_pdf, send_email

app = FastAPI()

_reports = {}
_users = {}
_settings = AppSettings(logo_path=None, smtp=SMTPSettings(server="localhost", port=1025, use_tls=False))


@app.post("/reports", response_model=Report)
def create_report(report: ReportCreate):
    if report.id in _reports:
        raise HTTPException(status_code=400, detail="Report already exists")
    stored = Report(id=report.id, description=report.description)
    _reports[report.id] = stored
    pdf = generate_pdf(stored.description, _settings.logo_path)
    docx_bytes = generate_docx(stored.description, _settings.logo_path)
    if report.recipients:
        send_email(
            _settings.smtp,
            subject=f"Report {stored.id}",
            body=stored.description,
            recipients=report.recipients,
            attachments=[(f"report_{stored.id}.pdf", pdf), (f"report_{stored.id}.docx", docx_bytes)],
        )
    return stored


@app.get("/reports/{report_id}", response_model=Report)
def get_report(report_id: int):
    if report_id not in _reports:
        raise HTTPException(status_code=404, detail="Report not found")
    return _reports[report_id]


@app.post("/users", response_model=User)
def create_user(user: User):
    if user.username in _users:
        raise HTTPException(status_code=400, detail="User already exists")
    _users[user.username] = user
    return user


@app.get("/users/{username}", response_model=User)
def get_user(username: str):
    if username not in _users:
        raise HTTPException(status_code=404, detail="User not found")
    return _users[username]


@app.get("/settings", response_model=AppSettings)
def get_settings():
    return _settings


@app.put("/settings", response_model=AppSettings)
def update_settings(settings: AppSettings):
    global _settings
    _settings = settings
    return _settings
