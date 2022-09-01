import requests

def get_html(url = 'http://stat.ruc.edu.cn/Home/People/Faculty/b3a208a052844c1e90df60c6e3f2f3d9.htm'):
    headers={'user-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
    
    
    
    response = requests.get(url,headers=headers)
    
    response.encoding='utf-8'
    
    
    
    return response
