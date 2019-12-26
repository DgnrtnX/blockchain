**Activation virtual env**
```
for windows:

project_path\venv\Scripts\
.\activate

for mac/linux:
source env-name/bin/activate
``` 

**Install packages**
```
pip3 install -r install requirementss.txt
```

**test**
 : start the virtual env

```
python3 -m pytest backend\test
```

**Run the application and API**
```
python3 -m backend.app
```

**Run Peer Instance**
: Activate env
```
export PEER = True && python3-m backend.app
```

**Frontend**
```
npm start
```
**SEED backend with DATA**
```
export SEED_DATA=True && python3 -m backend.app
```
