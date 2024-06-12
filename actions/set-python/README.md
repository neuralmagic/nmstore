# set-python

This action sets the local version of Python and creates a virtual environment.

## Requirements

This action requires `pyenv` to be installed.

## Usage

`set-python` accepts two inputs (both required) and yields a single output:

### Inputs

* `python`: the python version to use
* `venv`: the base name for the virtual environment

### Output

* `version`: the full Python version (from `python --version`)

### Example

```yaml
steps:
  - name: "Set Python"
    uses: neuralmagic/nm-actions/actions/set-python@main
      with:
        python: 3.10.12
        venv: BUILD
```
