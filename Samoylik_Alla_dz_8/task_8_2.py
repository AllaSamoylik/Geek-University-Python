import re

RE_EMAIL_PARSER = re.compile(
    r'(^[\d.]+) - - \[([\d\w\s/:+]+)] \"([A-Z]+) ([/\w]+) [A-Z]+/[\d.]+\" (\d+) (\d+)(?= )')

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for row in f:
        parsed_raw = re.findall(RE_EMAIL_PARSER, row)
        parsed_raw_str = ''.join(str(i) for i in parsed_raw)
        print(parsed_raw_str)
