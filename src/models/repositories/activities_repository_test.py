import pytest
import uuid
from .activities_repository import ActivitiesRepository
from src.models.settings.db_connection_handler import db_connection_handler
from datetime import datetime

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interecao com o banco")
def test_registry_activity():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activity_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "title": "Academia",
        "occurs_at": datetime.strptime("02-01-2024 08:30", "%d-%m-%Y %H:%M")
    }
    activities_repository.registry_activity(activity_infos)

@pytest.mark.skip(reason="interecao com o banco")
def test_find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activities = activities_repository.find_activities_from_trip(trip_id)
    print()
    print(activities)
