import subprocess

hostname = "www.naver.com" # 테스트할 호스트명

ping_result = subprocess.run(["ping.exe", "-n", "4", hostname], stdout=subprocess.PIPE)

print(ping_result.stdout.decode('cp949')) # 윈도우에서는 cp949 인코딩을 사용합니다.
