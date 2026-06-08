def test_unregister_valid_student(client):
    """Test successful unregister from an activity"""
    # Arrange
    activity = "Chess%20Club"
    email = "michael@mergington.edu"
    
    # Act
    response = client.post(f"/activities/{activity}/unregister?email={email}")
    result = response.json()
    
    # Assert
    assert response.status_code == 200
    assert "Unregistered" in result["message"]


def test_unregister_nonexistent_activity(client):
    """Test unregister from non-existent activity returns 404"""
    # Arrange
    activity = "NonExistent"
    email = "student@mergington.edu"
    
    # Act
    response = client.post(f"/activities/{activity}/unregister?email={email}")
    result = response.json()
    
    # Assert
    assert response.status_code == 404
    assert "Activity not found" in result["detail"]


def test_unregister_not_registered_student(client):
    """Test unregister fails when student is not registered"""
    # Arrange
    activity = "Chess%20Club"
    email = "notregistered@mergington.edu"
    
    # Act
    response = client.post(f"/activities/{activity}/unregister?email={email}")
    result = response.json()
    
    # Assert
    assert response.status_code == 400
    assert "not signed up" in result["detail"]


def test_unregister_removes_participant_from_list(client):
    """Test that unregister removes participant from activities participant list"""
    # Arrange
    activity = "Chess%20Club"
    email = "michael@mergington.edu"
    
    # Verify email is in list before unregister
    response_before = client.get("/activities")
    assert email in response_before.json()["Chess Club"]["participants"]
    
    # Act
    client.post(f"/activities/{activity}/unregister?email={email}")
    response_after = client.get("/activities")
    
    # Assert
    assert email not in response_after.json()["Chess Club"]["participants"]


def test_unregister_then_resignup_succeeds(client):
    """Test that unregistering allows re-signup to the same activity"""
    # Arrange
    activity = "Chess%20Club"
    email = "resignup@mergington.edu"
    
    # Act - First signup
    client.post(f"/activities/{activity}/signup?email={email}")
    response_after_signup = client.get("/activities")
    signup_success = email in response_after_signup.json()["Chess Club"]["participants"]
    
    # Act - Unregister
    client.post(f"/activities/{activity}/unregister?email={email}")
    response_after_unregister = client.get("/activities")
    unregister_success = email not in response_after_unregister.json()["Chess Club"]["participants"]
    
    # Act - Re-signup
    response_resignup = client.post(f"/activities/{activity}/signup?email={email}")
    
    # Assert
    assert signup_success
    assert unregister_success
    assert response_resignup.status_code == 200
