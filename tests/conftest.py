import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from app.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client
