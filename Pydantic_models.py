from pydantic import BaseModel
from typing import List, Optional

# Syntax for creating a child class is
# class child_class(parent_class):
class User(BaseModel):
    username: str
    password: str
    comments: List[str]
    contact_info: Optional


