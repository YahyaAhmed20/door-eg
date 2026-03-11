from django.contrib import admin
from .models import AboutHeader,AboutSection,FeatureSection, Feature,TeamSection, TeamMember

admin.site.register(AboutHeader)


admin.site.register(AboutSection)

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1


class FeatureSectionAdmin(admin.ModelAdmin):
    inlines = [FeatureInline]


admin.site.register(FeatureSection, FeatureSectionAdmin)




class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 1


class TeamSectionAdmin(admin.ModelAdmin):
    inlines = [TeamMemberInline]


admin.site.register(TeamSection, TeamSectionAdmin)