# Python Tox Release Action

This is a reusable GitHub Action that finalizes the `pyproject.toml` file, builds a Python package, and optionally publishes it to public PyPI or Neural Magic PyPI.

## Inputs

- `publish_pypi`: Boolean to push to public PyPI.
- `publish_nm_pypi`: Boolean to push to Neural Magic internal PyPI.
- `build_type`: Type of build: `release`, `nightly`, or `dev`.

## Outputs

- `wheel`: The wheel output from the build.
- `tar`: The tar output from the build.

## Secrets

- `GCP_PROJECT`: The GCP project ID.
- `GCP_WORKLOAD_IDENTITY_PROVIDER`: The GCP workload identity provider.
- `GCP_NM_PYPI_SA`: The GCP service account for Neural Magic PyPI.
- `NM_PYPI_SA`: The Neural Magic PyPI service account for GCP.
- `PYPI_PUBLIC_USER`: The public PyPI username for publishing to the public PyPI.
- `PYPI_PUBLIC_AUTH`: The public PyPI password for publishing to the public PyPI.

## Usage

Use this action in your repository as follows:

```yaml
name: Deploy

on:
  push:
    branches:
      - main

jobs:
    deploy:
      uses: neuralmagic/nm-actions/actions/python-tox-release@main
      with:
        publish_pypi: false
        publish_nm_pypi: true
        build_type: dev
      secrets:
        GCP_PROJECT: ${{ secrets.GCP_PROJECT }}
        GCP_WORKLOAD_IDENTITY_PROVIDER: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
        GCP_NM_PYPI_SA: ${{ secrets.GCP_NM_PYPI_SA }}
        NM_PYPI_SA: ${{ secrets.NM_PYPI_SA }}
        PYPI_PUBLIC_USER: ${{ secrets.PYPI_PUBLIC_USER }}
        PYPI_PUBLIC_AUTH: ${{ secrets.PYPI_PUBLIC_AUTH }}
```
