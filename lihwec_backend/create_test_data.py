from events.models import Event, Category, Organization
from datetime import date, time

# Crear categorías
competencia, _ = Category.objects.get_or_create(name="competencia", defaults={"display_name": "Competencia"})
evento, _ = Category.objects.get_or_create(name="evento", defaults={"display_name": "Evento de Difusión"})

# Crear organizaciones
nasa, _ = Organization.objects.get_or_create(name="NASA", defaults={"description": "Agencia Espacial"})
google, _ = Organization.objects.get_or_create(name="Google", defaults={"description": "Tecnología"})
microsoft, _ = Organization.objects.get_or_create(name="Microsoft", defaults={"description": "Software"})

# Crear eventos de prueba
Event.objects.get_or_create(
    name="Google DevFest 2025",
    defaults={
        "date": date(2025, 8, 15),
        "time": time(10, 0),
        "modality": "presencial",
        "location": "Centro de Convenciones",
        "organization": google,
        "category": evento,
        "type": "DevFest",
        "image": "https://example.com/devfest.jpg",
        "description": "Evento de desarrollo de Google con charlas y workshops",
        "link": "https://devfest.google.com"
    }
)

Event.objects.get_or_create(
    name="Microsoft Hackathon 2025",
    defaults={
        "date": date(2025, 9, 10),
        "time": time(9, 0),
        "modality": "hibrido",
        "location": "Online y Seattle",
        "organization": microsoft,
        "category": competencia,
        "type": "Hackathon",
        "image": "https://example.com/mshack.jpg",
        "description": "Hackathon de Microsoft para desarrolladores",
        "link": "https://hackathon.microsoft.com"
    }
)

Event.objects.get_or_create(
    name="NASA Innovation Challenge",
    defaults={
        "date": date(2025, 10, 5),
        "time": time(14, 0),
        "modality": "virtual",
        "location": "Online",
        "organization": nasa,
        "category": competencia,
        "type": "Challenge",
        "image": "https://example.com/nasa.jpg",
        "description": "Desafío de innovación de la NASA",
        "link": "https://nasa.gov/challenge"
    }
)

print("Datos de prueba creados exitosamente!")
print(f"Total eventos: {Event.objects.count()}")
print(f"Total categorías: {Category.objects.count()}")
print(f"Total organizaciones: {Organization.objects.count()}")
