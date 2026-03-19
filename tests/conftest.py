from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def isolate_activities_state():
    """Reset in-memory activities before each test to keep tests independent."""
    snapshot = deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(snapshot)


@pytest.fixture
def client():
    return TestClient(app_module.app)
