HOST_PATH = "C:/Windows/System32/drivers/etc/hosts"
REDIRECT = '127.0.0.1'


def block_websites(domain_list):
    with open(HOST_PATH, 'r+') as file:
        content = file.read()
        for domain in domain_list:
            if domain in content:
                pass
            else:
                file.write(REDIRECT + ' ' + domain + '\n')
    print("Listed Websites are blocked")


def unblock_websites(domain_list):
    with open(HOST_PATH, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(domain in line for domain in domain_list):
                file.write(line)
        file.truncate()
    print("Websites unblocked successfully.")

