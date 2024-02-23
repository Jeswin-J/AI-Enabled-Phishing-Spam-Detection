import socket
from urllib.request import urlopen
from json import load
from ipwhois import IPWhois
from tld import get_tld


def ip_address(host):
    ip = socket.gethostbyname(host)
    return ip


def host_name(ip_addr):
    host = socket.gethostbyaddr(ip_addr)
    return host


def ip_location_info(ip_addr):
    if ip_addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + ip_addr + '/json'

    res = urlopen(url)
    data = load(res)

    return data


def ip_info(ip_addr):
    obj = IPWhois(ip_addr)
    result = obj.lookup_rdap()
    return result


def url_tld(url):
    tld = get_tld(url)
    return tld
