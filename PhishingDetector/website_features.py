import re
from bs4 import BeautifulSoup


def have_iframe(response):
    if response == "":
        return 1
    else:
        if re.findall(r"[<iframe>|<frameBorder>]", response.text):
            return 0
        else:
            return 1


def forwarding(response):
    if response == "":
        return 1
    else:
        if len(response.history) <= 2:
            return 0
        else:
            return 1


def right_click(response):
    if response == "":
        return 1
    else:
        if re.findall(r"event.button ?== ?2", response.text):
            return 0
        else:
            return 1


def mouse_over(response):
    if response == "":
        return 1
    else:
        if re.findall("<script>.+onmouseover.+</script>", response.text):
            return 1
        else:
            return 0


def check_head_script(response):
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            head = soup.find('head')
            if head:
                script_tags = head.find_all('script')
                if script_tags:
                    return 1
    except Exception as e:
        print(f"Error: {e}")
    return 0
