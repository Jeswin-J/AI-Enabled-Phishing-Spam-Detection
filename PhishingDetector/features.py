def count_dots_in_url(url):
    """
    Count the number of dots in a URL.

    Args:
    url (str): The URL to count dots in.

    Returns:
    int: The number of dots in the URL.
    """
    dot_count = url.count('.')
    return dot_count


def count_hyphens_in_url(url):
    """
    Count the number of hyphens in a URL.

    Args:
    url (str): The URL to count hyphens in.

    Returns:
    int: The number of hyphens in the URL.
    """
    hyphen_count = url.count('-')
    return hyphen_count


def count_underscores_in_url(url):
    """
    Count the number of underscores in a URL.

    Args:
    url (str): The URL to count underscores in.

    Returns:
    int: The number of underscores in the URL.
    """
    underscore_count = url.count('_')
    return underscore_count


def count_slashes_in_url(url):
    """
    Count the number of slashes in a URL.

    Args:
    url (str): The URL to count slashes in.

    Returns:
    int: The number of slashes in the URL.
    """
    slash_count = url.count('/')
    return slash_count


def count_questionmarks_in_url(url):
    """
    Count the number of question marks in a URL.

    Args:
    url (str): The URL to count question marks in.

    Returns:
    int: The number of question marks in the URL.
    """
    question_mark_count = url.count('?')
    return question_mark_count


def count_equals_in_url(url):
    """
    Count the number of equal signs in a URL.

    Args:
    url (str): The URL to count equal signs in.

    Returns:
    int: The number of equal signs in the URL.
    """
    equal_count = url.count('=')
    return equal_count


def count_at_in_url(url):
    """
    Count the number of '@' symbols in a URL.

    Args:
    url (str): The URL to count '@' symbols in.

    Returns:
    int: The number of '@' symbols in the URL.
    """
    at_count = url.count('@')
    return at_count


def count_and_in_url(url):
    """
    Count the number of '&' symbols in a URL.

    Args:
    url (str): The URL to count '&' symbols in.

    Returns:
    int: The number of '&' symbols in the URL.
    """
    and_count = url.count('&')
    return and_count


def count_exclamation_in_url(url):
    """
    Count the number of '!' symbols in a URL.

    Args:
    url (str): The URL to count '!' symbols in.

    Returns:
    int: The number of '!' symbols in the URL.
    """
    exclamation_count = url.count('!')
    return exclamation_count


def count_spaces_in_url(url):
    """
    Count the number of spaces in a URL.

    Args:
    url (str): The URL to count spaces in.

    Returns:
    int: The number of spaces in the URL.
    """
    space_count = url.count(' ')
    return space_count


def count_tildes_in_url(url):
    """
    Count the number of '~' symbols in a URL.

    Args:
    url (str): The URL to count '~' symbols in.

    Returns:
    int: The number of '~' symbols in the URL.
    """
    tilde_count = url.count('~')
    return tilde_count


def count_commas_in_url(url):
    """
    Count the number of ',' symbols in a URL.

    Args:
    url (str): The URL to count ',' symbols in.

    Returns:
    int: The number of ',' symbols in the URL.
    """
    comma_count = url.count(',')
    return comma_count


def count_plus_in_url(url):
    """
    Count the number of '+' symbols in a URL.

    Args:
    url (str): The URL to count '+' symbols in.

    Returns:
    int: The number of '+' symbols in the URL.
    """
    plus_count = url.count('+')
    return plus_count


def count_asterisks_in_url(url):
    """
    Count the number of '*' symbols in a URL.

    Args:
    url (str): The URL to count '*' symbols in.

    Returns:
    int: The number of '*' symbols in the URL.
    """
    asterisk_count = url.count('*')
    return asterisk_count


def count_hashtags_in_url(url):
    """
    Count the number of '#' symbols in a URL.

    Args:
    url (str): The URL to count '#' symbols in.

    Returns:
    int: The number of '#' symbols in the URL.
    """
    hashtag_count = url.count('#')
    return hashtag_count


