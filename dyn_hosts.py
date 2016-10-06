#!/usr/bin/env python
"""
{
    "databases"   : {
        "hosts"   : [ "host1.example.com", "host2.example.com" ],
        "vars"    : {
            "a"   : true
        }
    },
    "webservers"  : [ "host2.example.com", "host3.example.com" ],
    "atlanta"     : {
        "hosts"   : [ "host1.example.com", "host4.example.com", "host5.example.com" ],
        "vars"    : {
            "b"   : false
        },
        "children": [ "marietta", "5points" ]
    },
    "marietta"    : [ "host6.example.com" ],
    "5points"     : [ "host7.example.com" ]
}
"""
import argparse
import json

import requests


class HostAggr(object):

    def __init__(self):
        self._roles = {}

    def _default_role(self, role):
        return {'hosts': [], 'vars': {'roles': [role]}}

    def add_host(self, role, host, domain):
        if host != 'global':
            if role not in self._roles:
                self._roles[role] = self._default_role(role)
            fqdn = host + '.' + domain
            self._roles[role]['hosts'].append(fqdn)

    def serialize(self):
        return json.dumps(self._roles, indent=4)

def list_hosts(config):
    aggr = HostAggr()
    for server, domain in config['servers'].iteritems():
        resp = requests.get('http://{}/v1/zones'.format(server))
        data = resp.json()
        for zone in data['zones']:
            name = zone['name']
            role = determine_role(name)
            aggr.add_host(role, name, domain)
    print aggr.serialize()

def determine_role(name):
    parts = name.split('-')
    if len(parts) == 1:
        role = name
    else:
        role = parts[1]
    return role



def host_vars(config, host):
    return {'_meta': {'hostvars': {}}}

def get_config():
    with open('dyn_hosts_config.json') as f:
        data = json.loads(f.read())
    return data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action = 'store_true')
    parser.add_argument('--host', action = 'store')
    args = parser.parse_args()
    config = get_config()
    if args.list:
        list_hosts(config)
    elif args.host:
        host_vars(config, args.host)

if __name__ == '__main__':
    main()
