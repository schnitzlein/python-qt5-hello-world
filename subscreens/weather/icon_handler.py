

def get_part_of_file_path() -> str:
    return "./subscreens/weather/icons/"


def get_icon_path(weather_code: int, daytime: str = "d") -> str:
    path = get_part_of_file_path() + get_icon_pre_file_name(weather_code) + daytime + "@2x.png"
    return path


def get_icon_pre_file_name(weather_code: int) -> str:
    if 200 <= weather_code < 233:
        return "11"
    elif 300 <= weather_code < 322:
        return "09"
    elif 500 <= weather_code < 505:
        return "10"
    elif 511 == weather_code:
        return "13"
    elif 520 <= weather_code < 532:
        return "09"
    elif 600 <= weather_code < 623:
        return "13"
    elif 700 < weather_code < 782:
        return "50"
    elif 800 == weather_code:
        return "01"
    elif 801 == weather_code:
        return "02"
    elif 802 == weather_code:
        return "03"
    elif 803 == weather_code:
        return "04"
    elif 804 == weather_code:
        return "04"
    else:
        return "01"

