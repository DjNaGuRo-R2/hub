# Getting started

## ⏳ Quick setup

Follows these steps to setup your CI/CD pipeline in less than 10 minutes !

1. If you haven't yet a `.gitlab-ci.yml` file in the root on your repository:
   create it with the list of stages:

    ```yaml
    stages:
      - static_tests
      - build
      - dynamic_tests
      - review
      - deployment
    ```

    !!! info
        Check [stages](#stages) section to get more information about this list
        or if you already have a configuration with different stages.

2. Select jobs you want in [Jobs section](/jobs/) and add their URL at the end
   of your `.gitlab-ci.yml` file:

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/<job_name>.yml'
      - remote: 'https://jobs.go2scale.io/<job_name>.yml'
      - ...
    ```

    !!! note

        By default, the `latest` version of a job is used. You can choose to
        use a specific version using a `tag`. Available tags are described for
        each jobs in [Jobs section](/jobs/). Description of `tag` format is
        available in [Versioning page](/versioning/).

        Once your pipeline is functional, we recommend to use specific version
        for jobs in order to ensure that your pipeline will not be broken by a
        job update.

3. Jobs can be customized 👉 check the [jobs
   customization](#jobs-customization) section.

4. Everything is ready! You can now benefit the full power of a CI / CD
   pipeline 🎉🚀

    !!! tip
        You can also combine jobs templates and your own jobs in
        `.gitlab-ci.yml` configuration file.

### 🏳󠁵󠁳󠁴󠁸󠁿 Example


An example of a full `.gitlab-ci.yml` file with:

* One job template with latest version. Note that `latest/` is optional in the
  job URL
* One job template with specific version using tag `2020-06-22_1`
* A custom `unit_tests` job

``` yaml
stages:
  - static_tests
  - build
  - dynamic_tests
  - review
  - deployment

# Jobs from g2s hub
include:
  - remote: 'https://jobs.go2scale.io/latest/docker.yml'
  - remote: 'https://jobs.go2scale.io/2020-06-22_1/mkdocs.yml'

# You can also include your own jobs
unit_tests:
  image: python:3.7-alpine3.10
  stage: static_tests
  before_script:
    - apk add gcc make musl-dev postgresql-dev git linux-headers libmagic jpeg-dev zlib-dev
    - pip install pipenv && pipenv --bare install --dev
  script:
    - make test
```

## ▶ Stages

By default, each job from the hub is a part of on these stages:

* **🔎 Static_tests:** static tests launched on repository file
* **📦 Build:** build and packaging of software
* **🛡 Dynamic_tests:** dynamic tests launched on a running version of the software
* **🙋 Review:** deployment of the software in an isolated review environment
* **🚀 Deployment:** deployment of the software on real environments

This is an efficient and simple workflow. Nevertheless, if you want to use your
own custom stage list: you can re-declare yourself the stage of any job from
the hub. Follow the [customization section](#jobs-customization) to do it.

## 🔧 Jobs customization

🚧 *Work in progress*

<!-- TODO: describe how to override a job (part of
https://gitlab.com/go2scale/hub/-/issues/14) -->
