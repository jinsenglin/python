# fab delivery:config=config.yaml
def delivery(config=None):
    if config:
        import yaml
    
        f = open(config, 'r')
        y = yaml.load(f)
        f.close()
    
        # DSL
        if y['version'] == 1:
            print('compatible')
    
            if y['destination'] == 'vagrant-vb':
                print(y['vagrant-vb']['box'])
    
            elif y['destination'] == 'vagrant-kvm':
                print(y['vagrant-kvm']['box_url'])
    
            else:
                print("unsupported")
    
        else:
            print("incompatible")
    else:
        print("missing config file")
