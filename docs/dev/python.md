## Virtual Environment

The python environment and packages is managed by `poetry`.

To access:

`poetry shell`

To exit:

`exit`

### Dependencies installation

Some packages are only required during the development process and should not be deployed to production e.g. mkdocs.  While others i.e. ansible are required for deployment to production.

=== "For Development"
    ````
    poetry install -D package-x 
    ````

=== "For Production"
    ````
    poetry install package-y
    ````

!!! Note
    See [poetry](https://python-poetry.org/docs/) documentation for more details.

## Debugging

The project uses .env files to configure debugging.

Copy .env.example to .env in the project root directory.  

### Logging

Logging at **INFO** level to *sysout* is enabled by default, however logging to a file can be enabled. i.e. in such case you need to lodge a bug.

`DEBUG=True` enables logging to a log file, and **DEBUG** logging level.

`LOGFILE="maker-hub.log"` sets the external log file name.

`ENABLE_SQL_LOGGING=True` Enables all underlying sql statements to be logged.

!!! Note
    When the logfile is enabled it will create the logfile in the root of the project directory.