def count_dollars_in_url(url):
    """
    Count the number of '$' symbols in a URL.

    Args:
    url (str): The URL to count '$' symbols in.

    Returns:
    int: The number of '$' symbols in the URL.
    """
    dollar_count = url.count('$')
    return dollar_count


def count_percent_in_url(url):
    """
    Count the number of '%' symbols in a URL.

    Args:
    url (str): The URL to count '%' symbols in.

    Returns:
    int: The number of '%' symbols in the URL.
    """
    percent_count = url.count('%')
    return percent_count


def count_length_of_url(url):
    """
    Count the length of a URL.

    Args:
    url (str): The URL to count the length of.

    Returns:
    int: The length of the URL.
    """
    return len(url)


def count_dots_in_domain(url):
    """
    Count the number of dots in the domain portion of a URL.

    Args:
    url (str): The URL to count dots in its domain.

    Returns:
    int: The number of dots in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the dots in the domain
    dot_count = domain.count('.')
    return dot_count


def count_hyphens_in_domain(url):
    """
    Count the number of hyphens in the domain portion of a URL.

    Args:
    url (str): The URL to count hyphens in its domain.

    Returns:
    int: The number of hyphens in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the hyphens in the domain
    hyphen_count = domain.count('-')
    return hyphen_count


def count_underscores_in_domain(url):
    """
    Count the number of underscores in the domain portion of a URL.

    Args:
    url (str): The URL to count underscores in its domain.

    Returns:
    int: The number of underscores in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the underscores in the domain
    underscore_count = domain.count('_')
    return underscore_count


def count_slashes_in_domain(url):
    """
    Count the number of slashes in the domain portion of a URL.

    Args:
    url (str): The URL to count slashes in its domain.

    Returns:
    int: The number of slashes in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the slashes in the domain
    slash_count = domain.count('/')
    return slash_count


def count_question_marks_in_domain(url):
    """
    Count the number of question marks in the domain portion of a URL.

    Args:
    url (str): The URL to count question marks in its domain.

    Returns:
    int: The number of question marks in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the question marks in the domain
    question_mark_count = domain.count('?')
    return question_mark_count


def count_equals_in_domain(url):
    """
    Count the number of equal signs in the domain portion of a URL.

    Args:
    url (str): The URL to count equal signs in its domain.

    Returns:
    int: The number of equal signs in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the equal signs in the domain
    equal_count = domain.count('=')
    return equal_count


def count_at_in_domain(url):
    """
    Count the number of '@' symbols in the domain portion of a URL.

    Args:
    url (str): The URL to count '@' symbols in its domain.

    Returns:
    int: The number of '@' symbols in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the '@' symbols in the domain
    at_count = domain.count('@')
    return at_count


def count_ampersand_in_domain(url):
    """
    Count the number of '&' symbols in the domain portion of a URL.

    Args:
    url (str): The URL to count '&' symbols in its domain.

    Returns:
    int: The number of '&' symbols in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the '&' symbols in the domain
    ampersand_count = domain.count('&')
    return ampersand_count


def count_exclamation_in_domain(url):
    """
    Count the number of '!' symbols in the domain portion of a URL.

    Args:
    url (str): The URL to count '!' symbols in its domain.

    Returns:
    int: The number of '!' symbols in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the '!' symbols in the domain
    exclamation_count = domain.count('!')
    return exclamation_count


def count_spaces_in_domain(url):
    """
    Count the number of ' ' (space) characters in the domain portion of a URL.

    Args:
    url (str): The URL to count ' ' (space) characters in its domain.

    Returns:
    int: The number of ' ' (space) characters in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the ' ' (space) characters in the domain
    space_count = domain.count(' ')
    return space_count


