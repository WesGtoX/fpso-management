from django.db import IntegrityError
from django.test import TestCase

from equipment.models import Equipment
from vessel.tests.fixture import VesselFactory


class EquipmentModelTestCase(TestCase):

    def setUp(self) -> None:
        self.vessel = VesselFactory.create()

    def test_create_equipment(self) -> None:
        """
        Test to create a successful Equipment model.
        """
        equipment = Equipment.objects.create(
            name='compressor', code='5310B9D7',
            location='Brazil', vessel=self.vessel
        )
        self.assertEqual(equipment.name, 'compressor')
        self.assertEqual(equipment.code, '5310B9D7')
        self.assertEqual(equipment.location, 'Brazil')
        self.assertTrue(equipment.status)
        self.assertEqual(equipment.__str__(), 'compressor, 5310B9D7')

    def test_not_create_duplicate_equipment(self) -> None:
        """
        Test not to create a duplicate Equipment model.
        """
        Equipment.objects.create(name='compressor1', code='5320B5D3', location='Brazil', vessel=self.vessel)

        with self.assertRaises(IntegrityError) as context:
            Equipment.objects.create(name='compressor2', code='5320B5D3', location='Brazil', vessel=self.vessel)

        self.assertIn('UNIQUE constraint failed', str(context.exception))

    def test_update_equipment(self) -> None:
        """
        Test to update a Equipment model.
        """
        Equipment.objects.create(name='compressor3', code='5330B1D2', location='Brazil', vessel=self.vessel)
        equipment = Equipment.objects.get(code='5330B1D2')
        self.assertEqual(equipment.name, 'compressor3')
        self.assertEqual(equipment.code, '5330B1D2')
        self.assertEqual(equipment.location, 'Brazil')
        self.assertTrue(equipment.status)

        equipment.name = 'compressor5'
        equipment.save()

        self.assertTrue(Equipment.objects.filter(name='compressor5').exists())
        self.assertFalse(Equipment.objects.filter(name='compressor3').exists())

    def test_delete_equipment(self) -> None:
        """
        Test to delete a Equipment model.
        """
        Equipment.objects.create(name='compressor6', code='5630B1A2', location='Brazil', vessel=self.vessel)
        equipment = Equipment.objects.get(code='5630B1A2')

        equipment.delete()
        self.assertFalse(Equipment.objects.filter(code='5630B1A2').exists())
