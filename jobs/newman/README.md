# 🚀 Newman

## Description

Launch a Postman collection of requests to test your API using [newman](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/)

## How to use it

1. Add a Postman collection to your project
2. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/newman.yml'
    ```
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀

## Job details

* Job name: `newman`
* Docker image:
[`node:15.0.4`](https://hub.docker.com/r/_/node)
* Default stage: `dynamic_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `NEWMAN_COLLECTION` <img width=100/> | Name of the Postman collection <img width=175/> | `postman_collection.json` <img width=100/> |
