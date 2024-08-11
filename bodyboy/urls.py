from django.urls import path
from bodyboy import views
urlpatterns=[
    
    path('',views.index),
    path('about/',views.about),
    path('service/',views.service),
    path('ai/',views.ai),
    path('info/',views.info),
    path('login/',views.login),
    path('register/',views.register),
    path('ai-predict/', views.gemini_api_view, name='ai_predict'),
    # path('ai/predict/', views.ai_predict, name='ai_predict'),
    # path('contact/', views.contact_view, name='contact'),
    # # path('contact_success/', TemplateView.as_view(template_name="contact_success.html"), name='contact_success')

]