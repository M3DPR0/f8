# uncompyle6 version 3.3.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Apr 24 2019, 10:05:31) 
# [GCC 4.2.1 Compatible Android (5058415 based on r339409) Clang 8.0.2 (https://a
# Embedded file name: <debby>
import requests, json, os, sys, hashlib
n = []

class warna:
    purple = '\x1b[95m'
    blue = '\x1b[94m'
    green = '\x1b[92m'
    yellow = '\x1b[93m'
    red = '\x1b[91m'


def get_userid(token):
    url = 'https://graph.facebook.com/me?access_token=%s' % token
    res = requests.get(url)
    info = json.loads(res.text)
    nick = info['name']
    n.append(info['name'])
    return info['id']


def turn_shield(token, enable=True):
    uid = get_userid(token)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(uid))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % token}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    if '"is_shielded":true' in res.text:
        print '\x1b[92mProfil Guard Is Active '
    else:
        if '"is_shielded":false' in res.text:
            print '\x1b[91mProfil Guard Is Non-Active '
        else:
            print 'Error'
print '\x1b[94m  ____                     _'
print '\x1b[94m / ___|_   _  __ _ _ __ __| |'
print '\x1b[94m| |  _| | | |/ _` | '__/ _` |'
print '\x1b[94m| |_| | |_| | (_| | | | (_| |'
print '\x1b[94m \____|\__,_|\__,_|_|  \__,_|' print '\x1b[92mV.1.1'

print '\x1b[94m[=============================================]'
print '\x1b[95m[ Tool     : Active/Non-Active Guard Facebook ]'
print '\x1b[92m[ Author   : Soesanto                         ]'
print '\x1b[93m[ WhatsAp  : 081617772813                     ]'
print '\x1b[92m[ Team     : SAN-Brother                      ]'
print '\x1b[91m[ Facebook : SAN Brother                      ]'
print '\x1b[94m[=============================================]'
print '\x1b[0mPlease Login To Facebook'
usr = raw_input('\x1b[93mUsername : \x1b[0m')
pwd = raw_input('\x1b[93mPassword : \x1b[0m')
API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': usr, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + usr + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.0' + API_SECRET
x = hashlib.new('md5')
x.update(sig)
data.update({'sig': x.hexdigest()})
req = requests.get('https://api.facebook.com/restserver.php', params=data)
gn = json.loads(req.text)
try:
    USER_TOKEN = '' + gn['access_token'] + ''
except KeyError:
    print '\x1b[91m[!] Login Failed'
    print '\x1b[91m[!] Check Email or Password Again'
    exit()
print '\x1b[94m  ____                     _'
print '\x1b[94m / ___|_   _  __ _ _ __ __| |'
print '\x1b[94m| |  _| | | |/ _` | '__/ _` |'
print '\x1b[94m| |_| | |_| | (_| | | | (_| |'
print '\x1b[94m \____|\__,_|\__,_|_|  \__,_|' print '\x1b[92mV.1.1'
print '\x1b[0mPilih jenis fungsi guard'
print '\x1b[93m[01] Activate'
print '\x1b[93m[02] Non-Active'
act = raw_input('\x1b[0mPilih salah satu nomor: ')
if act == '1' or act == '01':
    SHIELD_ENABLE = 'true'
    turn_shield(USER_TOKEN, SHIELD_ENABLE)
else:
    if act == '2' or act == '02':
        SHIELD_ENABLE = 'false'
        turn_shield(USER_TOKEN, SHIELD_ENABLE)
    else:
        os.system('xdg-open https://mobile.facebook.com')
                time.sleep(1)
