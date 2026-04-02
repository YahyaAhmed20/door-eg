{% extends 'base.html' %}
{% load static %}
{% block body %}
<!-- Carousel Start -->
<div class="container-fluid p-0 pb-5 wow fadeIn">
    <div class="owl-carousel header-carousel position-relative">

        {% for carousel in carousels %}
            {% for img in carousel.images.all %}

            <div class="owl-carousel-item position-relative"
                 data-dot="<img src='{{ img.image.url }}'>">

                {% comment %} <img class="img-fluid w-100"
                     src="{{ img.image.url }}"
                     style="height:700px; object-fit:cover;"
                     alt=""> {% endcomment %}
                 <img class="img-fluid w-100 carousel-img"
     src="{{ img.image.url }}"
     loading="lazy"
     alt="{{ carousel.title }}">

                <div class="owl-carousel-inner">
                    <div class="container">
                        <div class="row justify-content-start">
                            <div class="col-10 col-lg-8">

                                <h1 class="display-1 text-white animated slideInDown">
                                    {{ carousel.title }}
                                </h1>

                                <p class="fs-5 fw-medium text-white mb-4 pb-3">
                                    {{ carousel.description }}
                                </p>

                                <a href="{% url 'catalog:catalog' %}"
                                   class="btn btn-primary py-3 px-5 animated slideInLeft">
                                    {{ carousel.button_text }}
                                </a>

                            </div>
                        </div>
                    </div>
                </div>

            </div>

            {% endfor %}
        {% endfor %}

    </div>
</div>
<!-- Carousel End -->

  <!-- Facts Start -->
<!-- Facts Start -->
<div class="container-xxl py-5">
    <div class="container pt-5">
        <div class="row g-4">

            {% for fact in facts %}

            <div class="col-lg-4 col-md-6 wow fadeInUp">
                <div class="fact-item text-center bg-light h-100 p-5 pt-0">

                    <div class="fact-icon">
                        <img src="{{ fact.icon.url }}" alt="">
                    </div>

                    <h3 class="mb-3">
                        {{ fact.title }}
                    </h3>

                    <p class="mb-0">
                        {{ fact.description }}
                    </p>

                </div>
            </div>

            {% endfor %}

        </div>
    </div>
</div>
<!-- Facts End -->
<!-- Facts End -->


  <!-- Service Start -->
<!-- Service Start -->
<div class="container-xxl py-5">
    <div class="container">

        <div class="text-center mx-auto mb-5 wow fadeInUp" style="max-width: 600px;">
            <h4 class="section-title">Our Services</h4>
            <h1 class="display-5 mb-4">
                Metal Fabrication & Laser Cut Design Services
            </h1>
        </div>

        <div class="row g-4">

            {% for service in services %}

            <div class="col-lg-4 col-md-6 wow fadeInUp">

                <div class="service-item d-flex position-relative text-center h-100">

                    <img class="bg-img"
                         src="{{ service.image.url }}"
                         alt="">

                    <div class="service-text p-5">

                        <img class="mb-4"
                             src="{{ service.icon.url }}"
                             alt="Icon">

                        <h3 class="mb-3">
                            {{ service.title }}
                        </h3>

                        <p class="mb-4">
                            {{ service.description }}
                        </p>

                        {% comment %} <a class="btn" href="#">
                            <i class="fa fa-plus text-primary me-3"></i>Read More
                        </a> {% endcomment %}

                    </div>

                </div>

            </div>

            {% endfor %}

        </div>

    </div>
</div>
<!-- Service End -->
<!-- Project Start -->
<div class="container-xxl project py-5">
<div class="container">

<div class="text-center mx-auto mb-5 wow fadeInUp" style="max-width:600px;">
<h4 class="section-title">Our Projects</h4>
<h1 class="display-5 mb-4">Visit Our Latest Projects And Our Innovative Works</h1>
</div>

<div class="row g-4 wow fadeInUp">

<!-- Tabs -->
<div class="col-lg-4">
<div class="nav nav-pills d-flex justify-content-between w-100 h-100 me-4">

{% for project in projects %}

<button class="nav-link w-100 p-4 mb-4 {% if forloop.first %}active{% endif %}"
        data-bs-toggle="pill"
        data-bs-target="#tab-pane-{{ forloop.counter }}">

<h3 class="m-0">
{{ forloop.counter|stringformat:"02d" }}. {{ project.title }}
</h3>

</button>

{% endfor %}

</div>
</div>

<!-- Content -->
<div class="col-lg-8">
<div class="tab-content w-100">

{% for project in projects %}

<div class="tab-pane fade {% if forloop.first %}show active{% endif %}"
     id="tab-pane-{{ forloop.counter }}">

<div class="row g-4">

<div class="col-md-6" style="min-height:350px;">
<div class="position-relative h-100">

<img class="project-img"
     src="{{ project.image.url }}"
     alt="">

</div>
</div>

<div class="col-md-6">

<h1 class="mb-3">
{{ project.title }}
</h1>

<p class="mb-4">
{{ project.description }}
</p>

</div>

</div>

</div>

{% endfor %}

</div>
</div>

</div>
</div>
</div>
<!-- Project End -->
  

    
<!-- Testimonial Start -->
<div class="container-xxl py-5">
<div class="container">

<div class="text-center mx-auto mb-5 wow fadeInUp" style="max-width:600px;">
<h4 class="section-title">Testimonials</h4>
<h1 class="display-5 mb-4">
What Our Clients Say
</h1>
</div>

<div class="owl-carousel testimonial-carousel wow fadeInUp">

{% for testimonial in testimonials %}

<div class="testimonial-item text-center"
     data-dot="<img class='img-fluid' src='{{ testimonial.image.url }}' alt=''>">

<p class="fs-5">
{{ testimonial.message }}
</p>

<h3>
{{ testimonial.name }}
</h3>

<span class="text-primary">
{{ testimonial.profession }}
</span>

</div>

{% endfor %}

</div>

</div>
</div>
<style>
 .carousel-img{
width:100%;
height:500px;
object-fit:cover;
object-position:center;
}



/* Laptop */
@media (min-width:992px){
.carousel-img{
height:520px;
}
}

/* Mobile */
@media (max-width:768px){
.carousel-img{
height:360px;
}
}

{% comment %} Services {% endcomment %}
.service-item{
position: relative;
overflow: hidden;
}

.service-item .bg-img{
position: absolute;
width:100%;
height:100%;
object-fit:cover;
top:0;
left:0;
}

.service-text{
position: relative;
z-index:2;
transition:0.4s;
background: rgba(0,0,0,0.2);
color:#fff;
}

/* Hover Effect */
.service-item:hover .service-text{
background: rgba(0,0,0,0.4);
}


{% comment %} Project {% endcomment %}
.project-img{
width:100%;
height:300px;
object-fit:contain;
}

/* laptop */
@media (min-width:992px){
.project-img{
height:350px;
}
}

/* mobile */
@media (max-width:768px){
.project-img{
height:250px;
}
}


</style>
<!-- Testimonial End -->
{% endblock body %}