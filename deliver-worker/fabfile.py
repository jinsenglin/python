import yaml
from fabric.api import lcd, local, cd, run, sudo, put, get

# fab delivery:config=config.yaml
def delivery(config=None):
    if config:
    
        f = open(config, 'r')
        y = yaml.load(f)
        f.close()
    
        # DSL
        if y['version'] == 1:
            print('compatible')
    
            if y['destination'] == 'vagrant-vb':
                with lcd(y['vagrant-vb']['vagrantfile_location']):
                    local('vagrant up')
    
            elif y['destination'] == 'vagrant-kvm':
                print(y['vagrant-kvm']['box_url'])
    
            else:
                print("unsupported")
    
        else:
            print("incompatible")
    else:
        print("missing config file")
