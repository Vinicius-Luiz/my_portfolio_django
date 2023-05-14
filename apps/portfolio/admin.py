from django.contrib import admin
from apps.portfolio.models import About, Link, Project, Skill, AboutLink, ProjectLink, SkillLink


class AboutAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id","name")

class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type")
    list_display_links = ("id","name")
    search_fields = ("name",)
    list_filter = ("type",)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "type", "published")
    list_display_links = ("id","title")
    search_fields = ("title",)
    list_filter = ("type",)
    list_editable = ("published",)

class SkillAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "type", "published")
    list_display_links = ("id","title")
    search_fields = ("title",)
    list_filter = ("type",)
    list_editable = ("published",)

class AboutLinkAdmin(admin.ModelAdmin):
    list_display = ("about", "link")
    list_display_links = ("about",)
    search_fields = ("about",)
    
class ProjectLinkAdmin(admin.ModelAdmin):
    list_display = ("project", "link")
    list_display_links = ("project",)
    search_fields = ("project",)

class SkillLinkAdmin(admin.ModelAdmin):
    list_display = ("skill", "link")
    list_display_links = ("skill",)
    search_fields = ("skill",)

admin.site.register(About, AboutAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(AboutLink, AboutLinkAdmin)
admin.site.register(ProjectLink, ProjectLinkAdmin)
admin.site.register(SkillLink, SkillLinkAdmin)