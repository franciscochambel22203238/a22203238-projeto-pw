from django import forms    # formulários Django
from .models import Course, Discipline, Project, ScientificArea, Teacher, ProgrammingLanguage

class CourseForm(forms.ModelForm):
  class Meta:
    model = Course        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Course.

class DisciplineForm(forms.ModelForm):
  class Meta:
    model = Discipline        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Discipline.

class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Project.

class ScientificAreaForm(forms.ModelForm):
  class Meta:
    model = ScientificArea        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe ScientificArea.

class TeacherForm(forms.ModelForm):
  class Meta:
    model = Teacher        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Teacher.

class ProgrammingLanguageForm(forms.ModelForm):
  class Meta:
    model = ProgrammingLanguage        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe ProgrammingLanguage.
