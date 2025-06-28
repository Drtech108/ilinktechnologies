from os import access
from django.shortcuts import redirect, render

from myapp import form
from myapp import form1
from myapp.form import ContactForm
from myapp.form1 import RegistrationForm

def home(request):
    services = [
        {"title": "CCTV Installation", "description": "Advanced surveillance for residential and commercial premises..."},
        {"title": "Electric Fence Solutions", "description": "High-security electric fencing for perimeter control..."},
        {"title": "Gate Automation", "description": "Seamless entry and exit with smart gate automation..."},
        {"title": "Network Cabling", "description": "Structured cabling solutions for reliable connectivity..."},
        {"title": "Access Control System","description": "Modern biometric and card-based access controll solutions for secure entries management in any facility"},
        {"title": "Satellite Dish Installation", "description": "Professional satellite dish setup for uninterrupted TV service..."},
    ]

    projects = [
        {"title": "Home Security Upgrade", "description": "CCTV upgrade for 50,00 sq ft for apartment", "image_url": "/static/imgs/c1.jpg"},
        {"title": "Residential Perimeter Defense", "description": "Electric fence & automation for high-value residence", "image_url": "/static/imgs/ef4.jpg"},
        {"title": "Corporate Network Infrastructure", "description": "CAT6 cabling & secure network setup", "image_url": "/static/imgs/n1.jpg"},
        {"title": "Smart Doorbell", "description": "Full smart home with door bell", "image_url": "/static/imgs/vb1.jpg"},
        {"title": "Retail Store Acccess Control", "description": "Biometric and RFID control systems implementated for chain of retail outlets", "image_url": "/static/imgs/b1.jpg"},
        {"title": "Gate Automation", "description": "installation of Heavy-duty silde gate with integrated safty feacture for commercial complex", "image_url": "/static/imgs/ag5.png" },
    ]

    testimonials = [
        {"quote": "The CCTV system is top-notch. Highly recommend!", "name": "Sarah M.", "role": "Operations Manager"},
        {"quote": "Their electric fence gave us peace of mind.", "name": "David L.", "role": "Homeowner"},
        {"quote": "Our new automated gate is secure and sleek.", "name": "Emily R.", "role": "Estate Manager"},
    ]

    return render(request, 'page/home.html', {
        'services': services,
        'projects': projects,
        'testimonials': testimonials
        })
    

def services(request):
    offerings = [
        {
            'title': 'High-Definition CCTV Installation',
            'category': 'CCTV',
            'description': 'Crystal-clear surveillance cameras for wide area monitoring.',
            'image': 'imgs/c2.jpg',
            'url': '#',
        },
        {
            'title': 'Electric Fence Installation',
            'category': 'Electric Fence',
            'description': 'High-security electric fencing for residential and commercial properties.',
            'image': 'imgs/ef1.jpg',
            'url': '#',
        },
        {
            'title': 'Gate Automation',
            'category': 'Automation',
            'description': 'Automated gate systems for secure and convenient access.',
            'image': 'imgs/ga1.jpg',
            'url': '#',
        },
        {
            'title': 'Network Cabling Solutions',
            'category': 'Networking',
            'description': 'Structured cabling solutions for reliable connectivity.',
            'image': 'imgs/n1.jpg',
            'url': '#',
        },
        {
            'title': 'Access Control Systems',
            'category': 'Security',
            'description': 'Modern biometric and card-based access control solutions.',
            'image': 'imgs/b1.jpg',
            'url': '#',
        },
        {
            'title': "Satellite Dish Installation",
            "category": "Installation",
            "description": "Professional satellite dish setup for uninterrupted TV service.",
            "image": "imgs/ds1.jpg",
            "url": "#",
        },
        {
            'title': 'Video Intercom System',
            'category': 'Communication',
            'description': 'High-quality video intercom systems for secure communication at entry points.',
            'image': 'imgs/it1.jpg',
            'url': '#',
        },
        # Add more offerings as needed
    ]

    return render(request, 'page/services.html', {'offerings': offerings})

        
def gallery(request):
    videos = [
        {
            'title': 'Construction Site Monitoring',
            'category': 'CCTV Installation',
            'description': 'Robust, weather-proof surveillance for construction zones.',
            'source': 'videos/cv1.mp4',
            'thumbnail': 'imgs/c2.jpg',
            'detail_url': '#'
        },
        {
            'title': 'Electric Fence Installation',
            'category': 'Security',
            'description': 'High-security electric fencing for residential and commercial properties.',
            'source': 'videos/ev1.mp4',
            'thumbnail': 'imgs/ef1.jpg',
            'detail_url': '#'
        },
        {
            'title': 'Gate Automation System',
            'category': 'Automation',
            'description': 'Automated gate systems for secure and convenient access.',
            'source': 'videos/gv2.mp4',
            'thumbnail': 'imgs/ga1.jpg',
            'detail_url': '#'
        },
        
        {
            'title': 'Network Cabling Solutions',
            'category': 'Networking',
            'description': 'Structured cabling solutions for reliable connectivity.',
            'source': 'videos/network_cabling.mp4',
            'thumbnail': 'imgs/n1.jpg',
            'detail_url': '#'
        },
        {
            'title': 'Access Control Systems',
            'category': 'Security',
            'description': 'Modern biometric and card-based access control solutions.',
            'source': 'videos/access_control.mp4',
            'thumbnail': 'imgs/b1.jpg',
            'detail_url': '#'
        },
        {
            'title': "Satellite Dish Installation",
            "category": "Installation",
            "description": "Professional satellite dish setup for uninterrupted TV service.",
            "source": "videos/satellite_dish.mp4",
            "thumbnail": "imgs/ds1.jpg",
            "detail_url": "#"
        },
        {
            'title': 'Video Intercom System',
            'category': 'Communication',
            'description': 'High-quality video intercom systems for secure communication at entry points.',
            'source': 'videos/icv1.mp4',
            'thumbnail': 'imgs/it1.jpg',
            'detail_url': '#'
        },
        # Add more video entries here
    ]
    
    
    return render(request, 'page/gallery.html', {'videos': videos})
        
        
def contact_view(request):
    form = ContactForm()
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()  # reset form after submission

    faqs = [
        ("What types of security systems do you install?", "We install CCTV, access control, alarm, and electric fence systems."),
        ("Do you offer maintenance services for installed systems?", "Yes, we offer comprehensive maintenance plans."),
        ("Can I get a custom security solution for my business?", "Absolutely. We provide tailored solutions."),
        ("What areas do you serve?", "We serve the NY area and surrounding cities."),
    ]

    context = {
        'form': form,
        'success': success,
        'faqs': faqs,
    }
    return render(request, 'page/contact.html', context)




# views.py
def about(request):
    team_members = [
        {
            'name': 'Isaac Mensah',
            'title': 'Founder & CEO',
            'description': 'Isaac is the driving force behind the company\'s vision and success.',
            'image_url': '/static/imgs/b1.jpg',
        },
        {
            'name': 'MR Richard',
            'title': 'Lead Engineer',
            'description': 'Mr Richard leads our technical innovations with over 10 years of experience.',
            'image_url': '/static/imgs/john.jpg',
        },
        {
            'name': 'Emily Johnson',
            'title': 'Marketing Director',
            'description': 'Emily crafts compelling campaigns that elevate our brand.',
            'image_url': '/static/imgs/emily.jpg',
        },
    ]
    return render(request, 'page/about.html', {'team_members': team_members})


def registration_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # You can define this route

    return render(request, 'page/registration.html', {'form': form})

def registration_success(request):
    return render(request, 'page/registration_success.html')
