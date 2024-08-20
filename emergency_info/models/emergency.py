from typing import List, Dict
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class BloodTypes(Enum):
    a_pos = 'A+'
    a_neg = 'A-'
    b_pos = 'B+'
    b_neg = 'B-'
    ab_pos = 'A+'
    ab_neg = 'A-'
    o_pos = 'O+'
    o_neg = 'O-'


class EmergencyInfo(BaseModel):
    blood_type: BloodTypes | None = None


class EmergencyLocation(BaseModel):
    location_name: str
    location_coords: List = []
    trailhead: str
    instructions: str | List[str] = None


class Emergency(BaseModel):
    id: int
    patients: str | List[str] = None
    log: Dict = {}
    emergency_info: EmergencyInfo




