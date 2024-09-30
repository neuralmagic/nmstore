# Summary

Used to find asset in downloaded build assets folder. The search is done via the bash utility `find`, so REGEX is suggested. Outputs REPO relative path to found asset. If nothing is found, then output will be empty.

## Usage

### Example

```yaml
steps:
  - name:
    uses: neuralmagic/nm-actions/actions/find-asset@main
    with:
        run_id: '0123456789'
        asset_identifier: 'nm_vllm*.whl'
```
