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
                    # TODO set roles
    
            elif y['destination'] == 'hosts':
                print(y['hosts']['monitor'])
                print(y['hosts']['target'])
                # TODO set roles
                env.roledefs.update({
                    'monitor': [y['hosts']['monitor']['ssh_host']],
                    'target': [y['hosts']['target']['ssh_host']],
                    })
    
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

