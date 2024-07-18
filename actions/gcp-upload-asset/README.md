# Summary

Used to upload build asset to GCP. Requires that the assets are available locally, e.g. they have already been downloaded from our backing store.

**Requires "runner" to already be authenticated.**


## Usage

### Example

```yaml
steps:
  - name: upload asset to GCP
    uses: neuralmagic/nm-actions/actions/gcp-upload-asset@main
    with:
        bucket_target: 'gs://some-bucket/some-prefix'
        asset: 'dist/awesome-build.asset'
```

To set ideas this will result in an object created at `gs://some-bucket/some-prefix/awesome-build.asset`.
