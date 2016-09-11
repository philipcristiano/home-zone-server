# Servers

My home server configs

## Running
Paths in the virtualenv are messed up, need to figure out why, but for now just
run directly from the venv.

    ANSIBLE_LIBRARY="ansible/modules-extras" /Users/philipcristiano/virtualenvs/home-server/bin/ansible-playbook -u root bootstrap.yml -i hosts
