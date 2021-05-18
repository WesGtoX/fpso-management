import json

from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from equipment.tests.fixture import EquipmentFactory
from vessel.tests.fixture import VesselFactory

User = get_user_model()


class VesselViewSetTests(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_perform_create(self) -> None:
        """
        Test creating a Vessel model per rest request.
        """
        data = {'code': 'MV102'}
        response = self.client.post(reverse('vessel-list'), data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data.get('code'), response.data.get('code'))

    def test_perform_not_create_duplicate(self) -> None:
        """
        Test not to create a duplicate Vessel model via rest request.
        """
        VesselFactory.create(code='MV100')
        data = {'code': 'MV100'}

        response = self.client.post(reverse('vessel-list'), data=data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual('["Vessel with this Code already exists."]', json.dumps(response.data.get('code')))

    def test_list(self) -> None:
        """
        Test to return a list of created Vessels, via rest request.
        """
        response = self.client.get(reverse('vessel-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(0, len(response.data))

        VesselFactory.create_batch(5)

        response = self.client.get(reverse('vessel-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(5, len(response.data))

    def test_retrieve(self) -> None:
        """
        Test to return details of a Vessel model, via rest request.
        """
        vessel = VesselFactory.create(code='MV158')
        response = self.client.get(reverse('vessel-detail', args=[vessel.id]))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(vessel.code, response.data.get('code'))

    def test_update(self) -> None:
        """
        Test to update the data of a Vessel model, via rest request.
        """
        vessel = VesselFactory.create(id=21)
        data = {'code': 'MV001'}
        self.assertNotEqual(vessel.code, data.get('code'))

        response = self.client.put(reverse('vessel-detail', args=[21]), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(data.get('code'), response.data.get('code'))

    def test_partial_update(self) -> None:
        """
        Test to partially update the data of a Vessel model, via request rest.
        """
        vessel = VesselFactory.create(id=22)
        data = {'code': 'MV002'}
        self.assertNotEqual(vessel.code, data.get('code'))

        response = self.client.patch(reverse('vessel-detail', args=[22]), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(data.get('code'), response.data.get('code'))

    def test_destroy(self) -> None:
        """
        Test removing a Vessel model, via request rest.
        """
        VesselFactory.create(id=15)

        response = self.client.get(reverse('vessel-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTrue(1, len(response.data))

        response = self.client.delete(reverse('vessel-detail', args=[15]))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        response = self.client.get(reverse('vessel-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(0, len(response.data))


class VesselEquipmentViewSetTests(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.vessel = VesselFactory.create()

    def test_vessel_equipment_list(self) -> None:
        """
        Test to return the active equipment of a specific vessel.
        """
        EquipmentFactory.create_batch(2, status=False, vessel=self.vessel)
        EquipmentFactory.create_batch(3, status=True, vessel=self.vessel)
        response = self.client.get(reverse('vessel-equipments', args=[self.vessel.id]))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(3, len(response.data))
