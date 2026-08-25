def validate_location(location:str) -> str:
    location = location.strip()


    if not location:
        raise ValueError("Location can not be empty")


    return location