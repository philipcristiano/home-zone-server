# Servers

My home server configs

## Running
Paths in the virtualenv are messed up, need to figure out why, but for now just
run directly from the venv.

    ANSIBLE_LIBRARY="ansible/modules-extras" /Users/philipcristiano/virtualenvs/home-server/bin/ansible-playbook -u root bootstrap.yml -i hosts

### Deploying Zone Man

Set `zone_man_pkgsrvr` for publishing

    ANSIBLE_LIBRARY=ansible/modules-extras ansible-playbook -u root  -i hosts -v --limit zmbuild deploy_zm.yml --extra-vars 'zone_man_ref=man zone_man_pkgsrvr=SERVER'
