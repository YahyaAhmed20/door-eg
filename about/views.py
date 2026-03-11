from django.shortcuts import render
from .models import AboutHeader,AboutSection,FeatureSection,TeamSection

def about(request):
    header = AboutHeader.objects.first()
    about = AboutSection.objects.first()

    feature_section = FeatureSection.objects.first()
    team_section = TeamSection.objects.first()


    return render(request, 'about/about.html', {
        'header': header,
        'about': about,
        'feature_section': feature_section,
        'team_section': team_section


    })