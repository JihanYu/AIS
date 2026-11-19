import json

import requests

from config.config import (
    real_host_url,
    real_app_key,
    real_app_secret,
    paper_host_url,
    paper_app_key,
    paper_app_secret,
)


def fn_au10001(host, app_key, app_secret):
    """접근토큰 발급 (examples/get-token.py 참조)"""
    url = host + "/oauth2/token"
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    data = {
        "grant_type": "client_credentials",
        "appkey": app_key,
        "secretkey": app_secret,
    }

    response = requests.post(url, headers=headers, json=data, timeout=10)

    print("Code:", response.status_code)
    print(
        "Header:",
        json.dumps(
            {k: response.headers.get(k) for k in ["next-key", "cont-yn", "api-id"]},
            indent=4,
            ensure_ascii=False,
        ),
    )
    body = response.json()
    print("Body:", json.dumps(body, indent=4, ensure_ascii=False))
    return body.get("token")


if __name__ == "__main__":
    print("===== 실제투자 토큰 발급 =====")
    real_token = fn_au10001(real_host_url, real_app_key, real_app_secret)
    print("실제투자 토큰:", real_token)

    print("\n===== 모의투자 토큰 발급 =====")
    paper_token = fn_au10001(paper_host_url, paper_app_key, paper_app_secret)
    print("모의투자 토큰:", paper_token)
