import pytest
from pydantic import ValidationError
from backend.models import Report

def test_report_model_valid():
    report = Report(id=1, description="Anomaly")
    assert report.id == 1
    assert report.description == "Anomaly"

def test_report_model_invalid_id():
    with pytest.raises(ValidationError):
        Report(id=-1, description="Invalid")