def count_tilde_in_domain(url):
    """
    Count the number of '~' symbols in the domain portion of a URL.

    Args:
    url (str): The URL to count '~' symbols in its domain.

    Returns:
    int: The number of '~' symbols in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the '~' symbols in the domain
    tilde_count = domain.count('~')
    return tilde_count


def count_commas_in_domain(url):
    """
    Count the number of ',' symbols in the domain portion of a URL.

    Args:
    url (str): The URL to count ',' symbols in its domain.

    Returns:
    int: The number of ',' symbols in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the ',' symbols in the domain
    comma_count = domain.count(',')
    return comma_count


def count_plus_in_domain(url):
    """
    Count the number of '+' symbols in the domain portion of a URL.

    Args:
    url (str): The URL to count '+' symbols in its domain.

    Returns:
    int: The number of '+' symbols in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the '+' symbols in the domain
    plus_count = domain.count('+')
    return plus_count


def count_asterisks_in_domain(url):
    """
    Count the number of '*' symbols in the domain portion of a URL.

    Args:
    url (str): The URL to count '*' symbols in its domain.

    Returns:
    int: The number of '*' symbols in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the '*' symbols in the domain
    asterisk_count = domain.count('*')
    return asterisk_count


def count_hashtags_in_domain(url):
    """
    Count the number of '#' symbols in the domain portion of a URL.

    Args:
    url (str): The URL to count '#' symbols in its domain.

    Returns:
    int: The number of '#' symbols in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the '#' symbols in the domain
    hashtag_count = domain.count('#')
    return hashtag_count


def count_dollars_in_domain(url):
    """
    Count the number of '$' symbols in the domain portion of a URL.

    Args:
    url (str): The URL to count '$' symbols in its domain.

    Returns:
    int: The number of '$' symbols in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the '$' symbols in the domain
    dollar_count = domain.count('$')
    return dollar_count


def count_percent_in_domain(url):
    """
    Count the number of '%' symbols in the domain portion of a URL.

    Args:
    url (str): The URL to count '%' symbols in its domain.

    Returns:
    int: The number of '%' symbols in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the '%' symbols in the domain
    percent_count = domain.count('%')
    return percent_count


def count_vowels_in_domain(url):
    """
    Count the number of vowels in the domain portion of a URL.

    Args:
    url (str): The URL to count vowels in its domain.

    Returns:
    int: The number of vowels in the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Count the vowels in the domain
    vowels = 'aeiou'
    vowel_count = sum(domain.count(vowel) for vowel in vowels)
    return vowel_count


def count_domain_length(url):
    """
    Count the length of the domain portion of a URL.

    Args:
    url (str): The URL to count the length of its domain.

    Returns:
    int: The length of the domain portion of the URL.
    """
    # Extract the domain from the URL
    domain_start = url.find('//') + 2
    domain_end = url.find('/', domain_start)
    if domain_end == -1:
        domain_end = len(url)
    domain = url[domain_start:domain_end]

    # Calculate the length of the domain
    domain_length = len(domain)
    return domain_length


def count_dot_in_directory(url):
    """
    Count the number of '.' symbols in the directory portion of a URL.

    Args:
    url (str): The URL to count '.' symbols in its directory.

    Returns:
    int: The number of '.' symbols in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '.' symbols in the directory
    dot_count = directory.count('.')
    return dot_count


def count_hyphen_in_directory(url):
    """
    Count the number of '-' symbols in the directory portion of a URL.

    Args:
    url (str): The URL to count '-' symbols in its directory.

    Returns:
    int: The number of '-' symbols in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '-' symbols in the directory
    hyphen_count = directory.count('-')
    return hyphen_count


def count_underscore_in_directory(url):
    """
    Count the number of '_' symbols in the directory portion of a URL.

    Args:
    url (str): The URL to count '_' symbols in its directory.

    Returns:
    int: The number of '_' symbols in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '_' symbols in the directory
    underscore_count = directory.count('_')
    return underscore_count


def count_slash_in_directory(url):
    """
    Count the number of '/' symbols in the directory portion of a URL.

    Args:
    url (str): The URL to count '/' symbols in its directory.

    Returns:
    int: The number of '/' symbols in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '/' symbols in the directory
    slash_count = directory.count('/')
    return slash_count


