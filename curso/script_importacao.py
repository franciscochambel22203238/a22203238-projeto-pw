import json
from .models import Course, ScientificArea, Discipline, ProgrammingLanguage, Project

ScientificArea.objects.all().delete()
Discipline.objects.all().delete()
Project.objects.all().delete()

with open('curso/json/lig.json') as file:
    data = json.load(file)

     # Criar instância de ScientificArea
    scientific_area_name = data.get('courseDetail', {}).get('scientificArea', '')
    scientific_area, created = ScientificArea.objects.get_or_create(name=scientific_area_name)

    # Criar instância de Course
    course_data = data.get('courseDetail', {})
    course = Course.objects.create(
        name=course_data.get('courseName'),
        presentation=course_data.get('presentation'),
        objectives=course_data.get('objectives'),
        competences=course_data.get('competences')
    )
    course.scientific_areas.add(scientific_area)


    # Criar instâncias de Discipline
    for discipline_data in data.get('courseFlatPlan', []):
        discipline = Discipline.objects.create(
            name=discipline_data.get('curricularUnitName'),
            year=discipline_data.get('curricularYear'),
            semester=discipline_data.get('semester'),
            ects=discipline_data.get('ects'),
            curricularIUnitReadableCode=discipline_data.get('curricularIUnitReadableCode'),
            scientific_area=scientific_area
        )

    # Criar instâncias de Project para as Disciplinas
    for project_data in data.get('projects', []):
        discipline = Discipline.objects.get(curricularIUnitReadableCode=project_data.get('curricularIUnitReadableCode'))
        project = Project.objects.create(
            description=project_data.get('description'),
            concepts_applied=project_data.get('concepts_applied'),
            technologies_used=project_data.get('technologies_used'),
            youtube_link=project_data.get('youtube_link'),
            github_link=project_data.get('github_link'),
            discipline=discipline
        )

        # Associar linguagens de programação ao projeto
        for language_name in project_data.get('programming_languages', []):
            language, created = ProgrammingLanguage.objects.get_or_create(name=language_name)
            project.programming_languages.add(language)

    # Criar instâncias de Teacher e associar às Disciplinas
    for teacher_data in data.get('teachers', []):
        teacher = Teacher.objects.create(name=teacher_data.get('name'))
        for discipline_code in teacher_data.get('disciplines', []):
            discipline = Discipline.objects.get(curricularIUnitReadableCode=discipline_code)
            TeacherDiscipline.objects.create(teacher=teacher, discipline=discipline)