## Objective

Clippy runs a format check onto your Rust project and logs any unexpected linting warning or error in your project into the pipeline.

## How to use it

1. By default, the job will not fail when encountering warnings or errors. If you want the job to fail, change `ADDITIONAL_OPTIONS` value to `-- -D clippy::all`.
1. If you want to add more options into the `clippy` command, please check the official [documentation](https://github.com/rust-lang/rust-clippy#readme){:target="_blank"}.
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/cargo_clippy.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization){:target="_blank"}
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `cargo_clippy`
* Docker image:
[`rust:1.57-buster`](https://hub.docker.com/r/_/rust){:target="_blank"}
* Default stage: `static_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=100/> | Relative to root of your repository, it is the path to your rust project <img width=175/>| `.` <img width=100/>|
| `ADDITIONAL_OPTIONS` <img width=100/> | Possibility to add more options into the command <img width=175/>| `-- -W clippy::all` <img width=100/>|
