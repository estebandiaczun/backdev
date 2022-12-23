# models.py
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel

class Gender(str, Enum):
 male = "hombre"
 female = "mujer"
 otro = "otro"

class Roles(str, Enum):
 admin = "admin"
 user = "user"
 
class User(BaseModel):
 id: Optional[UUID] = uuid4()
 first_name: str
 last_name: str
 gender: Gender
 roles: List[Roles]