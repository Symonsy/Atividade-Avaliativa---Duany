from pydantic import BaseModel, Field
from typing import Optional, Literal
from uuid import UUID
from datetime import datetime

StatusType = Literal["Planejado", "Em Andamento", "Concluído", "Cancelado"]

class ProjectBase(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    priority: Literal[1, 2, 3]
    status: StatusType

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: UUID
    created_at: datetime
