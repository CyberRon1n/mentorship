import requests
res=requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('there was a problem: %s' % (exc))
    
