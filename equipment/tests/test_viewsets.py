import json

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from equipment.models import Equipment
from equipment.tests.fixture import EquipmentFactory
from vessel.tests.fixture import VesselFactory


class EquipmentViewSetTests(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.vessel = VesselFactory.create()

    def test_perform_create(self) -> None:
        """
        Test creating a Equipment model per rest request.
        """
        data = {
            'name': 'compressor',
            'code': '5310B9D7',
            'location': 'Brazil',
            'vessel': self.vessel.id
        }
        response = self.client.post(reverse('equipment-list'), data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data.get('name'), response.data.get('name'))
        self.assertEqual(data.get('code'), response.data.get('code'))
        self.assertEqual(data.get('location'), response.data.get('location'))
        self.assertTrue(response.data.get('status'))

    def test_perform_not_create_duplicate(self) -> None:
        """
        Test not to create a duplicate Equipment model via rest request.
        """
        EquipmentFactory.create(code='2311A9D7', vessel=self.vessel)
        data = {
            'name': 'compressor2',
            'code': '2311A9D7',
            'location': 'Brazil',
            'vessel': self.vessel.id
        }

        response = self.client.post(reverse('equipment-list'), data=data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual('["Equipment with this Code already exists."]', json.dumps(response.data.get('code')))

    def test_list(self) -> None:
        """
        Test to return a list of created Equipments, via rest request.
        """
        response = self.client.get(reverse('equipment-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(0, len(response.data))

        EquipmentFactory.create_batch(2, vessel=self.vessel)
        EquipmentFactory.create_batch(3, status=False, vessel=self.vessel)
        self.assertEqual(5, Equipment.objects.all().count())

        response = self.client.get(reverse('equipment-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(5, len(response.data))

    def test_retrieve(self) -> None:
        """
        Test to return details of a Equipment model, via rest request.
        """
        equipment = EquipmentFactory.create(code='9100A3D1', vessel=self.vessel)
        response = self.client.get(reverse('equipment-detail', args=[equipment.id]))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(equipment.code, response.data.get('code'))

    def test_update(self) -> None:
        """
        Test to update the data of a Equipment model, via rest request.
        """
        equipment = EquipmentFactory.create(id=21, vessel=self.vessel)
        data = {
            'name': 'compressor9',
            'code': '9100A3D1',
            'location': 'Japan',
            'vessel': self.vessel.id,
        }
        self.assertNotEqual(equipment.code, data.get('code'))

        response = self.client.put(reverse('equipment-detail', args=[21]), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(data.get('code'), response.data.get('code'))

    def test_partial_update(self) -> None:
        """
        Test to partially update the data of a Equipment model, via request rest.
        """
        equipment = EquipmentFactory.create(id=22, vessel=self.vessel)
        data = {'name': 'compressor10'}
        self.assertNotEqual(equipment.name, data.get('name'))
        self.assertNotEqual(equipment.code, data.get('code'))
        self.assertNotEqual(equipment.location, data.get('location'))

        response = self.client.patch(reverse('equipment-detail', args=[22]), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(data.get('name'), response.data.get('name'))

    def test_destroy(self) -> None:
        """
        Test removing a Equipment model, via request rest.
        """
        EquipmentFactory.create(id=15, vessel=self.vessel)

        response = self.client.get(reverse('equipment-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTrue(1, len(response.data))

        response = self.client.delete(reverse('equipment-detail', args=[15]))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        response = self.client.get(reverse('equipment-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(0, len(response.data))

    def test_status_inactive_list_of_element(self) -> None:
        """
        Test to change the status to false on more than one element.
        """
        EquipmentFactory.create_batch(3, vessel=self.vessel)

        equipment_list = Equipment.objects.filter()
        self.assertEqual(3, equipment_list.count())

        for equipment in equipment_list:
            self.assertTrue(equipment.status)

        data = {'codes': [equipment.code for equipment in equipment_list]}

        response = self.client.post(reverse('equipment-status-inactive'), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        for equipment in response.data:
            self.assertFalse(equipment.get('status'))

    def test_status_inactive_one_element(self) -> None:
        """
        Test to change the status to false on an element.
        """
        equipment = EquipmentFactory.create(vessel=self.vessel)
        self.assertTrue(equipment.status)

        data = {'codes': [equipment.code]}

        response = self.client.post(reverse('equipment-status-inactive'), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        for equipment in response.data:
            self.assertFalse(equipment.get('status'))

    def test_status_inactive_empty_list(self) -> None:
        """
        Test to return error when trying to change the status to false in an empty list.
        """
        data = {'codes': []}

        response = self.client.post(reverse('equipment-status-inactive'), data=data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(
            'One or more equipment code must be inputted.', response.data.get('error', {}).get('message')
        )
