from fastapi import FastAPI, HTTPException
from .models import Report

app = FastAPI()
_reports = {}

@app.post("/reports", response_model=Report)
def create_report(report: Report):
    if report.id in _reports:
        raise HTTPException(status_code=400, detail="Report already exists")
    _reports[report.id] = report
    return report

@app.get("/reports/{report_id}", response_model=Report)
def get_report(report_id: int):
    if report_id not in _reports:
        raise HTTPException(status_code=404, detail="Report not found")
    return _reports[report_id]
