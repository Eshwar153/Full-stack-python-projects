from django.shortcuts import render
from django.http import JsonResponse
import openai

# Set your OpenAI API key
openai.api_key = "your-api-key"

def chatbot_response(request):
    if request.method == "POST":
        user_input = request.POST.get("message")
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        
        chatbot_reply = response["choices"][0]["message"]["content"]
        return JsonResponse({"response": chatbot_reply})

    return render(request, "chatbot/chat.html")

# Create your views here.
