import json

import aiohttp

from gtp_api.settings import Settings


async def get_answer(content, instruction):
    content = {
        "model": 'general',
        "instruction_text": instruction,
        "request_text": content,
        "generation_options": {
            "max_tokens": 2500,
            "temperature": Settings.TemperatureYndx
        }
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Api-Key {Settings.ApiKeyYndx}',
        'x-folder-id': Settings.FolderIDYndx,
    }

    print(Settings.ApiKeyYndx, Settings.FolderIDYndx)

    async with aiohttp.ClientSession() as session:
        async with session.post(Settings.ApiAddrYndx, headers=headers, data=json.dumps(content)) as response:
            answer = await response.json()

    return answer['result']['alternatives'][0]['text']
