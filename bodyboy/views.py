from asyncio.log import logger
import json
from django.shortcuts import render,redirect
import requests
from django.http import JsonResponse
from django.conf import settings
import logging
# Create your views here.

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from sqlalchemy import JSON
from .forms import CustomUserCreationForm
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')


# api_key = os.getenv('api_key')
genai.configure(api_key=GEMINI_API_KEY)
model=genai.GenerativeModel(model_name="gemini-pro")


def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def service(request):
    return render(request, 'service.html')
def ai(request):
    return render(request, 'ai.html')
def info(request):
    return render(request, 'info.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



# @csrf_exempt # type: ignore
def gemini_api_view(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON request to get the text input
            data = json.loads(request.body)
            # logger.debug('This is a debug message')
            input_text = data.get('query')
            # print(input_text)
            # print(input_text)
            if input_text=="":
                return JsonResponse({'error': 'No text input provided'}, status=400)
            input_text = "Give gym related responses for the following query, if it's not related gym then return \"out of context\"" + input_text
            # Define the Gemini API endpoint (replace with your actual endpoint)
            # url = "https://api.gemini.com/v1/ai-endpoint"  # Replace with your specific endpoint
            
            # Your API key (should be stored securely)
            # api_key = settings.GEMINI_API_KEY
            
            # headers = {
            #     'Content-Type': 'application/json',
            #     'Authorization': f'Bearer {GEMINI_API_KEY}',  # Example if Gemini requires Bearer token
            #     # Other headers if necessary
            # }
            
            # Prepare the payload to be sent to the Gemini API
            # payload = {
            #     'input_text': input_text  # Adjust this according to the API's expected input format
            # }
            
            # Make the POST request to the Gemini API with headers and payload
            # response = requests.post(url, headers=headers, json=payload)
            # response.raise_for_status()  # Raise an error for bad status codes
            
            # # Parse the JSON response
            # result_data = response.json()

            response = model.generate_content(input_text)
            print(response.text)
            # Return the Gemini API's response as a JSON response
            return JsonResponse({'response': response.text})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON provided'}, status=400)
        
        except requests.exceptions.RequestException as e:
            # Handle any errors that occur during the request
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
