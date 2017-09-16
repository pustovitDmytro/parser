# parser
tiny universal Python-based asynchronous sites scrapper

## Table of Contents
1. [Requirements](#requirements)
2. [Install & Run](#install-&-run)
3. [Project Structure](#project-structure)
4. [Tests](#tests)
5. [Related Projects](related-projects)
6. [License](license)

## Requirements
* python `3.0+`
* pip `9.0+`

## Install & Run

To install packages run:
```sh
$ pip install bs4 selenium aiohttp asyncio async_timeout time abc re
$ python script.py
```

## Project Structure

```
.
├── html                            # folder with files for offline parsing
│   └── google.example.page         # page with google request
├── results                         # folder with parsed files
├── screenshots                     # folder with selenium screenshots
├── main.py                         # file with method implementation
└── test.google.py                  # example of using
```

## Tests

Best way to test web-parser, is to parse some site with data templates. For instance in `test.google.py` you can explore a way of parsing google search pages.
Run it by
```
$ python test.google.py
```

## Related Projects

There are some  more boilerplates that I'm working on:
1. [gulp](https://github.com/pustovitDmytro/gulp) - simple template for quick site creation via gulp
2. [web-extension](https://github.com/pustovitDmytro/web-extension) - boilerplate to making web-extensions (firefox and chrome simultaneously)
3. [react](https://github.com/pustovitDmytro/react) - boilerplate for making gracefull react apps

## Examples Of Use

There are some examples of implementation:
* [dmsu-bot](https://github.com/pustovitDmytro/dmsu-bot) - bot which helped me to order biometric passport
* [quotes](https://github.com/pustovitDmytro/quotes) - scraps famous quotes and saves them to scv

## License

MIT
