def hello():
    print("hello")

def dump():
    import yaml

    f = open("config.yaml", "r")
    y = yaml.load(f)
    f.close()

    print(y)

def main():
    import yaml

    f = open("config.yaml", "r")
    y = yaml.load(f)
    f.close()

    # DSL
    if y['version'] == "1.0.0":
        print("compatible")

    else:
        print("incompatible")
