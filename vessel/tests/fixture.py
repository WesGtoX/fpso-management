import factory
from vessel.models import Vessel


class VesselFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Vessel

    code = factory.Faker('numerify', text='MV###')
