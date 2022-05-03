from datetime import datetime

def currentDate():
    return datetime.now().date().isoformat()
