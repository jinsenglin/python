# Usage

```
pip install kafka-python
python main.py
```

Consume

```
kernel,host=2018-dib-machine.novalocal context_switches=27378340i,boot_time=1521789543i,processes_forked=304308i,interrupts=40374339i 1522216770000000000
```

Produce

```
{"metric": {"timestamp": 1522038535066.8818, "value_meta": null, "name": "kernel.context_switches", "value": 27378340i, "dimensions": {"hostname": "2018-dib-machine.novalocal"}}, "meta": {"region": "RegionOne", "tenantId": "40b90476ff244edeb3102875f46c36a2"}, "creation_time": 1522038538}
{"metric": {"timestamp": 1522038535066.8818, "value_meta": null, "name": "kernel.boot_time", "value": 1521789543i, "dimensions": {"hostname": "2018-dib-machine.novalocal"}}, "meta": {"region": "RegionOne", "tenantId": "40b90476ff244edeb3102875f46c36a2"}, "creation_time": 1522038538}
{"metric": {"timestamp": 1522038535066.8818, "value_meta": null, "name": "kernel.processes_forked", "value": 304308i, "dimensions": {"hostname": "2018-dib-machine.novalocal"}}, "meta": {"region": "RegionOne", "tenantId": "40b90476ff244edeb3102875f46c36a2"}, "creation_time": 1522038538}
{"metric": {"timestamp": 1522038535066.8818, "value_meta": null, "name": "kernel.interrupts", "value": 40374339i, "dimensions": {"hostname": "2018-dib-machine.novalocal"}}, "meta": {"region": "RegionOne", "tenantId": "40b90476ff244edeb3102875f46c36a2"}, "creation_time": 1522038538}
```
