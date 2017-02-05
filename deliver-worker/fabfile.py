import yaml
from fabric.api import lcd, local, cd, run, sudo, put, get, env, hosts, roles

# fab set_hosts:config=config.yaml
def set_hosts(config=None):
    if config:

        with open(config, 'r') as f:
            y = yaml.load(f)
    
        # DSL
        if y['version'] == 1:
            print('compatible')
    
            if y['destination'] == 'vagrant-vb':
                with lcd(y['vagrant-vb']['vagrantfile_location']):
                    local('vagrant up')
                    # TODO set hosts
                    # TODO set roles
                    # TODO set key files
    
            elif y['destination'] == 'hosts':
                # set hosts
                monitor = '{}@{}:{}'.format(y['hosts']['monitor']['ssh_user'], y['hosts']['monitor']['ssh_host'], y['hosts']['monitor']['ssh_port'])
                target = '{}@{}:{}'.format(y['hosts']['target']['ssh_user'], y['hosts']['target']['ssh_host'], y['hosts']['target']['ssh_port'])
                env.hosts = [monitor, target]

                # set roles
                env.roledefs.update({
                    'monitor': [monitor],
                    'target': [target],
                    })

                # set passwords and key files
                env.key_filename = []
                for k,v in y['hosts'].iteritems():
                    if v['ssh_auth_type'] == 'password':
                        h = '{}@{}:{}'.format(v['ssh_user'], v['ssh_host'], v['ssh_port'])
                        env.passwords[h] = v['ssh_pass']
                    elif v['ssh_auth_type'] == 'public-key':
                        env.key_filename.append(v['ssh_key_file']);
    
            else:
                print("unsupported")
    
        else:
            print("incompatible")
    else:
        print("missing config file")

# fab deliver_monitor:config=config.yaml
@roles('monitor')
def deliver_monitor(config=None):
    if config:

        with open(config, 'r') as f:
            y = yaml.load(f)
    
        # DSL
        if y['version'] == 1:
            print('compatible')
    
            if y['destination'] == 'vagrant-vb':
                # TODO run
                run('hostname')
    
            elif y['destination'] == 'hosts':
                # TODO run
                run('hostname')
    
            else:
                print("unsupported")
    
        else:
            print("incompatible")
    else:
        print("missing config file")

# fab deliver_target:config=config.yaml
@roles('target')
def deliver_target(config=None):
    if config:

        with open(config, 'r') as f:
            y = yaml.load(f)
    
        # DSL
        if y['version'] == 1:
            print('compatible')
    
            if y['destination'] == 'vagrant-vb':
                # TODO run
                run('hostname')
    
            elif y['destination'] == 'hosts':
                # TODO run
                run('hostname')
    
            else:
                print("unsupported")
    
        else:
            print("incompatible")
    else:
        print("missing config file")

