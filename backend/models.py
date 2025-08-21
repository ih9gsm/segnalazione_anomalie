from typing import List, Optional
from pydantic import BaseModel, Field


class Report(BaseModel):
    id: int = Field(..., ge=0)
    description: str


class ReportCreate(Report):
    recipients: List[str] = []


class User(BaseModel):
    username: str
    email: str
    role: str = "manutentore"


class SMTPSettings(BaseModel):
    server: str
    port: int = 587
    username: Optional[str] = None
    password: Optional[str] = None
    use_tls: bool = True


class AppSettings(BaseModel):
    logo_path: Optional[str] = None
    smtp: SMTPSettings
