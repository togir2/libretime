from rest_framework.test import APIClient


# pylint: disable=invalid-name,unused-argument
def test_stream_preferences_get(db, api_client: APIClient):
    response = api_client.get("/api/v2/stream/preferences")
    assert response.status_code == 200
    assert response.json() == {
        "input_fade_transition": 0.0,
        "default_crossfade_duration": 0.0,
        "default_fade_in": 0.0,
        "default_fade_out": 0.0,
        "message_format": 0,
        "message_offline": "LibreTime - offline",
    }


# pylint: disable=invalid-name,unused-argument
def test_stream_state_get(db, api_client: APIClient):
    response = api_client.get("/api/v2/stream/state")
    assert response.status_code == 200
    assert response.json() == {
        "input_main_connected": False,
        "input_main_streaming": False,
        "input_show_connected": False,
        "input_show_streaming": False,
        "schedule_streaming": True,
    }
