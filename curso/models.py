from django.db import models

class ScientificArea(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    semester = models.CharField(max_length=20)
    ects = models.IntegerField()
    curricularIUnitReadableCode = models.CharField(max_length=20)
    scientific_area = models.ForeignKey(ScientificArea, on_delete=models.CASCADE, related_name='disciplines')
    projects = models.ManyToManyField('Project', related_name='disciplines', blank=True)
    teachers = models.ManyToManyField('Teacher', related_name='disciplines')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    presentation = models.TextField()
    objectives = models.TextField()
    competences = models.TextField()
    scientific_areas = models.ManyToManyField(ScientificArea, related_name='courses')
    disciplines = models.ManyToManyField(Discipline, related_name='courses')

    def __str__(self):
        return self.name

class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255, default = "Projeto")
    description = models.TextField()
    concepts_applied = models.TextField()
    technologies_used = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    youtube_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    programming_languages = models.ManyToManyField(ProgrammingLanguage, related_name='projects')

    def __str__(self):
        return self.name

