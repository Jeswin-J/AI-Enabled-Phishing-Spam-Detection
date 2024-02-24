import re
from urllib.parse import urlparse


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
