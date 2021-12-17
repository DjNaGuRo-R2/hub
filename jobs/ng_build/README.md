## Objective

Compiles an Angular app into an output directory named dist/ at the given output path. Must be executed from within a workspace directory.
The application builder uses the webpack build tool, with default configuration options specified in the workspace configuration file (angular.json) or with a named alternative configuration. Check the [Angular documentation](https://angular.io/cli/build){:target="_blank"} if you need more information. 

## How to use it

1. Ensure that your project has
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
   file which contains the script required to build (`build` by default)
1. You should specify your project name in the `PROJECT_NAME` variable, you can find it in your `angular.json` file under the `projects` section. You don't have to go through this step if there is a `defaultProject` value in your `angular.json` because the `ng build` command will be executed on the  `defaultProject`.
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/ng_build.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `ng_build`
* Docker image:
[`node:16.13.1-buster`](https://hub.docker.com/r/_/node){:target="_blank"}
* Default stage: `build`
* When: `always`

### Variables

| Name | Description                                                                                                                                                                                                          | Default              |
| ---- |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| `PROJECT_ROOT` <img width=100/> | Path to the root of project. <img width=175/>                                                                                                                                                                        | `.` <img width=100/> |
| `PROJECT_NAME` <img width=100/> | Project name specified in the `projects` section of the `angular.json` workspace configuration file. If no `PROJECT_NAME` have been specified it will execute the `ng build` command on the `defaultProject` specified in the `angular.json` file. <img width=175/>                                                                                                | ` ` <img width=100/> |
| `NG_BUILD_OPTIONS` <img width=100/> | Additional options available for the user, they are added at the end of build command. Check the different options in the official [documentation](https://angular.io/cli/build){:target="_blank"}. <img width=175/> | ` ` <img width=100/> |
| `OUTPUT_PATH` <img width=100/> | Path to the output produced by the `ng` build script used (path relative from the `PROJECT_ROOT`) <img width=175/>                                                                                                   | `website_build/` <img width=100/> |
