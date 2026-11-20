# Демо-хранилище в оперативной памяти
TICKETS = []
NEXT_ID = 1

def get_all():
    return TICKETS

def add(title, description, priority):
    global NEXT_ID
    ticket = {
        "id": NEXT_ID,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "Новая"
    }
    TICKETS.append(ticket)
    NEXT_ID += 1
    return ticket

def get_by_id(ticket_id):
    for t in TICKETS:
        if t["id"] == ticket_id:
            return t
    return None
