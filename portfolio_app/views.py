from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render(request, "portfolio_app/home.html")

def about(request):
    return render(request, "portfolio_app/about.html")

def projects(request):
    projects_show=[
        {
            "title": "Project 1",
            "description": "Description of project 1",
            "image": "images/project1.png",
            "link": "https://github.com/VickyMahajanGitHub/VirtualAssistant_Vicky_Project1",
        },
         {
            "title": "Project 2",
            "description": "Description of project 2",
            "image": "images/project1.png",
            "link": "https://github.com/VickyMahajanGitHub/VirtualAssistant_Vicky_Project1",
        },
         {
            "title": "Project 1",
            "description": "Description of project 1",
            "image": "project1.jpg",
            "link": "#",
        },
         {
            "title": "Project 1",
            "description": "Description of project 1",
            "image": "project1.jpg",
            "link": "#",
        },
         {
            "title": "Project 1",
            "description": "Description of project 1",
            "image": "project1.jpg",
            "link": "#",
        },
         {
            "title": "Project 1",
            "description": "Description of project 1",
            "image": "project1.jpg",
            "link": "#",
        },
         {
            "title": "Project 1",
            "description": "Description of project 1",
            "image": "project1.jpg",
            "link": "#",
        },

    ]


    return render(request, "portfolio_app/projects.html",{"projects": projects_show})

def experience(request):
    experience=[
        {
            "company": "ABC Company",
            "position": "Position 1",
            "description": "Description of experience 1",
            # "image": "images/project1.png",
            # "link": "#",
        },
         {
            "company": "C 2",
            "position": "Position 2",
            "description": "Description of experience 2",
            # "image": "images/project1.png",
            # "link": "#",
        },
         {
            "company": "C 3",
            "position": "Position 3",
            "description": "Description of experience 3",
            # "image": "images/project1.png",
            # "link": "#",
        },
    ]
    return render(request, "portfolio_app/experience.html",{"experience": experience})
    return render(request, "portfolio_app/experience.html")

def certificates(request):

    certificates=[
        {

            "name": "Python Developer Certification",
            "issued_by": "Google",
            "validation": "Valid until 2026",
            "description": "Certification demonstrating proficiency in Python programming language.",
        },
         {
            "name": "Certificate 2",
            "issued_by": "Google",
            "validation": "Valid until 2026",
            "description": "Certification demonstrating proficiency in Python programming language.",
            # "image": "images/project1.png",
            # "link": "#",
        },
          {
            "name": "Certificate 3",
            "issued_by": "Google",
            "validation": "Valid until 2026",
            "description": "Certification demonstrating proficiency in Python programming language.",
            # "image": "images/project1.png",
            # "link": "#",
        },
        
    ]

    return render(request, "portfolio_app/certificates.html", {"certificates": certificates})

def contact(request):
    return render(request, "portfolio_app/contact.html")

def resume(request):
    resume_path="myapp/Vicky_Resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, 'rb') as resume_file:
            response=HttpResponse(resume_file.read(), content_type='application/pdf')

            if request.GET.get('download') == 'true':
                response['Content-Disposition'] = 'attachment; filename="Vicky_Resume.pdf"'
            else:
                response['Content-Disposition'] =  'inline; filename="Vicky_Resume.pdf"'
            return response
    else:
        return HttpResponse("Resume not found", status=404)