from pysys.constants import *
from pysys.basetest import BaseTest
from apama.correlator import CorrelatorHelper
import os


class PySysTest(BaseTest):
	def execute(self):
		corr = CorrelatorHelper(self, name='correlator')
		corr.start(logfile='correlator.log', arguments=[
			'--applicationLogLevel', 'DEBUG',
			'-Dasserts=true'])
		corr.injectEPL('../../../src/AssertHelper.mon')
		corr.injectEPL('../../../src/callback/Assert.mon')
		tests = os.listdir(self.input)
		tests.sort()
		for test in tests:
			if test.endswith('.mon'):
				corr.injectEPL(test)
				corr.flush()
		corr.shutdown()

	def validate(self):
		self.assertLineCount('correlator.log', 'ERROR', condition='==0')
		self.assertGrep('correlator.log', 'ERROR', contains=False)