def count_questionmark_in_directory(url):
    """
    Count the number of '?' symbols in the directory portion of a URL.

    Args:
    url (str): The URL to count '?' symbols in its directory.

    Returns:
    int: The number of '?' symbols in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '?' symbols in the directory
    questionmark_count = directory.count('?')
    return questionmark_count


def count_equal_in_directory(url):
    """
    Count the number of '=' symbols in the directory portion of a URL.

    Args:
    url (str): The URL to count '=' symbols in its directory.

    Returns:
    int: The number of '=' symbols in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '=' symbols in the directory
    equal_count = directory.count('=')
    return equal_count


def count_at_in_directory(url):
    """
    Count the number of '@' symbols in the directory portion of a URL.

    Args:
    url (str): The URL to count '@' symbols in its directory.

    Returns:
    int: The number of '@' symbols in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '@' symbols in the directory
    at_count = directory.count('@')
    return at_count


def count_and_in_directory(url):
    """
    Count the number of '&' symbols in the directory portion of a URL.

    Args:
    url (str): The URL to count '&' symbols in its directory.

    Returns:
    int: The number of '&' symbols in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '&' symbols in the directory
    and_count = directory.count('&')
    return and_count


def count_exclamation_in_directory(url):
    """
    Count the number of '!' symbols in the directory portion of a URL.

    Args:
    url (str): The URL to count '!' symbols in its directory.

    Returns:
    int: The number of '!' symbols in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '!' symbols in the directory
    exclamation_count = directory.count('!')
    return exclamation_count


def count_space_in_directory(url):
    """
    Count the number of ' ' (space) characters in the directory portion of a URL.

    Args:
    url (str): The URL to count ' ' (space) characters in its directory.

    Returns:
    int: The number of ' ' (space) characters in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the ' ' (space) characters in the directory
    space_count = directory.count(' ')
    return space_count


def count_tilde_in_directory(url):
    """
    Count the number of '~' characters in the directory portion of a URL.

    Args:
    url (str): The URL to count '~' characters in its directory.

    Returns:
    int: The number of '~' characters in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '~' characters in the directory
    tilde_count = directory.count('~')
    return tilde_count


def count_comma_in_directory(url):
    """
    Count the number of ',' characters in the directory portion of a URL.

    Args:
    url (str): The URL to count ',' characters in its directory.

    Returns:
    int: The number of ',' characters in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the ',' characters in the directory
    comma_count = directory.count(',')
    return comma_count


def count_plus_in_directory(url):
    """
    Count the number of '+' characters in the directory portion of a URL.

    Args:
    url (str): The URL to count '+' characters in its directory.

    Returns:
    int: The number of '+' characters in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '+' characters in the directory
    plus_count = directory.count('+')
    return plus_count


def count_asterisk_in_directory(url):
    """
    Count the number of '*' characters in the directory portion of a URL.

    Args:
    url (str): The URL to count '*' characters in its directory.

    Returns:
    int: The number of '*' characters in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '*' characters in the directory
    asterisk_count = directory.count('*')
    return asterisk_count


def count_hashtag_in_directory(url):
    """
    Count the number of '#' characters in the directory portion of a URL.

    Args:
    url (str): The URL to count '#' characters in its directory.

    Returns:
    int: The number of '#' characters in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '#' characters in the directory
    hashtag_count = directory.count('#')
    return hashtag_count


def count_dollar_in_directory(url):
    """
    Count the number of '$' characters in the directory portion of a URL.

    Args:
    url (str): The URL to count '$' characters in its directory.

    Returns:
    int: The number of '$' characters in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '$' characters in the directory
    dollar_count = directory.count('$')
    return dollar_count


