''' @File :common.py @Author:张宇 @Date :2020/8/2 15:09 @Desc : '''

from qiniu import Auth, put_data, put_file

class Qiniu(object):
    AK = '2zdV4opbmFZaDcTF0yUfW25kymJrpWNpx3MtkUwM'
    SK = '2fw3FgmHRaoYdSyUca8A3clQKiowHDiL4FsusSEC'
    def __init__(self,bucket_name,base_url):
        # 存储空间名
        self.bucket_name = bucket_name
        # 外链域名
        self.base_url = base_url
        self.q = Auth(self.AK,self.SK)

    def put(self,name,data):
        token = self.q.upload_token(self.bucket_name,name)
        ret,info = put_data(token,name,data)

        if 'key' in ret:
            #获得完整的链接
            remote_url = '/'.join([self.base_url,ret['key']])
            #访问的链接
            return  remote_url
        else:
            return False

BUCKET_NAME = 'navcator'
BASE_URL = 'http://qg8pbwdiv.hd-bkt.clouddn.com'
video_qiniu = Qiniu(bucket_name=BUCKET_NAME,
                    base_url=BASE_URL)
