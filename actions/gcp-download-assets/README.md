# Summary

Used to download build assets from GCP. Assets are identified by the Github Actions Run that generated them. The download is recusive and will download whatever was placed under the "run id" prefix.


**Requires "runner" to already be authenticated.**


**Requires access to Github secret `GCP_BUILD_ASSETS`**


## Usage

### Example

```yaml
steps:
  - name:
    uses: neuralmagic/nm-actions/actions/gcp-download-assets@main
    with:
        bucket_source: 'gs://some-bucket/some-prefix'
        run_id: '0123456789'
```
