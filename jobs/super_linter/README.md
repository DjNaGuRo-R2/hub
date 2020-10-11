# ✅ Super linter

## Description

Simple combination of various linters, to help validate the quality of your source code.
TODO (link to repo etc)

## How to use it

1. TODO
2. Choose a version in [version list](#versions)
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/super_linter.yml'
    ```

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/getting-started/#jobs-customization)

5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `super_linter`
* Docker image:
[`github/super-linter`](https://hub.docker.com/r/github/super-linter)
* Default stage: `static_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `TODO` | TODO | `TODO` |

### Artifacts

We use [Junit](https://junit.org/junit5/)'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget.

!!! warning
    TODO: describe that the report isn't full right now. https://github.com/dhershman1/tap-junit/issues/30
