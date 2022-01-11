## Objective

This job checks your code quality inside your Angular application. It uses a custom lint script of your choices. Check the [Angular documentation](https://angular.io/cli/lint){:target="_blank"} if you need more information.

## How to use it

1. Make sure that your project has 
      [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
1. If you don't already have a lint package installed in your project, you must specified the `NG_LINT_PACKAGE` variable.
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/ng_lint.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `ng_lint`
* Docker image:
[`node:16.13.1-buster`](https://hub.docker.com/r/_/node){:target="_blank"}
* Default stage: `static_tests`
* When: `always`

### Variables

!!! info
    If you already have a package that will be used by the `ng lint` command, you don't have to override the `NG_LINT_PACKAGE` variable.

!!! info
    If you don't have a `defaultProject` value in your `angular.json` file, you have to override the `PROJECT_NAME` variable.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=100/> | Path to the root of project. <img width=175/>| `.` <img width=100/>|
| `PROJECT_NAME` <img width=100/> | Project name specified in the `projects` section of the `angular.json` workspace configuration file. <img width=175/>| ` ` <img width=100/>|
| `NG_LINT_OPTIONS` <img width=100/> | Additional options for `ng lint`. <img width=175/>| ` ` <img width=100/>|
| `NG_LINT_PACKAGE` <img width=100/> | Name of the package used by the `ng lint` command in order to lint the project <img width=175/>| ` ` <img width=100/>|