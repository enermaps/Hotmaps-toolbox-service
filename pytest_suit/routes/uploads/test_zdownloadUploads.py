from unittest import TestCase

import requests

from . import BASE_URL, test_token

url = BASE_URL + '/upload/download'


class TestDownload(TestCase):
    def test_post_working(self):
        """
        this test will pass the upload/download method
        """
        list_url = BASE_URL + '/upload/list'
        payload = {
            'token': test_token,
        }
        
        output = requests.post(list_url, json=payload)
        # should be the file added in add 'test_addUploads.py'
        test_upload_id = sorted(output.json()['uploads'], key=lambda upload: upload['id'], reverse=True)[0]['id']

        payload = {
            'token': test_token,
            'id': test_upload_id
        }

        expected_status = 200

        output = requests.post(url, json=payload)

        assert output.status_code == expected_status

    def test_download_missing_parameter(self):
        """
        this test will fail because the given parameters are wrong
        """
        payload = {
            'sdafid': -5,
            'togfdken': test_token,
        }

        output = requests.post(url, json=payload)

        expected_status = '531'

        assert output.json()['error']['status'] == expected_status

    def test_download_user_unidentified(self):
        """
        this test will pass the uploads/add method
        """
        payload = {
            'id': -5,
            'token': 'ThisIsAWrongToken',
        }

        output = requests.post(url, json=payload)

        expected_status = '539'

        assert output.json()['error']['status'] == expected_status

    def test_download_upload_not_existing(self):
        """
        this test will pass the uploads/add method
        """
        payload = {
            'id': -5,
            'token': test_token,
        }

        output = requests.post(url, json=payload)

        expected_status = '543'

        assert output.json()['error']['status'] == expected_status

