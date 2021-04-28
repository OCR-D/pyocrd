import logging
from re import match
from tempfile import TemporaryDirectory

from tests.base import CapturingTestCase as TestCase, main, FIFOIO, assets
from tests.data import DummyProcessor
from ocrd import Resolver, run_processor

from ocrd_utils import (
    pushd_popd,
    getLevelName,
    setOverrideLogLevel,
    disableLogging,
    initLogging,
    getLogger,
    LOG_FORMAT,
    LOG_TIMEFMT
)

# "00:00:00.000 "
TIMEFMT_RE = r'\d\d:\d\d:\d\d\.(\d+)? '

class TestLogging(TestCase):

    def setUp(self):
        super().setUp()
        disableLogging()

    def test_setOverrideLogLevel(self):
        initLogging()
        rootLogger = logging.getLogger('')
        somelogger = getLogger('foo.bar')
        somelogger.setLevel(getLevelName('ERROR'))
        setOverrideLogLevel('ERROR')
        self.assertEqual(rootLogger.getEffectiveLevel(), logging.ERROR)
        self.assertEqual(somelogger.getEffectiveLevel(), logging.ERROR)
        notherlogger = getLogger('bar.foo')
        self.assertEqual(notherlogger.getEffectiveLevel(), logging.ERROR)
        setOverrideLogLevel('INFO')
        somelogger = getLogger('foo.bar')

    def test_multiple_initLogging(self):
        disableLogging()
        initLogging()
        self.capture_out_err()
        initLogging()
        out = '\n'.join(self.capture_out_err())
        assert 'initLogging was called multiple times' in out
        assert __file__ in out

    def test_getLogger_before_initLogging(self):
        disableLogging()
        self.capture_out_err()
        getLogger('foo')
        out = '\n'.join(self.capture_out_err())
        print(out)
        assert 'getLogger was called before initLogging' in out
        assert __file__ in out

    def test_getLevelName(self):
        self.assertEqual(getLevelName('ERROR'), logging.ERROR)
        self.assertEqual(getLevelName('FATAL'), logging.ERROR)
        self.assertEqual(getLevelName('OFF'), logging.CRITICAL)

    def test_logging_really_non_duplicate(self):
        initLogging()
        child_logger = getLogger('a.b')
        print(child_logger)
        parent_logger = getLogger('a')
        root_logger = getLogger('')
        self.assertFalse(root_logger.propagate, 'root logger should not propagate')
        self.assertTrue(parent_logger.propagate, 'parent has no handler => do propagate')
        self.assertTrue(child_logger.propagate, 'child no handler => do propagate')

        root_capture = FIFOIO(256)
        root_handler = logging.StreamHandler(root_capture)
        root_handler.setFormatter(logging.Formatter(fmt=LOG_FORMAT, datefmt=LOG_TIMEFMT))
        root_logger.addHandler(root_handler)

        parent_capture = FIFOIO(256)
        parent_handler = logging.StreamHandler(parent_capture)
        parent_handler.setFormatter(logging.Formatter(fmt=LOG_FORMAT, datefmt=LOG_TIMEFMT))
        parent_logger.addHandler(parent_handler)

        # parent_logger = getLogger('a')
        # self.assertFalse(parent_logger.propagate, 'parent has handler now => do not propagate')

        self.assertTrue(child_logger.propagate, 'child has still no handler => do propagate')

        child_logger.error('test')

        root_str = root_capture.getvalue()
        parent_str = parent_capture.getvalue()
        print('root_str=%s' % root_str)
        print('parent_str=%s' % parent_str)

        self.assertEqual(root_str.count('\n'), 0)
        self.assertEqual(parent_str.count('\n'), 1)

        # root_logger.removeHandler(root_handler) # remove stream handler so we actually see the output
        # root_logger.info('root_str=%s', root_str)
        # root_logger.info('parent_str=%s', parent_str)

    def test_logging_non_duplicate(self):
        """
        Verify that child loggers don't propagate a log message they handle
        """
        initLogging()

        root_logger = logging.getLogger('')
        self.assertTrue(root_logger.handlers, 'root logger has at least 1 handler')

        parent_capture = FIFOIO(256)
        parent_handler = logging.StreamHandler(parent_capture)
        parent_handler.setFormatter(logging.Formatter(fmt=LOG_FORMAT, datefmt=LOG_TIMEFMT))
        parent_logger = getLogger('foo')
        self.assertTrue(parent_logger.propagate, 'no handler on logger => propagate')
        parent_logger.addHandler(parent_handler)
        parent_logger = getLogger('foo')
        self.assertFalse(parent_logger.propagate, 'should not propagate because StreamHandler has been attached')

        child_logger = getLogger('foo.bar')
        self.assertTrue(child_logger.propagate, 'no handler on logger => propagate')
        child_logger.setLevel('DEBUG')

        child_logger.error('first error')

        child_capture = FIFOIO(256)
        child_handler = logging.StreamHandler(child_capture)
        child_handler.setFormatter(logging.Formatter(fmt=LOG_FORMAT, datefmt=LOG_TIMEFMT))

        child_logger.debug('first debug')

        child_logger.addHandler(child_handler)
        child_logger = getLogger('foo.bar')
        self.assertFalse(child_logger.propagate, 'should not propagate because StreamHandler has been attached')

        child_logger.debug('second debug')
        child_logger.error('second error')

        parent_output = parent_capture.getvalue()
        parent_capture.close()
        child_output = child_capture.getvalue()
        child_capture.close()
        # print('parent', parent_output)
        # print('child', child_output)

        self.assertTrue(match(TIMEFMT_RE + 'ERROR foo.bar - first error\n', parent_output),
                'parent received first error but not second error nor first debug')
        self.assertTrue(match("\n".join([
            TIMEFMT_RE + 'DEBUG foo.bar - second debug',
            TIMEFMT_RE + 'ERROR foo.bar - second error',
            ]), child_output),
                'child received second error and debug but not first error and debug')

    def testProcessorProfiling(self):
        initLogging()
        log_capture_string = FIFOIO(256)
        ch = logging.StreamHandler(log_capture_string)
        ch.setFormatter(logging.Formatter(LOG_FORMAT))
        getLogger('ocrd.process.profile').setLevel('DEBUG')
        getLogger('ocrd.process.profile').addHandler(ch)

        run_processor(DummyProcessor, resolver=Resolver(), mets_url=assets.url_of('SBB0000F29300010000/data/mets.xml'))

        log_contents = log_capture_string.getvalue()
        log_capture_string.close()
        # with open('/tmp/debug.log', 'w') as f:
        #     f.write(log_contents)
        # Check whether profile information has been logged. Dummy should finish in under 0.1s
        # print(log_contents)
        assert "Executing processor 'ocrd-test' took 0" in log_contents
        # self.assertTrue(match(r'.*Executing processor \'ocrd-test\' took 0.\d+s.*', log_contents))

    def test_tmpConfigfile(self):
        self.assertNotEqual(logging.getLogger('').getEffectiveLevel(), logging.NOTSET)
        with pushd_popd(tempdir=True) as tempdir:
            with open('ocrd_logging.conf', 'w') as f:
                # write logging configuration file (MWE)
                f.write('''
                    [loggers]
                    keys=root

                    [handlers]
                    keys=consoleHandler

                    [formatters]
                    keys=

                    [logger_root]
                    level=ERROR
                    handlers=consoleHandler

                    [handler_consoleHandler]
                    class=StreamHandler
                    formatter=
                    args=(sys.stdout,)
                    ''')
            # this will call logging.config.fileConfig with disable_existing_loggers=True,
            # so the defaults from the import-time initLogging should be invalided
            initLogging()
            # ensure log level is set from temporary config file
            self.assertEqual(logging.getLogger('').getEffectiveLevel(), logging.ERROR)

if __name__ == '__main__':
    main(__file__)
