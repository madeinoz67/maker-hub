## Environment

The python environment and packages is managed by `poetry`.

To access:

`poetry shell`

To exit:

`exit`

## Dependencies installation

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

