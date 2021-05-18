from django.db import IntegrityError
from django.test import TestCase

from vessel.models import Vessel


class VesselModelTestCase(TestCase):

    def test_create_vessel(self) -> None:
        """
        Test to create a successful Vessel model.
        """
        vessel = Vessel.objects.create(code='MV102')
        self.assertEqual(vessel.code, 'MV102')
        self.assertEqual(vessel.__str__(), 'MV102')

    def test_not_create_duplicate_vessel(self) -> None:
        """
        Test not to create a duplicate Vessel model.
        """
        Vessel.objects.create(code='MV103')

        with self.assertRaises(IntegrityError) as context:
            Vessel.objects.create(code='MV103')

        self.assertIn('UNIQUE constraint failed', str(context.exception))

    def test_update_vessel(self) -> None:
        """
        Test to update a Vessel model.
        """
        Vessel.objects.create(code='MV104')
        vessel = Vessel.objects.get(code='MV104')
        self.assertEqual(vessel.code, 'MV104')

        vessel.code = 'MV105'
        vessel.save()

        self.assertTrue(Vessel.objects.filter(code='MV105').exists())
        self.assertFalse(Vessel.objects.filter(code='MV104').exists())

    def test_delete_vessel(self) -> None:
        """
        Test to delete a Vessel model.
        """
        Vessel.objects.create(code='MV106')
        vessel = Vessel.objects.get(code='MV106')

        vessel.delete()
        self.assertFalse(Vessel.objects.filter(code='MV106').exists())
