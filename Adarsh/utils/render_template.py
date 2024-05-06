from Adarsh.vars import Var
from Adarsh.bot import StreamBot
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.file_properties import get_file_ids
from Adarsh.server.exceptions import InvalidHash
import urllib.parse
import aiofiles
import logging
import aiohttp

async def render_page(id, secure_hash):
    file_data=await get_file_ids(StreamBot, int(Var.BIN_CHANNEL), int(id))
    if file_data.unique_id[:6] != secure_hash:
        logging.debug(f'link hash: {secure_hash} - {file_data.unique_id[:6]}')
        logging.debug(f"Invalid hash for message with - ID {id}")
        raise InvalidHash
    src = urllib.parse.urljoin(Var.URL, f'{secure_hash}{str(id)}')
    if str(file_data.mime_type.split('/')[0].strip()) == 'video':
        async with aiofiles.open('Adarsh/template/req.html') as r:
            heading = 'Watch {}'.format(file_data.file_name)
            tag = file_data.mime_type.split('/')[0].strip()
            html = (await r.read()).replace('tag', tag) % (heading, file_data.file_name, src)
    elif str(file_data.mime_type.split('/')[0].strip()) == 'audio':
        async with aiofiles.open('Adarsh/template/req.html') as r:
            heading = 'Listen {}'.format(file_data.file_name)
            tag = file_data.mime_type.split('/')[0].strip()
            html = (await r.read()).replace('tag', tag) % (heading, file_data.file_name, src)
    else:
        async with aiofiles.open('Adarsh/template/dl.html') as r:
            async with aiohttp.ClientSession() as s:
                async with s.get(src) as u:
                    heading = 'Download {}'.format(file_data.file_name)
                    file_size = humanbytes(int(u.headers.get('Content-Length')))
                    html = (await r.read()) % (heading, file_data.file_name, src, file_size)
    return html

async def media_watch(id):
    file_data=await get_file_ids(StreamBot, int(Var.BIN_CHANNEL), int(id))
    file_name, mime_type = file_data.file_name, file_data.mime_type
    secure_hash = file_data.unique_id[:6]
    src = urllib.parse.urljoin(Var.URL, f'{secure_hash}{str(id)}')
    tag = file_data.mime_type.split('/')[0].strip()
    if tag == 'video':
        async with aiofiles.open('Adarsh/template/req.html') as r:
            heading = 'Watch - {}'.format(file_name)
            tag = file_data.mime_type.split('/')[0].strip()
            html = (await r.read()).replace('tag', tag) % (heading, file_name, src)
    else:
        html = '<h1>This is not streamable file</h1>'
    return html



async def batch_page(message_id_x, message_id_y):
    links_with_names = []
    for i in range(message_id_x, message_id_y + 1):
        file_data=await get_file_ids(StreamBot, int(Var.BIN_CHANNEL), int(id))
        secure_hash = file_data.unique_id[:6]
        link = urllib.parse.urljoin(Var.URL, f'{secure_hash}{str(id)}')
        file_name = file_data.file_name
        links_with_names.append((file_name, link, secure_hash))

    async with aiofiles.open('Adarsh/template/batch.html') as r:
        template = await r.read()

    buttons_html = ''
    for file_name, link, secure_hash in links_with_names:
        buttons_html += f'<form action="{link}" method="get"><button style="height:200px; width:200px; font-size: 20px; background-color: skyblue; border-radius: 15px;" class="button" type="submit">{file_name}</button></form>\n<br><p>&nbsp</p>'
    html_code = template.replace('{links_placeholder}', buttons_html)
    
    return html_code


    
    
    
    
