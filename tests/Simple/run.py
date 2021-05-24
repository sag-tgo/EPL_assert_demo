from pysys.basetest import BaseTest
from apama.correlator import CorrelatorHelper
import os

class PySysTest(BaseTest):
	def execute(self):
		corr = CorrelatorHelper(self, name='correlator')
		corr.start(logfile='correlator.log')
		corr.injectEPL(os.getenv('APAMA_HOME','') + '/monitors/ManagementImpl.mon')
		corr.injectEPL(os.getenv('APAMA_HOME','') + '/monitors/Management.mon')

		corr.injectEPL('../../../src/Assert.mon')

		corr.injectEPL('Demo.mon')
		corr.flush()
		corr.shutdown()

	def validate(self):
		self.assertLineCount('correlator.log', 'ERROR', condition='==0')
		self.assertGrep('correlator.log', 'ERROR', contains=False)
