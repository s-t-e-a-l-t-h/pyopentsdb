import unittest
from unittest import mock

from pyopentsdb import tsdb
from tests.testutils import get_mock_requests_get
from tests.testutils import GeneralUrlTestCase


class TsdbDopcachesTestCase(unittest.TestCase):
    __TETS_DROPCACHES__ = {
        "message": "Caches dropped",
        "status": "200"
    }

    def setUp(self):
        self._host = 'mockhttp://localhost:5896/'

        self._c = tsdb.tsdb_connection(self._host)

    @mock.patch('requests.Session.get', side_effect=get_mock_requests_get(None))
    def test_url(self, _):
        GeneralUrlTestCase.test_url(self, "/api/dropcaches/", "dropcaches")

    @mock.patch('requests.Session.get', side_effect=get_mock_requests_get(__TETS_DROPCACHES__))
    def test_config(self, _):
        response = self._c.dropcaches()
        self.assertEqual(sorted(response), sorted(TsdbDopcachesTestCase.__TETS_DROPCACHES__))
