import yaml
import os

path = "./powershell_downgrade_attack.yml"
file = open(path,'r')

class rule():
    def __init__(self ):
        self.title = ""
        self.status = ""
        self.description = ""
        self.author = ""
        self.references = ""
        self.logsource = ""
        self.detection = ""
        self.fields = ""
        self.falsepositives = ""
        self.level = ""
        self.tags = ""

yamls = yaml.safe_load(file)
boom = rule()

for key, value in yamls.items():
    if(hasattr(boom, key)):
        setattr(boom, key, value)
    else:
        print("Key Not account for Key: {}  Value: {}".format(key, str(value)))

print(yaml.dump(boom, default_flow_style=False, sort_keys=False))

file.close()