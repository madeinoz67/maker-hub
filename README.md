# maker-hub

Personal Hub for makers, document, blog, track projects, ideas, documentation, parts and footprints etc

## About

Maker Hub is being build on FastAPI <https://fastapi.tiangolo.com/> and aims to be an open source platform for makers to manage their parts and projects at home.

### Status

This project is only in the very early stages of Development.

## Getting Started

To read the documentation

```bash
make install       # install project dependencies for the first time
make docs-serve    # make and view documentation
```

Open your browser: <http://localhost:8000>

### Docker

currently this image is not availble on docker hub due to the project status, howver can be build locally.

1. docker must be installed on the local machine
2. clone this repo and make install dependencies (or make update if you already have a clone of the repo).
3. `docker compose up` to build and run.  will be available on <http://localhost:8080/>  try `docker compose build --no-cache` first if it is caching the local build
4. `docker compose down` to stop.

Note:  no volume mappings have been configured for the sqlite db this will be added shortly after database is operational. 

## Help Wanted

1) Front end developers - We're definitely not front end developers so any help would be greatly appreciated, particularly around dynamic live searches.

Merge Requests Accepted!
