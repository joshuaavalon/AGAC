from imghdr import what
from json import loads
from os import rename
from os.path import splitext, join
from re import findall
from sys import argv
from urllib.request import urlopen, urlretrieve

from bs4 import BeautifulSoup


def main():
    args = argv
    if len(args) < 2 or len(args) > 3:
        raise RuntimeError("Invalid Arguments")

    download_url = args[1]
    output_folder = args[2] if len(args) == 3 else ""
    soup = BeautifulSoup(urlopen(download_url), "html.parser")

    scripts = soup.find_all("script", type="text/javascript")

    urls = []
    for script in scripts:
        matches = findall("window\.INIT_data\[.*\]\s*=\s*(\[[\s\S]*?\])\s*;", script.get_text())
        for match in matches:
            url = "https:{}".format(loads(match)[2])
            urls.append((url.split("/")[-1], url))

    for item in urls:
        file_name = item[0]
        path = join(output_folder, file_name)
        urlretrieve(item[1], path)
        ext = splitext(file_name)[1]
        if ext == "":
            ext = what(path)
            rename(path, "{}.{}".format(path, ext))


if __name__ == "__main__":
    main()