def count_percent_in_directory(url):
    """
    Count the number of '%' characters in the directory portion of a URL.

    Args:
    url (str): The URL to count '%' characters in its directory.

    Returns:
    int: The number of '%' characters in the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Count the '%' characters in the directory
    percent_count = directory.count('%')
    return percent_count


def directory_length(url):
    """
    Count the length of the directory portion of a URL.

    Args:
    url (str): The URL to count the length of its directory.

    Returns:
    int: The length of the directory portion of the URL.
    """
    # Extract the directory from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    directory = url[path_start:]

    # Calculate the length of the directory
    directory_length = len(directory)
    return directory_length


def count_dot_in_file(url):
    """
    Count the number of '.' symbols in the file portion of a URL.

    Args:
    url (str): The URL to count '.' symbols in its file portion.

    Returns:
    int: The number of '.' symbols in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '.' symbols in the file portion
    dot_count = path.count('.')
    return dot_count


def count_hyphen_in_file(url):
    """
    Count the number of '-' symbols in the file portion of a URL.

    Args:
    url (str): The URL to count '-' symbols in its file portion.

    Returns:
    int: The number of '-' symbols in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '-' symbols in the file portion
    hyphen_count = path.count('-')
    return hyphen_count


def count_underline_in_file(url):
    """
    Count the number of '_' symbols in the file portion of a URL.

    Args:
    url (str): The URL to count '_' symbols in its file portion.

    Returns:
    int: The number of '_' symbols in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '_' symbols in the file portion
    underline_count = path.count('_')
    return underline_count


def count_slash_in_file(url):
    """
    Count the number of '/' symbols in the file portion of a URL.

    Args:
    url (str): The URL to count '/' symbols in its file portion.

    Returns:
    int: The number of '/' symbols in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '/' symbols in the file portion
    slash_count = path.count('/')
    return slash_count


def count_questionmark_in_file(url):
    """
    Count the number of '?' symbols in the file portion of a URL.

    Args:
    url (str): The URL to count '?' symbols in its file portion.

    Returns:
    int: The number of '?' symbols in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '?' symbols in the file portion
    questionmark_count = path.count('?')
    return questionmark_count


def count_equal_in_file(url):
    """
    Count the number of '=' symbols in the file portion of a URL.

    Args:
    url (str): The URL to count '=' symbols in its file portion.

    Returns:
    int: The number of '=' symbols in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '=' symbols in the file portion
    equal_count = path.count('=')
    return equal_count


def count_at_in_file(url):
    """
    Count the number of '@' symbols in the file portion of a URL.

    Args:
    url (str): The URL to count '@' symbols in its file portion.

    Returns:
    int: The number of '@' symbols in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '@' symbols in the file portion
    at_count = path.count('@')
    return at_count


def count_and_in_file(url):
    """
    Count the number of '&' symbols in the file portion of a URL.

    Args:
    url (str): The URL to count '&' symbols in its file portion.

    Returns:
    int: The number of '&' symbols in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '&' symbols in the file portion
    and_count = path.count('&')
    return and_count


def count_exclamation_in_file(url):
    """
    Count the number of '!' symbols in the file portion of a URL.

    Args:
    url (str): The URL to count '!' symbols in its file portion.

    Returns:
    int: The number of '!' symbols in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '!' symbols in the file portion
    exclamation_count = path.count('!')
    return exclamation_count


def count_space_in_file(url):
    """
    Count the number of ' ' (space) characters in the file portion of a URL.

    Args:
    url (str): The URL to count ' ' (space) characters in its file portion.

    Returns:
    int: The number of ' ' (space) characters in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the ' ' (space) characters in the file portion
    space_count = path.count(' ')
    return space_count


def count_tilde_in_file(url):
    """
    Count the number of '~' characters in the file portion of a URL.

    Args:
    url (str): The URL to count '~' characters in its file portion.

    Returns:
    int: The number of '~' characters in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '~' characters in the file portion
    tilde_count = path.count('~')
    return tilde_count


