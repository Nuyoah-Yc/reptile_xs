import frida
import time
import ctypes
import hashlib
import random
import uuid
import time
import gzip
import requests
from urllib.parse import quote_plus
from urllib.parse import urlencode


def md5(data_string):
    obj = hashlib.md5()
    obj.update(data_string.encode("utf-8"))
    return obj.hexdigest()


def create_random_mac(sep=":"):
    """ 随机生成mac地址 """

    def mac_same_char(mac_string):
        v0 = mac_string[0]
        index = 1
        while index < len(mac_string):
            if v0 != mac_string[index]:
                return False
            index += 1
        return True

    data_list = []
    for i in range(1, 7):
        part = "".join(random.sample("0123456789ABCDEF", 2))
        data_list.append(part)
    mac = sep.join(data_list)

    if not mac_same_char(mac) and mac != "00:90:4C:11:22:33":
        return mac

    return create_random_mac(sep)


def create_cdid():
    return str(uuid.uuid4())


def create_openudid():
    # return "".join([hex(i)[2:] for i in random.randbytes(10)])
    return "".join([hex(i)[2:] for i in [random.randint(1, 255) for i in range(10)]])


def m44417a(barr):
    def int_overflow(val):
        maxint = 2147483647
        if not -maxint - 1 <= val <= maxint:
            val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
        return val

    def unsigned_right_shift(n, i):
        # 数字小于0，则转为32位无符号uint     n>>>i
        if n < 0:
            n = ctypes.c_uint32(n).value
        # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
        if i < 0:
            return -int_overflow(n << abs(i))
        # print(n)
        return int_overflow(n >> i)

    char_array = "0123456789abcdef"
    result = ['' for i in range(len(barr) * 2)]
    for i in range(len(barr)):
        i2 = barr[i] & 255
        i3 = i * 2
        result[i3] = char_array[unsigned_right_shift(i2, 4)]  # i2>>>4
        result[i3 + 1] = char_array[i2 & 15]
    return ''.join(result)


def get_frida_rpc_script():
    rdev = frida.get_remote_device()
    session = rdev.attach("抖音短视频")
    scr = """
    rpc.exports = {   
        ttencrypt:function(bArr,len){
             var res;

             Java.perform(function () {
                var EncryptorUtil = Java.use("com.bytedance.frameworks.encryptor.EncryptorUtil");  

                // 将bArr转换成Java的字节数组。
                var dataByteArray = Java.array('byte',bArr);

                // 调用native方法，并获取返回值。
                res = EncryptorUtil.ttEncrypt(dataByteArray,len);
             });

             return res;
        },
        execandleviathan: function (i2,str){
            var result;
            Java.perform(function () {
                // 先处理拼接好的数据（字节数组）
                var bArr = [];
                for(var i=0;i<str.length;i+=2){
                    var item = (parseInt(str[i],16) << 4) + parseInt(str[i+1],16);
                    bArr.push(item);
                }

                // 转换为java的字节数组
                var dataByteArray = Java.array('byte',bArr);

                // 调用leviathan方法
                var Gorgon = Java.use("com.ss.sys.ces.a");
                result = Gorgon.leviathan(-1, i2 , dataByteArray);   //leviathan为方法名
            });
            return result;
        }
    }
    """
    script = session.create_script(scr)
    script.load()
    return script


def get_gorgon(script, param_string, cookie_string):

    # 7.变量a，对URL参数进行md5加密，生成 a
    ha = hashlib.md5()
    ha.update(param_string.encode('utf-8'))
    a = ha.hexdigest()

    # 8.变量str7（get请求时是000.。，post请求时是x_ss_stud ）
    str7 = '00000000000000000000000000000000'

    # 9.变量str8，对cookie的md5加密（抓包注册设备时cookie是空的；获取评论时cookie才有值）
    if cookie_string:
        str8 = md5(cookie_string)  # 00000000000000000000000000000000 也可以，说明cookie不是必须的。
    else:
        str8 = "00000000000000000000000000000000"

    # 10.变量str9，sessionid的md5（无）
    str9 = "00000000000000000000000000000000"

    # 11.拼接变量
    un_sign_string = "{}{}{}{}".format(a, str7, str8, str9)

    # 12.m44418a处理 + 执行so中的leviathan
    khronos = int(time.time())
    gorgon_byte_list = script.exports.execandleviathan(khronos, un_sign_string)

    # 13.m44417a处理
    gorgon = m44417a(gorgon_byte_list)
    return gorgon, khronos


def get_comment_list():
    """ 获取评论 """
    script = get_frida_rpc_script()


    mac_addr = create_random_mac()
    cdid = create_cdid()
    openudid = create_openudid()
    _rticket = int(time.time() * 1000)  # 1662623963894
    ts = int(time.time())

    device_id = "1324270467154856"
    iid = "3408905239797464"

    # 在获取评论时，没啥用；可以删除 & 可以是空 & 可以是其他值
    ttreq = ""
    odin_tt = ""

    param_dict = {
        "aweme_id": "7134390831976434951",
        "cursor": "0",
        "count": "20",
        "address_book_access": "2",
        "gps_access": "2",
        "forward_page_type": "1",
        "channel_id": "0",
        "city": "130400",
        "hotsoon_filtered_count": "0",
        "hotsoon_has_more": "0",
        "follower_count": "0",
        "is_familiar": "0",
        "page_source": "0",
        "manifest_version_code": "110501",
        "_rticket": _rticket,
        "app_type": "normal",
        "iid": iid,
        "channel": "gdt_growth14_big_yybwz",
        "device_type": "M2007J17C",
        "language": "zh",
        "cpu_support64": "true",
        "host_abi": "armeabi-v7a",
        "resolution": "1080*2189",
        "openudid": openudid,
        "update_version_code": "11509900",
        "cdid": cdid,
        "os_api": "29",
        "mac_address": mac_addr,
        "dpi": "408",
        "oaid": "",
        "ac": "wifi",
        "device_id": device_id,
        "mcc_mnc": "46001",
        "os_version": "10",
        "version_code": "110500",
        "app_name": "aweme",
        "version_name": "11.5.0",
        "device_brand": "Redmi",
        "ssmix": "a",
        "device_platform": "android",
        "aid": "1128",
        "ts": ts
    }

    param_string = urlencode(param_dict)
    print('拼接起来的URL参数--->', param_string)

    # 获取评论时候，有cookie
    # cookie_string = "install_id={}; ttreq={}; odin_tt={}".format(iid, ttreq, odin_tt)
    cookie_string = None
    gorgon, khronos = get_gorgon(script, param_string, cookie_string)

    res = requests.get(
        url="https://api26-normal-hl.amemv.com/aweme/v2/comment/list/",
        params=param_dict,
        headers={
            "user-agent": "com.ss.android.ugc.aweme/110501 (Linux; U; Android 10; zh_CN; Redmi 8A; Build/QKQ1.191014.001; Cronet/TTNetVersion:3c28619c 2020-05-19 QuicVersion:0144d358 2020-03-24)",
            "x-khronos": str(khronos),
            "x-gorgon": gorgon
        },
        cookies={
            "install_id": iid,
            "odin_tt": odin_tt
        }
    )

    print("\n\n\n -------获取评论------- \n\n")
    print(res.text)


if __name__ == '__main__':
    get_comment_list()