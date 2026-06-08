import pytest
from fastapi.testclient import TestClient
from src import app as app_module


@pytest.fixture
def client():
    """Provides a TestClient instance with fresh app data for each test"""
    # Reset activities to initial state before each test
    initial_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Soccer Team": {
            "description": "Competitive soccer team practicing skills and teamwork",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 22,
            "participants": ["liam@mergington.edu", "noah@mergington.edu"]
        },
        "Basketball Club": {
            "description": "Pickup games and drills to improve basketball fundamentals",
            "schedule": "Mondays and Wednesdays, 5:00 PM - 6:30 PM",
            "max_participants": 18,
            "participants": ["ava@mergington.edu", "sophia@mergington.edu"]
        },
        "Art Club": {
            "description": "Explore painting, drawing, and other visual arts",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": ["isabella@mergington.edu"]
        },
        "Drama Club": {
            "description": "Acting, stagecraft, and school theater productions",
            "schedule": "Wednesdays, 4:00 PM - 6:00 PM",
            "max_participants": 25,
            "participants": ["elijah@mergington.edu"]
        },
        "Science Club": {
            "description": "Hands-on experiments and science fair projects",
            "schedule": "Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["mia@mergington.edu"]
        },
        "Debate Team": {
            "description": "Practice public speaking and competitive debate",
            "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["benjamin@mergington.edu"]
        }
    }
    
    # Clear and repopulate the module-level activities dictionary
    app_module.activities.clear()
    app_module.activities.update(initial_activities)
    
    return TestClient(app_module.app)
