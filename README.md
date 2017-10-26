# Archiving Google Arts & Culture

![](https://img.shields.io/github/license/joshuaavalon/AGAC.svg)

Python script to scrap images from Google Arts & Culture. This is a request from [r/DataHoarder](https://www.reddit.com/r/DataHoarder/comments/78h9ck/archiving_google_arts_culture_paintings/).

## Requirements
* Python 3
* Beautiful Soup 4.6.0

## Install
```bash
pip install -r requirements.txt
```

## Usage
It should work on pages that have `window.INIT_data`.

```bash
python agac.py <url> [<output folder>]
```

```bash
python agac.py "https://www.google.com/culturalinstitute/beta/"
```

## How does it work?
It loads the html and parses `window.INIT_data` in the `<script>`. Then, it uses imghdr to determine file extension if not provided.
