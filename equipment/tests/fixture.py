import factory

from equipment import COUNTRY_LIST
from equipment.models import Equipment

EQUIPMENT_NAME = [
    'ais',
    'arpa',
    'compressor',
    'ecdis',
    'lrit',
    'radar',
]


class EquipmentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Equipment

    name = factory.Faker('random_element', elements=EQUIPMENT_NAME)
    code = factory.Faker('bothify', text='####?#?#', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    location = factory.Faker('random_element', elements=[i[0] for i in COUNTRY_LIST])
