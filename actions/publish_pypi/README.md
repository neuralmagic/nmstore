# Summary

Used to build and publish packages to internal and public package indexes using tox automation engine.

## Usage

```yaml
steps:
  - name:
    uses: neuralmagic/nm-actions/actions/publish_pypi@main
    with:
      publish_pypi: true
      publish_pypi_internal: true
```
