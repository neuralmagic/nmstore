# install-automation-components

This action will install various basic tools/components used during automation such as `curl`, `git`, and `wget`.

## Requirements

This action is currently designed to be used in a Debian-based environment — specifically, one using `apt` as the package manager.

## Usage

### Example

```yaml
steps:
  - name: Install automation components
    uses: neuralmagic/nm-actions/actions/install-automation-components@main
```
