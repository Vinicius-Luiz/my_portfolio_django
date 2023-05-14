from django.db import models

class About(models.Model):
    name          = models.CharField(max_length = 128, null = False, blank = False)
    about_me_text = models.TextField(null = False, blank = False)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Link(models.Model):
    LINK_TYPE = [
        ('LINKEDIN', 'LinkedIn'),
        ('GITHUB', 'GitHub'),
        ('KAGGLE', 'Kaggle'),
        ('CERTIFICATE', 'Certificado'),
        ('OTHER', 'Outros'),
    ]
    name = models.CharField(max_length = 128, null = False, blank = False)
    type = models.CharField(max_length=128, choices = LINK_TYPE)
    url  = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.type})'

class Project(models.Model):
    PROJECT_TYPE = [
        ('PY', 'Python'),
        ('ML', 'Machine Learning'),
        ('DA', 'Data Analytics'),
    ]

    title        = models.CharField(max_length = 256, null = False, blank = False)
    description  = models.TextField(null = False, blank = False)
    image        = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    type         = models.CharField(max_length=128, choices=PROJECT_TYPE)
    published    = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.type})'

class Skill(models.Model):
    SKILL_TYPE = [
        ('LP', 'Linguagens de Programação'),
        ('F', 'Ferramentas'),
        ('BF', 'Bibliotecas e Frameworks'),
    ]

    title = models.CharField(max_length = 256, null = False, blank = False)
    image = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    type  = models.CharField(max_length=128, choices=SKILL_TYPE)
    published    = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.type})'


class ProjectLink(models.Model):
    project    = models.ForeignKey(Project, on_delete=models.CASCADE, related_name = 'project')
    link       = models.ForeignKey(Link, on_delete=models.CASCADE, related_name = 'project_links')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.project.title} ({self.link.type})'

class SkillLink(models.Model):
    skill      = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name = 'skill')
    link       = models.ForeignKey(Link, on_delete=models.CASCADE, related_name = 'skill_links')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.skill.title} ({self.link.type})'