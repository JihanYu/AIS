from pathlib import Path

base_dir = Path(__file__).resolve().parent
file_path = base_dir.parent/ "build" / "keys.txt"

lines=[]
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        lines.append(line.rstrip('\n'))


# 실제투자용 HTTP와 소켓 URL
real_host_url = "https://api.kiwoom.com"
real_socket_url = "wss://api.kiwoom.com:10000"

# 모의투자용 HTTP와 소켓 URL
paper_host_url = "https://mockapi.kiwoom.com"
paper_socket_url = "wss://mockapi.kiwoom.com:10000"

# 실제투자용 앱 키와 시크릿
real_app_key = lines[0] 
real_app_secret = lines[1]

# 모의투자용 앱 키와 시크릿
paper_app_key = lines[2]
paper_app_secret = lines[3]

# 텔레그램용 챗 아이디와 토큰
telegram_chat_id = ""
telegram_token = ""

