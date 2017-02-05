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
                    # launch machines
                    local('vagrant up')

                    # parse machines' ssh login information
                    mh = local('vagrant ssh-config monitor | grep "  HostName " | sed "s/  HostName //"', capture=True)
                    mp = local('vagrant ssh-config monitor | grep "  Port " | sed "s/  Port //"', capture=True)
                    mu = local('vagrant ssh-config monitor | grep "  User " | sed "s/  User //"', capture=True)
                    mk = local('vagrant ssh-config monitor | grep "  IdentityFile " | sed "s/  IdentityFile //"', capture=True)
                    th = local('vagrant ssh-config target | grep "  HostName " | sed "s/  HostName //"', capture=True)
                    tp = local('vagrant ssh-config target | grep "  Port " | sed "s/  Port //"', capture=True)
                    tu = local('vagrant ssh-config target | grep "  User " | sed "s/  User //"', capture=True)
                    tk = local('vagrant ssh-config target | grep "  IdentityFile " | sed "s/  IdentityFile //"', capture=True)
                    mhost = '{}@{}:{}'.format(mu, mh, mp)
                    thost = '{}@{}:{}'.format(tu, th, tp)

                    # set hosts
                    env.hosts = [mhost, thost]

                    # set roles
                    env.roledefs.update({
                        'monitor': [mhost],
                        'target': [thost],
                        })

                    # set key files
                    env.key_filename = []
                    env.key_filename.append(mk)
                    env.key_filename.append(tk)
    
            elif y['destination'] == 'hosts':
                # parse machines' ssh login information
                m = y['hosts']['monitor']
                t = y['hosts']['monitor']
                mh = '{}@{}:{}'.format(m['ssh_user'], m['ssh_host'], m['ssh_port'])
                th = '{}@{}:{}'.format(t['ssh_user'], t['ssh_host'], t['ssh_port'])

                # set hosts
                env.hosts = [mh, th]

                # set roles
                env.roledefs.update({
                    'monitor': [mh],
                    'target': [th],
                    })

                # set passwords and key files
                env.key_filename = []
                for k,v in y['hosts'].iteritems():
                    if v['ssh_auth_type'] == 'password':
                        h = '{}@{}:{}'.format(v['ssh_user'], v['ssh_host'], v['ssh_port'])
                        env.passwords[h] = v['ssh_pass']
                    elif v['ssh_auth_type'] == 'public-key':
                        env.key_filename.append(v['ssh_key_file']);

            elif y['destination'] == 'openstack':
                # TODO launch machines
                ks = y['openstack']['identity_v3']

                from libcloud.compute.types import Provider
                from libcloud.compute.providers import get_driver
                import libcloud.security
                libcloud.security.VERIFY_SSL_CERT = False
                cls = get_driver(Provider.OPENSTACK)
                driver = cls(ks['auth_user'], ks['auth_pass'],
                        ex_force_auth_version='3.x_password',
                        ex_force_auth_url=ks['auth_url'],
                        ex_domain_name=ks['auth_domain'],
                        ex_tenant_name=ks['auth_tenant'])
                print(driver.list_nodes())
                print(driver.list_sizes())
                print(driver.list_images())
                #node = driver.create_node(name='libcloud', size=size, image=image)

                # TODO parse machines' ssh login information
                # TODO set hosts
                # TODO set roles
                # TODO set key files
                pass
    
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

