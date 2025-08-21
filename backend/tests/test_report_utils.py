import smtplib

from backend.report_utils import generate_docx, generate_pdf, send_email
from backend.models import SMTPSettings


def test_generate_pdf_contains_pdf_header():
    data = generate_pdf("hello")
    assert data.startswith(b"%PDF")


def test_generate_docx_is_zip():
    data = generate_docx("hello")
    assert data[:2] == b"PK"


def test_send_email(monkeypatch):
    sent = {}

    class DummySMTP:
        def __init__(self, server, port):
            sent["server"] = server
            sent["port"] = port
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc, tb):
            pass
        def starttls(self):
            sent["tls"] = True
        def login(self, username, password):
            sent["login"] = (username, password)
        def send_message(self, message):
            sent["to"] = message["To"]

    monkeypatch.setattr(smtplib, "SMTP", DummySMTP)
    settings = SMTPSettings(server="smtp.example.com", username="user", password="pass")
    send_email(settings, "Subject", "Body", ["a@example.com"])
    assert sent["server"] == "smtp.example.com"
    assert sent["to"] == "a@example.com"
