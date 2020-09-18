from unittest import TestCase

import requests

from . import BASE_URL

url = BASE_URL + '/upload/export/raster/nuts'


class TestExportRasterNuts(TestCase):
    def test_post(self):
        """
        this test will pass the upload/export/raster/nuts method
        """
        payload = {
            'layers': 'heat_tot_curr_density_nuts3',
            'year': '2012',
            'nuts': ['AT130']
        }

        expected_status = 200

        output = requests.post(url, json=payload)

        assert output.status_code == expected_status

    def test_port_wrong_parameters(self):
        """
        this test will fail because the wrong parameters are given
        """
        payload = {
            'layfdsers': 'heat_tot_curr_density_nuts3',
            'yeafdsar': '2012',
            'nutss': ['AT130']
        }

        output = requests.post(url, json=payload)

        expected_status = '531'

        assert output.json()['error']['status'] == expected_status

    def test_post_wrong_layer(self):
        """
        this test will fail because the layer is not a lau2 or nuts3
        """
        payload = {
            'layers': 'heat_tot_curr_density_nuts2',
            'year': '2012',
            'nuts': ['AT130']
        }

        output = requests.post(url, json=payload)

        expected_status = '532'

        assert output.json()['error']['status'] == expected_status
