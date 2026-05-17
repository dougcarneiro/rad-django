from django.db import migrations

def setup_analistas_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    
    # Models in edu app
    Livro = apps.get_model('edu', 'Livro')
    Autor = apps.get_model('edu', 'Autor')
    Editora = apps.get_model('edu', 'Editora')
    
    # Create group
    group, created = Group.objects.get_or_create(name='Analistas')
    
    # Permissions to add
    permissions_data = [
        (Livro, ['view_livro', 'add_livro', 'change_livro', 'delete_livro']),
        (Autor, ['view_autor', 'add_autor', 'change_autor', 'delete_autor']),
        (Editora, ['view_editora', 'add_editora', 'change_editora', 'delete_editora']),
    ]
    
    for model, codenames in permissions_data:
        content_type = ContentType.objects.get_for_model(model)
        permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=codenames
        )
        for perm in permissions:
            group.permissions.add(perm)

def remove_analistas_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name='Analistas').delete()

class Migration(migrations.Migration):
    dependencies = [
        ('edu', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(setup_analistas_group, remove_analistas_group),
    ]
