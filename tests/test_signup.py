def test_signup_valid_student(client):
    """Test successful signup for an activity"""
    # Arrange
    activity = "Chess%20Club"
    email = "newstudent@mergington.edu"
    
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    result = response.json()
    
    # Assert
    assert response.status_code == 200
    assert "Signed up" in result["message"]
    assert email in result["message"]


def test_signup_nonexistent_activity(client):
    """Test signup for non-existent activity returns 404"""
    # Arrange
    activity = "NonExistent"
    email = "student@mergington.edu"
    
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    result = response.json()
    
    # Assert
    assert response.status_code == 404
    assert "Activity not found" in result["detail"]


def test_signup_duplicate_student(client):
    """Test signup fails when student is already registered"""
    # Arrange
    activity = "Chess%20Club"
    email = "michael@mergington.edu"  # Already signed up
    
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    result = response.json()
    
    # Assert
    assert response.status_code == 400
    assert "already signed up" in result["detail"]


def test_signup_adds_participant_to_list(client):
    """Test that signup adds participant to activities participant list"""
    # Arrange
    activity = "Chess%20Club"
    new_email = "participant@mergington.edu"
    
    # Act
    client.post(f"/activities/{activity}/signup?email={new_email}")
    response = client.get("/activities")
    updated_participants = response.json()["Chess Club"]["participants"]
    
    # Assert
    assert new_email in updated_participants
