from django.urls import path

from core.views import home, about, contact, ContactView, export

app_name = 'core'
urlpatterns = [
    path('', home, name='home_page'),
    path('about/', about, name='about_page'),
    # path('contact/', contact, name='contact'),
    path('contact', ContactView.as_view(), name='contact'),

    # path('404', 404, name='404')

    path('export/', export, name='export')
]