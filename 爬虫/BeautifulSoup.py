import urllib.request
import urllib.parse

url='http://www.baidu.com/'
# 正常的方式进行访问
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
# }
# 携带cookie进行访问
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Accept-Language': ' zh-CN,zh;q=0.9'}
    #'Cookie': ' sysauth=c50fe86934b7baff6b60603660bfe4e4; comment_author_8baadd996acdd55230578be82aa9c68b=kolk; goSessionid=1-suIyO6nL1ZKIJOEbyz20qOq0pbTHLnN7Ss5Q6gD-g%3D; agh_session=9b61a59ed24ceb320c68229e2f243b2d9753f9d856f5cbaaf76396ccb6f3886c; stay_login=1; wp-settings-time-1=1609409731; wp-settings-1=libraryContent%3Dbrowse%26mfold%3Do%26editor%3Dtinymce; login=1; username=admin; SESSIONID=b0797e25-55bf-454d-ba45-f502d77e3ffe.Vz_8dsg1LYeYrVubGiPyq0u_aBg; request_token=YdVf7bVzOgAoYuumHRQ9pOHdgVZklgxkSQCptLVLFHJxouz4; ltd_end=-1; pro_end=-1; serverType=nginx; order=id%20desc; memSize=738; site_table_limit=20; sites_path=/www/wwwroot; id=CLnyZpKmO4qopjPH0nGOw1O0e9sMPISIWKDOb-lQ3cQ6fFyzY0s7zvltZ3o2bOGhfrgNog56mB45ANNSXG5o8s; smid=28qH0CFIXx7MoSDJgssfGAWyqTCENOcR3ETB8FVCAcumMMQCIqX_rKinkuJEBbZm_jnq83upt2t4a-yQGcERmA',

request=urllib.request.Request(url=url, headers=headers)
response=urllib.request.urlopen(request)
# 输出所有
# print(response.read().decode('gbk'))
# 将内容写入文件中
with open('D:/123456.html', 'wb') as fp:
    fp.write(response.read())