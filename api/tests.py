import unittest

import coverage
from app.models.indicators import layersData
from tests.routes import test_indicators

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(test_indicators.TestIndicators)
    """ for layer in layersData:
        suite = unittest.TestSuite()
        suite.addTest(test_indicators.TestIndicators(layersData[layer],'test_tablenameschema_exists')) """
    unittest.TextTestRunner(verbosity=2).run(suite)
