from langchain_google_genai import GoogleGenerativeAI


def invoke_gemini(prompt: str, api_key: str):
  llm = GoogleGenerativeAI(model='gemini-pro', google_api_key=api_key)
  return llm.invoke(prompt)

