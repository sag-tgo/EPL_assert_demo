from pysys.basetest import BaseTest
from apama.correlator import CorrelatorHelper
import os

class PySysTest(BaseTest):
	def execute(self):
		corr = CorrelatorHelper(self, name='correlator')
		corr.start(logfile='correlator.log', arguments=[
			'-Dasserts=true',
			'--config', self.input + '/correlator.yaml'
		])
		corr.injectEPL(os.getenv('APAMA_HOME','') + '/monitors/ManagementImpl.mon')
		corr.injectEPL(os.getenv('APAMA_HOME','') + '/monitors/Management.mon')

		corr.injectEPL('../../../src/Assert.mon')
		corr.injectEPL('../../../src/AssertHelper.mon')

		corr.injectEPL('EventDefs.mon')
		
		for test in ['ConfigAssert.mon', 'DebugAssert.mon', 
					'SimpleAssert.mon', 'SimpleAssert2.mon',
					'Demo.mon']:
			corr.injectEPL(test)
			corr.flush()
		corr.shutdown()

	def validate(self):
		self.assertLineCount('correlator.log', 'ERROR', condition='==0')
		self.assertGrep('correlator.log', 'ERROR', contains=False)
