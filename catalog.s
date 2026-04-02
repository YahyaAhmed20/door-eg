{% extends 'base.html' %}
{% load static %}

<!-- ✅ 1. SEO Meta Tags for Catalog Page -->
{% block title %}Our Catalog | Steel Doors, Pergolas & Ladders Products - Icondoor{% endblock %}
{% block meta_description %}Browse Icondoor's product catalog featuring high-quality steel doors, modern pergolas, and durable metal ladders. Download specifications and view our latest designs in Giza.{% endblock %}
{% block meta_keywords %}steel door catalog, metal pergola designs, ladder specifications, Icondoor products, laser cut door patterns, Giza metal fabrication{% endblock %}

{% block body %}

<div class="container-xxl py-5">
    <div class="container">

        <!-- Header Section -->
        <div class="text-center mx-auto mb-5 catalog-header" style="max-width:600px;">
            <h4 class="section-title">Our Catalog</h4>
            
            <!-- ✅ H1 Tag for SEO: Main Keyword Focus -->
            <h1 class="display-5 mb-3 catalog-main-title">
                Explore Our Product Catalogs
            </h1>
            
            <p class="text-muted catalog-subtitle">
                Browse our latest collections of steel doors, pergolas, and shading solutions. 
                View detailed specifications and designs.
            </p>
        </div>

        <div class="row g-4">

        {% for catalog in catalogs %}
        <div class="col-lg-4 col-md-6 wow fadeInUp" data-wow-delay="{{ forloop.counter|divisibleby:2|yesno:'0.1s,0.3s' }}">

            <!-- ✅ Semantic Article Tag for Each Catalog Item -->
            <article class="card catalog-card border-0 shadow-sm h-100">

                <div class="catalog-img">
                    <!-- ✅ Optimized Image with Alt Text & Lazy Loading -->
                    <img src="{{ catalog.image.url }}" 
                         class="card-img-top" 
                         alt="{{ catalog.title }} Catalog Cover" 
                         loading="lazy">

                    <div class="catalog-overlay">
                        <!-- ✅ Button with Accessibility & Security Attributes -->
                        <a href="{{ catalog.get_catalog_url }}" 
                           target="_blank" 
                           rel="noopener noreferrer"
                           class="btn btn-light preview-overlay-btn"
                           aria-label="Preview {{ catalog.title }}">
                           <i class="fa fa-eye me-2"></i>Preview
                        </a>
                    </div>
                </div>

                <div class="card-body text-center d-flex flex-column justify-content-between">

                    <!-- ✅ H2 for Catalog Title (Sub-heading under H1) -->
                    <h2 class="h4 mb-3 catalog-title">
                        {{ catalog.title }}
                    </h2>

                    <div class="d-flex justify-content-center gap-2 mt-auto">
                        <a href="{{ catalog.get_catalog_url }}" 
                           target="_blank" 
                           rel="noopener noreferrer"
                           class="btn btn-primary catalog-btn"
                           aria-label="View {{ catalog.title }} Details">
                           <i class="fa fa-eye me-2"></i>Preview Catalog
                        </a>
                    </div>

                </div>

            </article>

        </div>

        {% empty %}

        <div class="col-12 text-center py-5">
            <div class="alert alert-light border shadow-sm p-5">
                <i class="fa fa-folder-open fa-3x text-muted mb-3"></i>
                <h4 class="text-muted">No catalogs available yet</h4>
                <p class="mb-0">Please check back later for our latest steel door and pergola designs.</p>
                <a href="{% url 'home:home' %}" class="btn btn-outline-primary mt-3">Back to Home</a>
            </div>
        </div>

        {% endfor %}

        </div>

    </div>
</div>

<style>
    .preview-overlay-btn{
        font-weight:700;
        padding:10px 22px;
        border-radius:6px;
        transform:translateY(10px);
        transition:all .3s;
    }

    .catalog-card:hover .preview-overlay-btn{
        transform:translateY(0);
    }

    .catalog-main-title{
        font-weight:800;
    }

    .catalog-subtitle{
        font-weight:500;
        line-height: 1.6;
    }

    .catalog-title{
        font-weight:700;
        color: #333;
    }

    .catalog-btn{
        font-weight:600;
        padding: 8px 20px;
    }

    .catalog-card{
        transition: all .35s ease;
        border-radius:12px;
        overflow:hidden;
        cursor:pointer;
        background: #fff;
    }

    .catalog-card:hover{
        transform: translateY(-8px);
        box-shadow:0 15px 40px rgba(0,0,0,0.15);
    }

    .catalog-img img{
        height:260px;
        width:100%;
        object-fit:cover;
        transition:transform .4s;
    }

    .catalog-card:hover img{
        transform:scale(1.08);
    }

    .catalog-img{
        position:relative;
        overflow:hidden;
    }

    .catalog-overlay{
        position:absolute;
        top:0;
        left:0;
        width:100%;
        height:100%;
        display:flex;
        align-items:center;
        justify-content:center;
        background:rgba(0,0,0,0.45);
        opacity:0;
        transition:all .35s ease;
    }

    .catalog-card:hover .catalog-overlay{
        opacity:1;
    }
</style>

{% endblock body %}