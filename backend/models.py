from pydantic import BaseModel, Field

class Report(BaseModel):
    id: int = Field(..., ge=0)
    description: str
