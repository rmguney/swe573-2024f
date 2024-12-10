from django.test.runner import DiscoverRunner
from django.conf import settings

class NoDbTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        """Use existing test database instead of creating a new one"""
        self.keepdb = True
        settings.DATABASES['default'] = settings.DATABASES['test']
        return []

    def teardown_databases(self, old_config, **kwargs):
        """Prevent database teardown"""
        pass

    def get_test_db_name(self):
        """Return the test database name without 'test_' prefix"""
        return settings.DATABASES['test']['NAME']