def count_comma_in_file(url):
    """
    Count the number of ',' characters in the file portion of a URL.

    Args:
    url (str): The URL to count ',' characters in its file portion.

    Returns:
    int: The number of ',' characters in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the ',' characters in the file portion
    comma_count = path.count(',')
    return comma_count


def count_plus_in_file(url):
    """
    Count the number of '+' characters in the file portion of a URL.

    Args:
    url (str): The URL to count '+' characters in its file portion.

    Returns:
    int: The number of '+' characters in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '+' characters in the file portion
    plus_count = path.count('+')
    return plus_count


def count_asterisk_in_file(url):
    """
    Count the number of '*' characters in the file portion of a URL.

    Args:
    url (str): The URL to count '*' characters in its file portion.

    Returns:
    int: The number of '*' characters in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '*' characters in the file portion
    asterisk_count = path.count('*')
    return asterisk_count


def count_hashtag_in_file(url):
    """
    Count the number of '#' characters in the file portion of a URL.

    Args:
    url (str): The URL to count '#' characters in its file portion.

    Returns:
    int: The number of '#' characters in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '#' characters in the file portion
    hashtag_count = path.count('#')
    return hashtag_count


def count_dollar_in_file(url):
    """
    Count the number of '$' characters in the file portion of a URL.

    Args:
    url (str): The URL to count '$' characters in its file portion.

    Returns:
    int: The number of '$' characters in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '$' characters in the file portion
    dollar_count = path.count('$')
    return dollar_count


def count_percent_in_file(url):
    """
    Count the number of '%' characters in the file portion of a URL.

    Args:
    url (str): The URL to count '%' characters in its file portion.

    Returns:
    int: The number of '%' characters in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    path = url[path_start + 1: file_start]

    # Count the '%' characters in the file portion
    percent_count = path.count('%')
    return percent_count


def file_length(url):
    """
    Count the length of the file name in the file portion of a URL.

    Args:
    url (str): The URL to count the length of the file name in its file portion.

    Returns:
    int: The length of the file name in the file portion of the URL.
    """
    # Extract the path from the URL
    domain_end = url.find('//') + 2
    path_start = url.find('/', domain_end)
    if path_start == -1:
        return 0
    file_start = url.rfind('/') + 1
    file_name = url[file_start:]

    # Count the length of the file name
    file_name_length = len(file_name)
    return file_name_length


def count_dot_in_params(url):
    """
    Count the number of '.' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '.' characters in its parameters section.

    Returns:
    int: The number of '.' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '.' characters in the parameters section
    dot_count = params.count('.')
    return dot_count


def count_hyphen_in_params(url):
    """
    Count the number of '-' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '-' characters in its parameters section.

    Returns:
    int: The number of '-' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '-' characters in the parameters section
    hyphen_count = params.count('-')
    return hyphen_count


def count_underscore_in_params(url):
    """
    Count the number of '_' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '_' characters in its parameters section.

    Returns:
    int: The number of '_' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '_' characters in the parameters section
    underscore_count = params.count('_')
    return underscore_count


def count_slash_in_params(url):
    """
    Count the number of '/' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '/' characters in its parameters section.

    Returns:
    int: The number of '/' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '/' characters in the parameters section
    slash_count = params.count('/')
    return slash_count


def count_questionmark_in_params(url):
    """
    Count the number of '?' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '?' characters in its parameters section.

    Returns:
    int: The number of '?' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '?' characters in the parameters section
    questionmark_count = params.count('?')
    return questionmark_count


def count_equal_in_params(url):
    """
    Count the number of '=' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '=' characters in its parameters section.

    Returns:
    int: The number of '=' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '=' characters in the parameters section
    equal_count = params.count('=')
    return equal_count


