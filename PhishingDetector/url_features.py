import re
from urllib.parse import urlparse

import unicodedata


def check_url_protocol(url):
    """
    IF THE URL DOES NOT USE https PROTOCOL, THEN THE URL IS NOT SECURE
    """
    protocol = urlparse(url).scheme
    if protocol == 'https':
        return 0
    else:
        return 1


def check_at_sign(url):
    """
    IF THE URL CONTAINS '@' SYMBOL, THEN THE URL IS REDIRECTING TO SOME OTHER EXTERNAL SITE
    """
    if "@" in url:
        return 1
    else:
        return 0


def check_url_length(url):
    """
    IF THE LENGTH OF URL IS TOO LONG, IT MAY BE HIDING RED FLAGS
    """
    if len(url) < 54:
        return 0
    else:
        return 1


def have_ip_addr(url):
    """
    IF THE URL CONTAINS IP ADDRESS INSTEAD OF DOMAIN NAME, THEN IT IS SUSPICIOUS
    """
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    ipv6_pattern = r"^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$"

    if re.search(ip_pattern, url) or re.search(ipv6_pattern, url):
        return 1
    else:
        return 0


def have_redirection(url):
    pos = url.rfind('//')
    if pos > 6:
        if pos > 7:
            return 1
        else:
            return 0
    else:
        return 0


def check_https_domain(url):
    domain = urlparse(url).netloc
    if 'https' in domain:
        return 1
    else:
        return 0


def have_dash(url):
    if '-' in urlparse(url).netloc:
        return 1
    else:
        return 0


def is_domain_upper(url):
    domain = urlparse(url).netloc
    if domain and domain[0].isupper():
        return 1
    return 0


def check_homograph(url):
    domain = urlparse(url).netloc
    for char in domain:
        ascii_value = ord(char)
        if ascii_value < 97 or ascii_value > 122:
            if ascii_value == 46:
                pass
            else:
                return 1
    return 0


def tiny_url(url):

    shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                          r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                          r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                          r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                          r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                          r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                          r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                          r"tr\.im|link\.zip\.net"

    match = re.search(shortening_services, url)
    if match:
        return 1
    else:
        return 0
