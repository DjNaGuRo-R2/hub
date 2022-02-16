# Changelog
All notable changes to this job will be documented in this file.

## [1.1.0] - 2021-06-21
* Allows context different from root with new variable `DOCKER_CONTEXT_PATH`

## [1.0.0] - 2021-05-07
* Breaking change in the configuration of custom registry, see documentation
* Add support to push in multiple registries
* Add support to authentication in multiple registries

## [0.4.0] - 2021-04-19
* Add new option `--use-new-run` to kaniko executor (enabled by default)
* Update kaniko image to `v1.5.1`

## [0.3.0] - 2020-11-25
* New variable `DOCKER_USE_CACHE` to be able to cache layers of build
* New variable `DOCKER_CACHE_TTL` to define time to live of cache
* New variable `DOCKER_VERBOSITY` to set the verbosity of the build
* New variable `DOCKER_OPTIONS` to be able to add additional options

## [0.2.0] - 2020-11-02
* Add variable `DOCKERFILE_PATH` which permits specifying custom path to
  Dockerfile

## [0.1.0] - 2020-10-21
* Initial version