def count_at_in_params(url):
    """
    Count the number of '@' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '@' characters in its parameters section.

    Returns:
    int: The number of '@' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '@' characters in the parameters section
    at_count = params.count('@')
    return at_count


def count_and_in_params(url):
    """
    Count the number of '&' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '&' characters in its parameters section.

    Returns:
    int: The number of '&' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '&' characters in the parameters section
    and_count = params.count('&')
    return and_count


def count_exclamation_in_params(url):
    """
    Count the number of '!' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '!' characters in its parameters section.

    Returns:
    int: The number of '!' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '!' characters in the parameters section
    exclamation_count = params.count('!')
    return exclamation_count


def count_space_in_params(url):
    """
    Count the number of ' ' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count ' ' characters in its parameters section.

    Returns:
    int: The number of ' ' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the ' ' characters in the parameters section
    space_count = params.count(' ')
    return space_count


def count_tilde_in_params(url):
    """
    Count the number of '~' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '~' characters in its parameters section.

    Returns:
    int: The number of '~' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '~' characters in the parameters section
    tilde_count = params.count('~')
    return tilde_count


def count_comma_in_params(url):
    """
    Count the number of ',' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count ',' characters in its parameters section.

    Returns:
    int: The number of ',' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the ',' characters in the parameters section
    comma_count = params.count(',')
    return comma_count


def count_plus_in_params(url):
    """
    Count the number of '+' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '+' characters in its parameters section.

    Returns:
    int: The number of '+' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '+' characters in the parameters section
    plus_count = params.count('+')
    return plus_count


def count_asterisk_in_params(url):
    """
    Count the number of '*' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '*' characters in its parameters section.

    Returns:
    int: The number of '*' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '*' characters in the parameters section
    asterisk_count = params.count('*')
    return asterisk_count


def count_hashtag_in_params(url):
    """
    Count the number of '#' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '#' characters in its parameters section.

    Returns:
    int: The number of '#' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '#' characters in the parameters section
    hashtag_count = params.count('#')
    return hashtag_count


def count_dollar_in_params(url):
    """
    Count the number of '$' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '$' characters in its parameters section.

    Returns:
    int: The number of '$' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '$' characters in the parameters section
    dollar_count = params.count('$')
    return dollar_count


def count_percent_in_params(url):
    """
    Count the number of '%' characters in the parameters section of a URL.

    Args:
    url (str): The URL to count '%' characters in its parameters section.

    Returns:
    int: The number of '%' characters in the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the '%' characters in the parameters section
    percent_count = params.count('%')
    return percent_count


def params_length(url):
    """
    Count the length of the parameters section of a URL.

    Args:
    url (str): The URL to count the length of its parameters section.

    Returns:
    int: The length of the parameters section of the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Return the length of the parameters section
    return len(params)


