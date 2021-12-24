## Objective

This job test your front end web application by running tests headlessly in a CI context.

To ensure that the job work you have to specify the URL of your server (Example: http://localhost:4200 for Angular web App). It's used to prevent Cypress runs before your web sever is up and available. You can see more [here](https://docs.cypress.io/guides/continuous-integration/introduction#Boot-your-server)

## How to use it

1. Ensure yourself that your project is set to use Cypress. You can refer to the [Cypress Getting Started](https://docs.cypress.io/guides/getting-started/installing-cypress). If you want to connect your GitLab instance with the Cypress Dashboard to see there your job records - in case that you override the `CYPRESS_RECORD_KEY`, you can set up your project by following the [Cypress Dashboard documentation](https://docs.cypress.io/guides/dashboard/gitlab-integration#Installing-the-GitLab-integration).

**Override CYPRESS_BASE_URL variable. It's MANDATORY** 
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/cypress_run.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `cypress_run`
* Docker image:
[`cypress/browsers:node16.5.0-chrome94-ff93`](https://hub.docker.com/r/cypress/browsers)
* Default stage: `dynamic_tests`
* When: `always`

### Variables

| Name | Description | Default | 
| ---- | ----------- | ------- |
| `CYPRESS_CONFIG_FILE` | Specify a config file to use | `cypress.json` |
| `CYPRESS_PROJECT_PATH` | Path to project dir | `.` |
| `CYPRESS_RECORD_KEY` | Specify a record key in order to get a video of tests | ` ` |
| `CYPRESS_RECORDER` | Name of the reporter used | `spec` |
| `CYPRESS_BASE_URL`  | **(MANDATORY)** The base URL of your server | ``|
| `ADDITIONAL_OPTIONS` | Additional options to the run | ` ` |
