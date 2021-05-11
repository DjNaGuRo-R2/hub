## Objective

r2_jobdescription

## How to use it

1. <Your steps>
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/r2_jobname.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `r2_jobname`
* Docker image:
[`r2_imagename:r2_imagetag`](https://hub.docker.com/r/_/r2_imagename)
* Default stage: `r2_stage`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `VARIABLE` <img width=100/> | A general variable for this job <img width=175/>| `Hello R2` <img width=100/>|
