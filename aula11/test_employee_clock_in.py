import requests
import pytest

# Define the API endpoint
API_URL = 'http://your-flask-api-url/clock-in'

# Valid locations for the South Unit
VALID_LOCATIONS = ['South Unit Location A', 'South Unit Location B']

# Invalid locations (too far)
INVALID_LOCATIONS = ['North Unit Location A', 'East Unit Location B']

# Edge cases
egde_cases = ['South Unit Location Edge A', 'South Unit Location Edge B']

# Test function to simulate clocking in
@pytest.mark.parametrize('location,expected_result', [
    *[(loc, 'success') for loc in VALID_LOCATIONS],
    *[(loc, 'error') for loc in INVALID_LOCATIONS],
    *[(loc, 'edge_case') for loc in edge_cases]
])

def test_clock_in(location, expected_result):
    response = requests.post(API_URL, json={'location': location})
    assert (response.json().get('status') == expected_result), f'Failed for location: {location}'

if __name__ == '__main__':
    pytest.main()