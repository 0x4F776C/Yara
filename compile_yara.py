import yara

rules=yara.compile(filepaths={
    'namespace1':'/opt/CAPEv2/data',
    'namespace2':'/opt/CAPEv2/data/yara/CAPE',
    'namespace3':'/opt/CAPEv2/data/yara/memory',
    'namespace4':'/opt/CAPEv2/data/yara/depricated',
    'namespace5':'/opt/CAPEv2/data/yara/binaries',
    'namespace6':'/opt/CAPEv2/analyzer/windows/data/yara/windows',
    'namespace7':'/usr/local/lib/python3.8/dist-packages/malwareconfig/yaraRules'
})

#rules=yara.load('/dev/shm/compiled_rules')

rules.save('/dev/shm/compiled_rules')

''' References
https://yara.readthedocs.io/en/stable/yarapython.html
'''
