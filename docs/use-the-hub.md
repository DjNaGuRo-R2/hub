# Use the hub

## π Prerequisites

- π¦  Manage your project in Gitlab
- βοΈ   Have the write access to the `.gitlab-ci.yml` file in your project
- π«  Be aware each file modification in your project will trigger the pipeline
- π  Have access to the Pipelines page in your Gitlab project to see the pipeline execution

## β³ Quick setup

Follows these steps to setup your CI/CD pipeline in less than 5 minutes !

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
      - remote: 'https://jobs.r2devops.io/<job_name>.yml'
      - remote: 'https://jobs.r2devops.io/<job_name>.yml'
      - ...
    ```

    !!! note

        By default, the `latest` version of a job is used. You can choose to
        use a specific version using a `tag`. Available tags are described for
        each job in [Jobs section](/jobs/). Description of `tag` format is
        available in [Versioning page](/versioning/).

        Once your pipeline is functional, we recommend to use a specific version
        for jobs in order to ensure that your pipeline will not be broken by a
        job update.

3. Jobs can be customized π check the [jobs
   customization](#jobs-customization) section.

4. Everything is ready! You can now benefit the full power of a CI / CD
   pipeline ππ

    !!! tip
        You can also combine jobs templates and your own jobs in
        `.gitlab-ci.yml` configuration file.

### π³σ ΅σ ³σ ΄σ Έσ Ώ Example


An example of a full `.gitlab-ci.yml` file with:

* One job template with latest version. Note that `latest/` is optional in the
  job URL
* One job template with specific version using tag `0.1.0`
* Your own local `unit_tests` job

``` yaml
stages:
  - static_tests
  - build
  - dynamic_tests
  - review
  - deployment

# Jobs from g2s hub
include:
  - remote: 'https://jobs.r2devops.io/latest/docker_build.yml'
  - remote: 'https://jobs.r2devops.io/0.1.0/mkdocs.yml'

# You can also include your own local jobs
unit_tests:
  image: python:3.7-alpine3.10
  stage: static_tests
  before_script:
    - pip install pipenv && pipenv --bare install --dev
  script:
    - make test
```

<a alt="See all jobs" href="/jobs">
    <button class="md-button border-radius-10 md-button-center" >
        See all jobs available <img alt="" class="heart" src="../images/rocket.png">
    </button>
</a>

## βΆ Stages

By default, each job from the hub is a part of on these stages:

* **π Static_tests:** static tests launched on repository file
* **π¦ Build:** build and packaging of software
* **π‘ Dynamic_tests:** dynamic tests launched on a running version of the software
* **π Review:** deployment of the software in an isolated review environment
* **π Deployment:** deployment of the software on real environments

This is an efficient and simple workflow. Nevertheless, if you want to use your
own custom stage list: you can re-declare yourself the stage of any job from
the hub. Follow the [customization section](#jobs-customization) to do it.

## π§ Jobs customization

### π Global

Each jobs of the hub can be customized. To do it, you have to include the job
URL as usual and, in addition, override the options you want to customize.

!!! tip
    In this way, you can override all Gitlab jobs parameters. All parameters
    are described in [Gitlab
    documentation](https://docs.gitlab.com/ee/ci/yaml/){:target="_blank"}.

For example, if you want to use the [trivy_image](/jobs/dynamic_tests/trivy_image/) job and
customize it by:

* Redefining the `stage` to `security` to fit in your personal stages workflow
* Set the variable `TRIVY_VERSION` to `0.9.1` to use this version instead of
  the default
* Set the variable `TRIVY_SEVERITY` to `CRITICAL` to display only CRITICAL
  issues

```yaml
include:
  - remote: 'https://jobs.r2devops.io/trivy_image.yml'

trivy_image:
  stage: security
  variables:
    TRIVY_VERSION: "0.9.1"
    TRIVY_SEVERITY: "CRITICAL"
```

### π³ Advanced: `services`

You may want one of your job to interact with a container instance (API,
database, web server...) to work. GitLab has an option to run a container next
to a job: [`services`](https://docs.gitlab.com/ee/ci/yaml/#services).

To use this option, you must have access to an image of the container you want
to run as a service. For example, if you are using our
[docker_build](https://r2devops.io/jobs/build/docker_build/) job to build an
image of your application, and you want to test this image using the
[nmap](/jobs/dynamic_tests/nmap/) job, just add the following configuration in
your `.gitlab-ci.yml` file:

!!! info
    * The `name` option must contain your image name and tag or an image name from [Docker Hub](https://hub.docker.com){:target="_blank"}.
    * The `alias` option permits to the job to reach your application using a name. This name
    must be the same that the one specified inside the job target's variable.
    * You may also run some other services like a database depending on your application needs.

```yaml
nmap:
  services:
    - name: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
      alias: app
```
