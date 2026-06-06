import google.generativeai as genai

genai.configure(api_key="AIzaSyBhuxaikj74kHIV9fFCx9mZp5b7N8gZV38")

models = genai.list_models()

for m in models:
    print(m.name)