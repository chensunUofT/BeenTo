# BeenTo

Web application to keep track of IPs and locations

## Idea

回头再写。

## Run
locally (for testing):  
`export FLASK_APP=BeenTo.py`  
`flask run`  
on my VPS environment:  
`uwsgi --http :9090 --wsgi-file BeenTo.py --callable app`  
