from datetime import datetime, timezone, timedelta
import random

from DatabaseHandler.json_handler import read_json


def calc_phishing_score(features):
    weights = {
        "protocol": 2,
        "at_sign": 1.5,
        "url_length": 1.5,
        "ip_in_domain": 2.5,
        "redirection": 2,
        "https_in_domain": 2,
        "dash": 1,
        "upper_case": 1.5,
        "homograph": 2.5,
        "short": 2,
        "iframe": 2,
        "forward": 1.5,
        "r_click": 1.5,
        "m_over": 1.5,
        "head_script": 2,
        "have_num": 1.5,
        "favicon": 2,
    }

    phishing_score = 0
    max_score = 28.5

    for feature, weight in weights.items():
        if feature in features:
            phishing_score += weight * features[feature]

    phishing_score = (phishing_score / max_score) * 100
    print(phishing_score)

    return phishing_score


def get_timestamp():
    current_time_utc = datetime.now(timezone.utc)
    target_timezone = timezone(timedelta(hours=5, minutes=30))
    current_time_target_timezone = current_time_utc.astimezone(target_timezone)
    current_timestamp = current_time_target_timezone.strftime("%Y-%m-%dT%H:%M:%S%z")
    return current_timestamp


def get_random_recommend(data, key):
    inner_keys = list(data[key].keys())
    random_inner_key = random.choice(inner_keys)
    random_recommendation = random.choice(data[key][random_inner_key])
    return random_recommendation
