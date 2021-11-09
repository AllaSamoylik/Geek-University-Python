import re


def email_parse(email):
    match = re.search(r'(?P<username>[^.][\w\"!._&#;%()+-\\]*[^.\\])@(?P<domain>[\w-]+\.[A-Za-z]{2,})',
                      email)
    try:
        print(match.groupdict())
    except AttributeError:
        msg = f'wrong email: {email}'
        raise ValueError(msg)


email_parse('someone@geekbrains.ru')
# email_parse('someone@geekbrainsru')
