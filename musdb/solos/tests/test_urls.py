from django.test import TestCase
# from django.core.urlresolvers import resolve
from django.urls import reverse, resolve
from solos.views import index

class SolosURLsTestCase(TestCase):
    def test_root_url_uses_index_view(self):
        """
        Test that the root of the site resolves to the correct view function
        """

        # root = reverse(viewname='index')
        root = resolve('/')
        self.assertEqual(root.func, index)

