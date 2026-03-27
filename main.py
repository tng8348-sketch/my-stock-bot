import google.generativeai as genai
import requests
import os

# 깃허브 Secrets에서 안전하게 키를 가져옵니다
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = "7780808987"

genai.configure(api_key=GEMINI_KEY)
# 모델명을 무료 버전에서 가장 잘 돌아가는 flash로 변경했습니다
model = genai.GenerativeModel('gemini-1.5-flash')

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

def main():
    try:
        # 테스트 메시지 생성
        prompt = "주식 투자자 희준님에게 보낼 오늘의 첫 인사와 시스템 가동 성공 메시지를 작성해줘."
        response = model.generate_content(prompt)
        
        report = f"🚀 **시스템 가동 성공**\n\n{response.text}"
        send_telegram(report)
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    main()
