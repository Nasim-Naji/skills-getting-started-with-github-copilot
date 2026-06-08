def test_get_activities_returns_all_activities(client):
    """Test that GET /activities returns all 9 activities"""
    # Arrange
    expected_activity_count = 9
    
    # Act
    response = client.get("/activities")
    activities = response.json()
    
    # Assert
    assert response.status_code == 200
    assert len(activities) == expected_activity_count


def test_activities_have_correct_structure(client):
    """Test that activities have all required fields"""
    # Arrange
    required_fields = ["description", "schedule", "max_participants", "participants"]
    
    # Act
    response = client.get("/activities")
    activities = response.json()
    chess_club = activities["Chess Club"]
    
    # Assert
    for field in required_fields:
        assert field in chess_club
    assert isinstance(chess_club["participants"], list)


def test_activities_have_initial_participants(client):
    """Test that activities are populated with initial participants"""
    # Arrange
    expected_participant = "michael@mergington.edu"
    
    # Act
    response = client.get("/activities")
    activities = response.json()
    chess_club_participants = activities["Chess Club"]["participants"]
    
    # Assert
    assert len(chess_club_participants) >= 1
    assert expected_participant in chess_club_participants
