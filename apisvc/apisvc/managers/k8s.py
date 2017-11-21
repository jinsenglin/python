from kubernetes import client, config


class Manager(object):
    def __init__(self, credential=None):
        self._credential = credential

    def demo(self):
        config.load_kube_config(config_file=self._credential)
        v1 = client.CoreV1Api()
        ret = v1.list_pod_for_all_namespaces(watch=False)
        for i in ret.items:
            print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))