# maker-hub

Personal Hub for makers, document, blog, track projects, ideas, documentation, parts and footprints etc

See the [Project Documentation](https://madeinoz67.github.io/maker-hub/) for more details.

## Features

Our hit list of features:

- [ ] Parts Database (under development)
- [ ] Part Data Sheets
- [ ] Part Images
- [ ] Manage Projects
- [ ] Project Documentation
- [ ] Manage Storage Locations
- [ ] Order tracking
- [ ] OctoPart Integration
- [ ] KiCAD footprints
- [ ] KiCAD 3D Models
- [X] Runs in Docker container
- [ ] Runs on Raspberry Pi

## About

Maker Hub is being build on FastAPI <https://fastapi.tiangolo.com/> and aims to be an open source platform for makers to manage their parts and projects at home.

### Status

This project is only in the very early stages of Development and any help would be greatly appreciated.

## Getting Started

To read the documentation

```bash
make install       # install project dependencies for the first time
make docs-serve    # make and view documentation
```

Open your browser: <http://localhost:5000>

### Docker

Currently this image is not available on docker hub due to the project status, however can be build locally.

1. docker must be installed on the local machine
2. clone this repo and make install dependencies (or make update if you already have a clone of the repo).
3. `docker compose up` to build and run.  will be available on <http://localhost:8080/>  try `docker compose build --no-cache` first if it is caching the local build
4. `docker compose down` to stop.

Note:  no volume mappings have been configured for the sqlite db this will be added shortly after database is operational. 
