from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class Student:
    student_id: int
    name: str
    branch: str
    cgpa: float

def tuple_to_dict(tup: tuple, keys: list) -> Dict[str, Any]:
    """Converts a tuple of values into a dictionary using provided keys."""
    return dict(zip(keys, tup))

def object_to_dict(obj: Any) -> Dict[str, Any]:
    """Converts custom object/dataclass to dictionary."""
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    return {}

if __name__ == "__main__":
    # Example 1: Tuple to Dict
    raw_record = (101, "Vedanshi Agrawal", "CSE", 8.0)
    keys = ["id", "name", "department", "cgpa"]
    print("Converted Tuple to Dict:", tuple_to_dict(raw_record, keys))

    # Example 2: Dataclass to Dict
    student = Student(102, "Vedanshi", "Computer Science", 8.0)
    print("Converted Object to Dict:", object_to_dict(student))
