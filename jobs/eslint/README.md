## Objective

ESLint statically analyzes your code to quickly find problems in your JavaScript code. This tools is highly customizable with lots of plugins, and is a great way to find potential problems in your code. Check out the [ESLint documentation](https://eslint.org/docs/user-guide/configuring) for more information.

## How to use it


1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/eslint.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `eslint`
* Docker image: [`node:18-buster`](https://hub.docker.com/r/_/node)
* Default stage: `tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=100/> | Path to the root of project <img width=175/>| `.` <img width=100/>|
| `ESLINT_SOURCE` <img width=100/> | Relative path to the directory to lint <img width=175/>| `./src` <img width=100/>|
| `ESLINT_VERSION` <img width=100/> | Version for ESLint <img width=175/>| `8.17.0` <img width=100/>|
| `REPORT_OUTPUT` <img width=100/> | Output file used for Junit tests. None if empty <img width=175/>| `junit-report.xml` <img width=100/>|
| `ADDITIONAL_OPTIONS` <img width=100/> | Additional [options](https://eslint.org/docs/user-guide/command-line-interface) for ESLint <img width=175/>| ` ` <img width=100/>|

### Configuration file

YOu should write your configuration in a file called `.eslintrc` in the root of your project.
They are plenty of plugins available for ESLint, you can choose the right one depending of your configuration. In top of that, the [Airbnb](https://www.npmjs.com/package/eslint-config-airbnb) is one of the most popular and used as a base for your configuration.

Here are some example of configuration files for some technologies:

#### React:

```json
{
  "env": {
    "browser": true,
    "es2021": true
  },
  "extends": [
    "plugin:react/recommended",
    "airbnb"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaFeatures": {
      "jsx": true
    },
    "ecmaVersion": "latest",
    "sourceType": "module"
  },
  "plugins": [
    "react",
    "@typescript-eslint"
  ]

}
```

#### NextJS:

```json
{
  "extends": [
    "next/core-web-vitals",
    "airbnb",
    "airbnb/hooks",
    "airbnb-typescript",
    "prettier"
  ],
  "parserOptions": {
    "project": "./tsconfig.json"
  }
}
```



### Docusaurus:
```js
module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: [
    'plugin:react/recommended',
    'airbnb',
  ],
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  plugins: [
    'react',
  ],
  rules: {
  },
};
```

