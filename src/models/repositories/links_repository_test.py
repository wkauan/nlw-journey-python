import pytest
import uuid
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interecao com o banco")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links_trip_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "http://localhost:5000/test"
    }
    links_repository.registry_link(links_trip_infos)

@pytest.mark.skip(reason="interecao com o banco")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links = links_repository.find_links_from_trip(trip_id)
    print()
    print(links)
