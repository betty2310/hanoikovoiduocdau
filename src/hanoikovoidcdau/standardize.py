import difflib
from data import data

useless_street_keywords = ["Phố", "Đường"]
useless_ward_keywords = ["Phường", "Quận", "Huyện"]


def get_all_streets(standard_data):
    all_streets = []
    for district in standard_data["district"]:
        for street in district["streets"]:
            street = remove_keywords(useless_street_keywords, street)
            all_streets.append(street)
    return all_streets


def get_all_wards(standard_data):
    all_wards = []
    for district in standard_data["district"]:
        for ward in district["wards"]:
            ward = remove_keywords(useless_ward_keywords, ward)
            all_wards.append(ward)
    return all_wards


def get_all_district(standard_data):
    all_districts = []
    for district in standard_data["district"]:
        all_districts.append(district["name"])

    print(all_districts)
    return all_districts


def find_closest_match(input_street, standard_data):
    closest_match = difflib.get_close_matches(input_street, standard_data)
    if closest_match:
        return closest_match[0]

    return input_street


def standardize_street_name(street: str) -> str:
    street = remove_keywords(useless_street_keywords, street)
    all_streets = get_all_streets(data)
    ans = find_closest_match(street, all_streets)
    return ans


def standardize_ward_name(ward: str) -> str:
    ward = remove_keywords(useless_ward_keywords, ward)
    all_wards = get_all_wards(data)
    ans = find_closest_match(ward, all_wards)
    return ans


def standardize_district_name(district: str) -> str:
    all_districts = get_all_district(data)
    ans = find_closest_match(district, all_districts)
    return ans


def remove_keywords(useless_keywords: list, street: str) -> str:
    for keyword in useless_keywords:
        street = street.replace(keyword, "").strip()
    return street
