from django.db import models

class About(models.Model):
    name          = models.CharField(max_length = 128, null = False, blank = False)
    about_me_text = models.TextField(null = False, blank = False)
    image         = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
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
        ('INSTAGRAM', 'Instagram'),
        ('OTHER', 'Outros'),
    ]
    name = models.CharField(max_length = 128, null = False, blank = False)
    type = models.CharField(max_length=128, choices = LINK_TYPE)
    url  = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.type})'
    
    def link_type_icon(self):
        if self.type == 'LINKEDIN':
            return 'fa-brands fa-linkedin-in'
        
        elif self.type == 'GITHUB':
            return 'fa-brands fa-github'
        
        elif self.type == 'KAGGLE':
            return 'fa-solid fa-k'
        
        elif self.type == 'CERTIFICATE':
            return 'fa-sharp fa-solid fa-file-certificate'
        
        elif self.type == 'INSTAGRAM':
            return 'fa-brands fa-instagram'
        
        else:
            return 'fa-solid fa-link'

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
    developed_at = models.DateField(null = True, blank = True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.type})'
    
    def project_type_span(self):
        if self.type == 'PY':
            return 'badge text-bg-warning'
        elif self.type == 'ML':
            return 'badge text-bg-primary'
        elif self.type == 'DA':
            return 'badge text-bg-success'
        else:
            return 'badge text-bg-secondary'

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

class AboutLink(models.Model):
    about      = models.ForeignKey(About, on_delete=models.CASCADE, related_name = 'a_links')
    link       = models.ForeignKey(Link, on_delete=models.CASCADE, related_name = 'abouts_l')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.about.name} ({self.link.type})'
    
class ProjectLink(models.Model):
    project    = models.ForeignKey(Project, on_delete=models.CASCADE, related_name = 'p_links')
    link       = models.ForeignKey(Link, on_delete=models.CASCADE, related_name = 'projects_l')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.project.title} ({self.link.type})'

class SkillLink(models.Model):
    skill      = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name = 's_links')
    link       = models.ForeignKey(Link, on_delete=models.CASCADE, related_name = 'skills_l')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.skill.title} ({self.link.type})'
    