import json
import logging
import random
import sys
import time
import traceback
import uuid
from typing import List

import requests


logging.basicConfig(format='[%(filename)s] [%(asctime)s] [%(levelname)s] %(message)s', level=logging.INFO, stream=sys.stderr)
log = logging.getLogger(__name__)

HAS_ADDR: str = "https://audio-ai.ximalaya.com"


def get_token_headers(token: str = None):
    token = Token if Token else token
    return {"Authorization": token, "x-with-error-details": "1"}


def asr_async(audio_url: str = "", upload_id: str = None, addr: str = None, url: str = None, uid: str = None):
    addr = addr if addr else HAS_ADDR
    headers = get_token_headers()
    data = [
        {
            "uploadId": upload_id,
            "audioUrl": audio_url,
            "callbackUrl": "",
            "userData": json.dumps({"uid": uid}, ensure_ascii=False)
        }
    ]
    url = url if url else f"{addr}/has/asr/offline/api/v2/async"
    rsp = requests.post(url, json=data, headers=headers, timeout=30)
    assert rsp.status_code == 200, f"url:{url}, r:{rsp.content}"
    r = rsp.json()

    assert r[0].get("ok"), f"uid:{uid}, {addr}, data:{data}, url:{url}, r:{r}"
    log.debug(f"uid:{uid}, r:{r}")

    return r


def test_asr_async(
    loops: int = 100,
    uid: str = "",
    audio_url: str = None,
    url: str = None,
):
    time.sleep(random.random())
    log.info(f"uid:{uid}, audio_url:{audio_url}")
    err_cnt = 0
    suc_cnt = 0
    cost_list: List = list()
    for i in range(loops):
        i_uid = f"{uid}-{i}"
        t_start = time.time()
        try:
            r = None
            r = asr_async(audio_url=audio_url, url=url, uid=uid)
            ok = True
            suc_cnt += 1
            t_cost = time.time() - t_start
            cost_list.append(t_cost)
        except Exception as e:
            ok = False
            t_cost = time.time() - t_start
            err_cnt += 1
            t_sleep = random.random() * 5
            time.sleep(t_sleep)
        finally:
            log.info(
                f"uid:{i_uid}, ok:{ok}, {i:03}/{loops}! suc:{suc_cnt}, err:{err_cnt}, cost:{t_cost:.2f}s, "
                f"wait:{t_sleep:.2f}s, e:{traceback.format_exc(limit=1)}"
            )


def get_uuid():
    return uuid.uuid4().hex


def query_asr_result(task_id: int, addr: str = None):
    addr = addr if addr else HAS_ADDR
    headers = get_token_headers()
    while True:
        rsp = requests.get(f"{addr}/has/asr/offline/api/v2/async/{task_id}", headers=headers)
        rsp = rsp.json()
        if rsp["status"] != "DONE":
            sleep_sec = 2
            time.sleep(sleep_sec)
            log.info(f"waiting for {task_id}, status:{rsp['status']}")
            continue
        return rsp["phrases"]


def main():
    # audio_url: str = "http://aod.cos.tx.xmcdn.com/storages/f6d0-audiofreehighqps/0D/19/GMCoOScG2lIAAAowKAGWTzy6.m4a" # noqa: 90s
    audio_url: str = "http://localhost:8000/%E6%82%AC%E7%96%91_%E5%96%9C%E5%8D%83%E8%BE%89.mp3" # noqa: 90s
    uid = get_uuid()[-8:]
    loops = 1
    asr_final_result = ''
    for i in range(loops):
        t_start = time.time()
        ret = asr_async(audio_url=audio_url, uid=f"{uid}-{i}")  # send request
        asr_result = query_asr_result(ret[0]["taskId"])  # get result
        log.info(f"uid:{uid}, {i}/{loops}, takes:{time.time() - t_start:.2f}s, ret:{ret}， asr_result:{asr_result}")
        for response in asr_result:
            asr_final_result += response['text']
    
    print('=' * 80)
    print(asr_final_result)


if __name__ == '__main__':
    main()
