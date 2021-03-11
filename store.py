from datetime import datetime

from settings import WAIT_MINUTES_BEFORE_REINFORMING

__all__ = [
    "add_informed_person", "should_inform_person"
]

# This dict holds all people that have been informed.
informed_people = {}


def add_informed_person(identifier: str) -> None:
    informed_people[identifier] = datetime.now()
    

def should_inform_person(identifier: str) -> bool:
    if value := informed_people.get(identifier):
        now = datetime.now()
        write_time = value
        diff = (now - write_time).total_seconds() / 60
        
        if diff < WAIT_MINUTES_BEFORE_REINFORMING:
            return False
    
    return True
