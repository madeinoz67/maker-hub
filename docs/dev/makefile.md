## Commands

`make install` - installs project dependencies and virtual python environment using poetry

`make update` - updates projects dependencies using poetry

`make docs-build` - builds project documentation.

`make docs-serve` - builds and serves project documentation on <https://localhost:5000>.

`make docs-clean` - cleans documentation build artifacts.

`make test` - Runs python tests.

`make schema-revision` - creates a new revision of the current applcations schema ready for schema upgrade

`make schema-upgrade` - will perform database schema upgrade to the latest version

`make schema-downgrade` - will perform schema downgrade to the previous version [data may be lost]

## Makefile Contents

```
--8<-- "././makefile"
```
