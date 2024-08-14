# Summary

Used to build and publish packages to internal and public PyPI servers base on the `build_type` input parameter.

## Usage

```yaml
steps:
  - name:
    uses: neuralmagic/nm-actions/actions/publisher@main
    with:
      publish_pypi: true
      publish_pypi_internal: true
      timestamp: true
      prefix: "-nightly"
      build_number: ${{ github.event.pull_request.number }}
```
