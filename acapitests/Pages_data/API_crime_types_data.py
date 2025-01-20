class CrimeTypesData:
    CRIME1 = 'Theft'
    CRIME2 = 'Robbery'

    all_crime_type = {
        "page": 1,
        "limit": 25,
        "order": {
            "by": "name",
            "type": "asc"
        }
    }

    data_crime_type = {"name": "Digital",
                       "id": 0}
