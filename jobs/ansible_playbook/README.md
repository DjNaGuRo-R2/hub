## Objective

This job will run an [`ansible-playbook`](https://docs.ansible.com/ansible/latest/user_guide/playbooks.html) command to automate deployments. You can install multiple roles from a `requirements.yml` file, see the [documentation](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file).

## How to use it

1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`. 
2. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
3. Well done, your job is ready to work ! 😀

## Job details

* Job name: `ansible_playbook`
* Docker image:
[`alpine:3.15.1`](https://hub.docker.com/r/_/alpine)
* Default stage: `deploy`
* When: `always`

### Variables

| Name                                      | Description                                                                                                                                       | Default              |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| `ANSIBLE_WORKSPACE` <img width=100/>      | The path where is located your ansible project <img width=175/>                                                                                   | `.` <img width=100/> |
| `ANSIBLE_INVENTORY_FILE` <img width=100/> | The inventory file where are described roles and groups. This variable should be specified in `Gitalb > CI/CD Settings` as file. <img width=175/> | ` ` <img width=100/>  |
| `SSH_PRIVATE_KEY_FILE` <img width=100/>   | ⚠️ Mandatory variable. The name of your private SSH key. his variable should be specified in `Gitalb > CI/CD Settings` as file. <img width=175/>   | ` ` <img width=100/>  |
| `ADDITIONAL_OPTIONS` <img width=100/>     | Other [options](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html#common-options) you may want to use<img width=175/>             | ` ` <img width=100/>  |