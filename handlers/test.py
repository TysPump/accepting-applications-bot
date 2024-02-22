from yandex_music import Client
from aiogram import F, Bot
import requests
from xml.dom import minidom
from hashlib import md5


SIGN_SALT = 'XGRlBW9FXlekgbPrRHuSiA'

def get_text_node_data(nodes):
    return ''.join(node.data for node in nodes[0].childNodes if node.nodeType == node.TEXT_NODE)

def build_direct_link_from_url(url: str) -> str:
    
    response = requests.get(url)
    xml = response.text

    doc = minidom.parseString(xml)
    host = get_text_node_data(doc.getElementsByTagName('host'))
    path = get_text_node_data(doc.getElementsByTagName('path'))
    ts = get_text_node_data(doc.getElementsByTagName('ts'))
    s = get_text_node_data(doc.getElementsByTagName('s'))
    sign = md5((SIGN_SALT + path[1::] + s).encode('UTF-8')).hexdigest()

    return f'https://{host}/get-mp3/{sign}/{ts}{path}'


def get_url(text):
    client = Client('y0_AgAAAABgALPvAAG8XgAAAADfxaZ7VWgLPe3pRH6HX8YX9drw1kctPJw').init()

    try:
        search_result = client.search(text)

        if search_result.best:
            best = search_result.best.result
            track_info = best.get_download_info()

            return track_info[0]['download_info_url']
        
        else:
            return False
        
    except Exception as e:
        print("Error In {} func: {}".format('get_xml_url', e))

        return False



async def get_xml_url(query, bot: Bot):
    result = get_url(query.text)

    if result is False:
        await bot.send_message(query.from_user.id, "Трек не найден.")
        return 1
    
    else:
        current_url = build_direct_link_from_url(result)
    
    await bot.send_audio(query.from_user.id, current_url)
        

    

