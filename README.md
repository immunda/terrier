## Terrier

Terrier is a helper for Terraform remote configuration. It allows `terraform remote` configurations to be stored in a JSON file and used between developers reliably. Currently Terraform doesn't support meta-configuration of itself or its remotes. This makes usage of `terraform remote` problematic as lengthy commands need to remembered or be disseminated through a `README` or other error prone methods.

## Usage

### Define a `terrier.json` configuration file

```
{
  "qa": {
    "remote": {
      "backend": "S3",
      "config": {
        "bucket": "foo-qa-bucket",
        "key": "foo-qa.tfstate",
        "region": "us-west-1"
      }
    }
  }
}
```

The top level key provides the name of an environment, `qa` in the following example. Keys generally map to `terraform remote config` arguments. Keys and values defined under `config` will be passed through as `-backend-config` arguments.

### Run `terrier remote <environment>`

The example above would be called with

`terrier remote qa`

and would generate and execute the following `terraform remote` command

`terraform remote config -backend=S3 -backend-config="bucket=foo-qa-bucket" -backend-config="key=foo-qa.tfstate" -backend-config="region=us-west-1"`

### Continue with `terraform remote`

`terrier` only handles configuration of multiple `terraform` remotes. Once run and a remote configured, one should carry on using vanilla `terraform remote pull` and `push` commands.
