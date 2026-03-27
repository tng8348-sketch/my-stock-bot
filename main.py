import google.generativeai as genai
import requests
import os

# 깃허브 Secrets에서 키를 가져오도록 설정 (보안상 안전)
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = "7780808987"

# 제미나이 설정
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

def main():
    # 테스트용 프롬프트
    prompt = "주식 투자자 희준님에게 보낼 오늘의 첫 인사와 '테스트 성공' 메시지를 3줄로 작성해줘."
    
    try:
        response = model.generate_content(prompt)
        report = f"🚀 **시스템 테스트 가동**\n\n{response.text}"
        send_telegram(report)
        print("전송 완료!")
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    main()
