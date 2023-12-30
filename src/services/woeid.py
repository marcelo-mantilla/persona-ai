
def get_woeid(city: str):
    woeid_map = {
        'toronto': 4118,
        'london': 44418,
        'new york': 2459115,
        'san francisco': 2487956,
        'chicago': 2379574,
        'los angeles': 2442047,
        'vancouver': 9807,
        'montreal': 3534,
        'ottawa': 3369,
        'calgary': 8775,
        'quebec': 3444,
        'paris': 615702,
    }

    return woeid_map[city.lower()]