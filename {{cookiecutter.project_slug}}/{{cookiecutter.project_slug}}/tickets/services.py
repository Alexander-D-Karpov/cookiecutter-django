from django.core.cache import cache
from rest_framework.exceptions import NotFound


def get_ticket_data(uuid: str):
    t = cache.get(uuid)
    if t is None:
        raise NotFound(
            detail={
                "name": "not found",
                "current": 0,
                "max": 0,
                "next": None,
            }
        )
    data = cache.get_many(
        [f"{uuid}-max", f"{uuid}-current", f"{uuid}-name", f"{uuid}-next"]
    )
    return {
        "name": data[f"{uuid}-name"],
        "current": data[f"{uuid}-current"],
        "max": data[f"{uuid}-max"],
        "next": data[f"{uuid}-next"],
    }


def increase_ticket(uuid: str):
    cache.incr(f"{uuid}-current", 1)
