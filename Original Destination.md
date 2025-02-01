<!-- In your templates/travel/home.html -->

{% extends 'base.html' %}
{% load static %}
{% block content %}

<div class="destinations-showcase">
    <div class="destination-grid">
        <div class="destination-card">
            <img src="{% static 'img/Swizz.jpg' %}" alt="Bern, Switzerland" class="destination-image">
            <h3>Switzerland</h3>
        </div>
        <div class="destination-card">
            <img src="{% static 'img/brazil.jpg' %}" alt="Brasília, Brazil" class="destination-image">
            <h3>Brazil</h3>
        </div>
        <div class="destination-card">
            <img src="{% static 'img/China.jpg' %}" alt="Hong Kong, China" class="destination-image">
            <h3>China</h3>
        </div>
        <div class="destination-card">
            <img src="{% static 'img/Australia.jpg' %}" alt="Sydney, Australia" class="destination-image">
            <h3>Australia</h3>
        </div>
        <div class="destination-card">
            <img src="{% static 'img/USA.jpg' %}" alt="New York, USA" class="destination-image">
            <h3>USA</h3>
        </div>
    </div>
</div>
{% endblock %}