def tld_present_params(url):
    """
    Check if a Top-Level Domain (TLD) is present in the parameters section of a URL.

    Args:
    url (str): The URL to check.

    Returns:
    bool: True if a TLD is present in the parameters section of the URL, False otherwise.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Check if a TLD is present in the parameters section
    tld_list = [
            '.com',
            '.org',
            '.net',
            '.gov',
            '.edu',
            '.mil',
            '.int',
            '.info',
            '.biz',
            '.name',
            '.us',  # United States
            '.uk',  # United Kingdom
            '.ca',  # Canada
            '.au',  # Australia
            '.de',  # Germany
            '.jp',  # Japan
            '.fr',  # France
            '.cn',  # China
            '.in',  # India
            '.ru',  # Russia
            # Additional TLDs
            '.io',
            '.co',
            '.tv',
            '.me',
            '.mobi',
            '.cc',
            '.ws',
            '.xyz',
            '.online',
            '.tech',
            '.space',
            '.store',
            '.website',
            '.blog',
            '.club',
            '.design',
            '.dev',
            '.fm',
            '.fm',
            '.app',
            '.asia',
            '.at',
            '.ch',
            '.es',
            '.it',
            '.nl',
            '.nz',
            '.se',
            '.sg',
            '.be',
            '.dk',
            '.fi',
            '.no',
            '.pl',
            '.pt',
            '.gr',
            '.hu',
            '.ie',
            '.kr',
            '.mx'
        ]
    for tld in tld_list:
        if tld in params:
            return 1
    return 0


def count_params(url):
    """
    Count the number of parameters in a URL.

    Args:
    url (str): The URL to count parameters.

    Returns:
    int: The number of parameters in the URL.
    """
    # Extract the parameters from the URL
    params_start = url.find('?') + 1
    if params_start == 0:
        return 0
    params = url[params_start:]

    # Count the number of parameters
    param_count = len(params.split('&'))
    return param_count


def url_shortened(url):
    """
    Check if a URL is likely shortened.

    Args:
    url (str): The URL to check.

    Returns:
    bool: True if the URL is likely shortened, False otherwise.
    """
    # Define a threshold for considering a URL as shortened
    # You can adjust this threshold based on your requirements
    threshold_length = 20  # Example threshold length

    # Compare the length of the URL with the threshold
    if len(url) < threshold_length:
        return 1  # URL is likely shortened
    else:
        return 0  # URL is not likely shortened


def feature_extraction(url):
    features = [count_dots_in_url(url), count_hyphens_in_url(url), count_underscores_in_url(url),
                count_slashes_in_url(url), count_questionmarks_in_url(url), count_equals_in_url(url),
                count_at_in_url(url), count_and_in_url(url), count_exclamation_in_url(url), count_spaces_in_url(url),
                count_tildes_in_url(url), count_commas_in_url(url), count_plus_in_url(url), count_asterisks_in_url(url),
                count_hashtags_in_url(url), count_dollars_in_url(url), count_percent_in_url(url),
                count_length_of_url(url), count_dots_in_domain(url), count_hyphens_in_domain(url),
                count_underscores_in_domain(url), count_slashes_in_domain(url), count_question_marks_in_domain(url),
                count_equals_in_domain(url), count_at_in_domain(url), count_ampersand_in_domain(url),
                count_exclamation_in_domain(url), count_tilde_in_domain(url), count_commas_in_domain(url),
                count_plus_in_domain(url), count_asterisks_in_domain(url), count_hashtags_in_domain(url),
                count_dollars_in_domain(url), count_percent_in_domain(url), count_vowels_in_domain(url),
                count_domain_length(url), count_dot_in_directory(url), count_hyphen_in_directory(url),
                count_underscore_in_directory(url), count_slash_in_directory(url), count_questionmark_in_directory(url),
                count_equal_in_directory(url), count_at_in_directory(url), count_and_in_directory(url),
                count_exclamation_in_directory(url), count_tilde_in_directory(url), count_comma_in_directory(url),
                count_plus_in_directory(url), count_asterisk_in_directory(url), count_hashtag_in_directory(url),
                count_dollar_in_directory(url), count_percent_in_directory(url), directory_length(url),
                count_dot_in_file(url), count_hyphen_in_file(url), count_underline_in_file(url),
                count_questionmark_in_file(url), count_equal_in_file(url), count_and_in_file(url),
                count_exclamation_in_file(url), count_space_in_file(url), count_tilde_in_file(url),
                count_comma_in_file(url), count_plus_in_file(url), count_asterisk_in_file(url),
                count_hashtag_in_file(url), count_dollar_in_file(url), count_percent_in_file(url), file_length(url),
                count_dot_in_params(url), count_hyphen_in_params(url), count_underscore_in_params(url),
                count_slash_in_params(url), count_questionmark_in_params(url), count_equal_in_params(url),
                count_at_in_params(url), count_and_in_params(url), count_exclamation_in_params(url),
                count_tilde_in_params(url), count_comma_in_params(url), count_plus_in_params(url),
                count_asterisk_in_params(url), count_hashtag_in_params(url), count_dollar_in_params(url),
                count_percent_in_params(url), params_length(url), tld_present_params(url), count_params(url),
                url_shortened(url)]

    return features
