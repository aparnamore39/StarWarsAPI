import json
import pytest
from endpoints import endpoints_starwars
import requests
from utils import swapi


def test_people_200_OK():
    response = swapi.getpeople();
    assert response.status_code == 200, f"Expected status code is 200, but got {response.status_code}"


def test_people_with_height_more_than_200():
    response = swapi.get_all_people()

    expected_names = [
        "Darth Vader", "Chewbacca", "Roos Tarpals", "Rugor Nass",
        "Yarael Poof", "Lama Su", "Taun We", "Grievous", "Tarfful", "Tion Medon"
    ]

    actual_names = []
    count = 0

    for person in response:
        if 'height' in person and person['height'].isdigit():
            height = int(person['height'])
            # Check if the height is more than 80
            if height > 200:
                count += 1
                actual_names.append(person['name'])

    assert count == 10, "No people found with height more than 80"
    assert expected_names == actual_names, "Unexpected names found"


def test_total_people():
    response = swapi.get_all_people();
    total = len(response)

    assert total == 82, "Count is incorrect"
