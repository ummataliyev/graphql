from src.settings import default

default.INSTALLED_APPS.extend([
    "graphene_django",
])


GRAPHENE = {
    'SCHEMA': 'app.schema'
}
