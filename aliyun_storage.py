# 上传一张图片到阿里云
import oss2

from config import Config


class AliyunStorage(object):
    """阿里云存储"""

    def __init__(self, access_key_id=None, access_key_secret=None, endpoint=None, bucket_name=None):
        self.access_key_id = access_key_id or Config.access_key_id
        self.access_key_secret = access_key_secret or Config.access_key_secret
        self.endpoint = endpoint or Config.inner_endpoint
        self.bucket_name = bucket_name or 'testleqi'

    def __get_bucket(self):
        bucket = oss2.Bucket(oss2.Auth(self.access_key_id, self.access_key_secret), self.endpoint, self.bucket_name)
        return bucket

    def getfile(self, key):
        """根据key从阿里云获取对应的文件内容"""
        bucket = self.__get_bucket()
        try:
            content = bucket.get_object(key)
            return content.read()
        except Exception as e:
            raise (e)

    def sendfile(self, key, file):
        """上传文件到阿里云云端"""
        bucket = self.__get_bucket()
        try:
            bucket.put_object_from_file(key, file)
            return True,
        except Exception as e:
            return False, e

    def sendfile__data(self, key, file):
        """将文件上传到阿里云"""
        bucket = self.__get_bucket()
        try:
            bucket.put_object(key, file)
            return True,
        except Exception as e:
            return False, e

    def get_pic_url(self, key):
        """根据key获取文件的url"""
        bucket = self.__get_bucket()
        return bucket.sign_url('GET', key, 300)

    def gen_pic_url(self, key):
        """根据key生成文件的url"""
        bucket = self.__get_bucket()
        return bucket.sign_url('PUT', key, 3600)

    def exist_file(self, key):
        """根据key,判断文件是否在云端存在"""
        bucket = self.__get_bucket()
        exist = bucket.object_exists(key)
        return exist
