# Generated manually to handle data migration

from django.db import migrations, models
import django.db.models.deletion


def populate_types_and_migrate_data(apps, schema_editor):
    """
    Crea los registros de Type basados en los datos existentes
    y migra los datos del campo type (CharField) al nuevo campo type_new (ForeignKey)
    """
    Event = apps.get_model('events', 'Event')
    Type = apps.get_model('events', 'Type')
    
    # Obtener todos los tipos únicos de los eventos existentes
    existing_types = set(Event.objects.values_list('type', flat=True))
    
    # Crear los registros de Type
    type_objects = {}
    for type_name in existing_types:
        if type_name:  # Solo si no es None o string vacío
            type_obj, created = Type.objects.get_or_create(name=type_name)
            type_objects[type_name] = type_obj
            if created:
                print(f"Creado tipo: {type_name}")
    
    # Migrar los datos del campo type al campo type_new
    for event in Event.objects.all():
        if event.type and event.type in type_objects:
            event.type_new = type_objects[event.type]
            event.save()
            print(f"Migrado evento {event.id}: {event.type} -> Type ID {event.type_new.id}")


def reverse_populate_types_and_migrate_data(apps, schema_editor):
    """
    Reversa la migración copiando datos de type_new de vuelta a type
    """
    Event = apps.get_model('events', 'Event')
    
    for event in Event.objects.all():
        if event.type_new:
            event.type = event.type_new.name
            event.save()


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_link'),
    ]

    operations = [
        # Paso 1: Crear el modelo Type
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        
        # Paso 2: Añadir campo temporal type_new como ForeignKey
        migrations.AddField(
            model_name='event',
            name='type_new',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, to='events.type'),
        ),
        
        # Paso 3: Migrar datos
        migrations.RunPython(
            populate_types_and_migrate_data,
            reverse_populate_types_and_migrate_data,
        ),
        
        # Paso 4: Eliminar el campo type original
        migrations.RemoveField(
            model_name='event',
            name='type',
        ),
        
        # Paso 5: Renombrar type_new a type
        migrations.RenameField(
            model_name='event',
            old_name='type_new',
            new_name='type',
        ),
        
        # Paso 6: Hacer el campo obligatorio (quitar null=True, blank=True)
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.type'),
        ),
    ]
