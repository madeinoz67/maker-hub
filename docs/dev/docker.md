!!! Important
    Currently there is no published image - this will happen once maker-hub is officially released.

## Requirements

1. Docker Desktop installed on the local machine (https://www.docker.com/products/docker-desktop).
2. clone this repo and make install dependencies (or `make update` if you already have a clone of the repo).
3. `docker compose up` to build and run.  will be available on <http://localhost:8080/>  try `docker compose build --no-cache` first if it is caching the local build
4. `docker compose down` to stop.

!!! Note
    no volume mappings have been configured for the sqlite db this will be added shortly after database is operational.


## Configuration Files
### Dockerfile Contents

```
--8<-- "././Dockerfile"
```

### Docker-Compose contents

```
--8<-- "././docker-compose.yml"
```