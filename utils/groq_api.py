# import requests
# import os

# def ask_groq(prompt: str):
#     try:
#         res = requests.post(
#             "https://api.groq.com/openai/v1/chat/completions",
#             headers={
#                 "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
#                 "Content-Type": "application/json"
#             },
#             json={
#                 "model": "gemma2-9b-it",  # Or any model you use
#                 "messages": [{"role": "user", "content": prompt}],
#                 "temperature": 0.7
#             },
#             timeout=5
#         )

#         data = res.json()

#         # 💥 Debug: print full response if something fails
#         if "choices" not in data:
#             print("❌ GROQ ERROR:", data)
#             return "GROQ API error: response malformed or failed."

#         return data["choices"][0]["message"]["content"]

#     except Exception as e:
#         print("❌ Exception in ask_groq():", e)
#         return "GROQ API request failed."


# utils/groq_api.py
import os
import requests

def ask_groq(prompt: str) -> str | None:
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-8b-8192",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            },
            timeout=30
        )

        if response.status_code == 429:
            print("❌ Rate limit hit (429)")
            return "Rate limit exceeded. Please try again later."

        data = response.json()

        if "choices" in data and data["choices"]:
            return data["choices"][0]["message"]["content"]

        print("❌ Invalid response structure:", data)
        return None

    except Exception as e:
        print("❌ Exception in ask_groq():", str(e))
        return None
