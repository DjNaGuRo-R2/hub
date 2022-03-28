# Changelog
All notable changes to this job will be documented in this file.

## [0.3.0] - 2021-04-23
* Upgrade image `node` from `15.4` to `15.14`

## [0.2.2] - 2021-03-29
* Add `NEWMAN_ENVIRONMENT_FILE` variable
* Update job image from `node:15.10.0` to `node:15.12.0`

## [0.2.1] - 2021-03-03
* Update docker image version to `15.10.0`
* Fix version of `newman` package to `5.2.2` through variable `NEWMAN_VERSION`
* Fix version of `newman-reporter-junitfull` package to `1.1.1` through variable `NEWMAN_JUNIT_VERSION`

## [0.2.0] - 2021-01-13
* Fix doubly named variable `NEWMAN_FAIL_ON_ERROR` (remove `NEWMAN_EXIT_ON_ERROR`)
* `NEWMAN_FAIL_ON_ERROR` default value is now `true`
* Allow specifying number of iterations through variable `NEWMAN_ITERATIONS_NUMBER` with 2 as default value
* Add the `cli` report in log output in addition to `junit`
* Add `junit` report as user-reachable artifact in addition to the report integration

## [0.1.0] - 2020-12-28
* Initial version