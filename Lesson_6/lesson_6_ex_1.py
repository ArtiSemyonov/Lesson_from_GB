from collections import Counter
from os import path

from requests import get

URL = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
FILE = "nginx_logs.txt"

IP_INDEX = 0
METHOD_INDEX = 5
URL_INDEX = 6


def main():
    if not path.exists(FILE):
        download_log_file()

    log_file_parser = generator_parse_log_file()

    # count ip addresses
    ip_counter = Counter(log_rec[IP_INDEX] for log_rec in log_file_parser)
    print(ip_counter.most_common(5))


def generator_parse_log_file():
    with open(FILE, 'r', encoding='utf-8') as f:
        for log_line in f:
            splitted_line = log_line.split()
            ip, method, url, = splitted_line[IP_INDEX], splitted_line[METHOD_INDEX], splitted_line[URL_INDEX]
            method = method.strip('\'\"')
            yield ip, method, url


def download_log_file():
    response = get(FILE, stream=True)

    with open(FILE, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)


if __name__ == '__main__':
    main()
