import json

def readConfig(fileName):
    with open(str(fileName), "r") as f:
        w = f.read()
    
    fin = json.loads(w)
    return fin


def updateConfig(content, fileName):
    w = json.dumps(content)
    
    with open(fileName, "w") as f:
        f.write(w)


