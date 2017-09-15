# parser
tiny universal Python-based asynchronous sites scrapper

## Table of Contents
1. [Requirements](#requirements)
2. [Install & Run](#how-to-install)
3. [Project Structure](#project-structure)

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
├── build                    # All build-related code
├── public                   # Static public assets (not imported anywhere in source code)
├── server                   # Express application that provides webpack middleware
│   └── main.js              # Server application entry point
```

## Tests

Best way to test web-parser, is to parse some site with data templates. For instance


## Related Projects

There are some  more boilerplates that I'm working on:
1. [gulp](https://github.com/pustovitDmytro/gulp) - simple template for quick site creation via gulp
2. [web-extension](https://github.com/pustovitDmytro/web-extension) - boilerplate to making web-extensions (firefox and chrome simultaneously)
3. [react](https://github.com/pustovitDmytro/react) - boilerplate for making gracefull react apps

## License

MIT
