from django.test import TestCase
from django.urls import reverse, resolve
from threef.views import (
    RegisterationAPIView,
    LoginAPIView,
    upload_file_view,
    update_resolved_status,
    toggle_comment_selected,
    search,
    get_user,
)

class UrlsTest(TestCase):
    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, RegisterationAPIView)

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, LoginAPIView)

    def test_upload_file_url_resolves(self):
        url = reverse('upload_file')
        self.assertEqual(resolve(url).func, upload_file_view)

    def test_update_resolved_status_url_resolves(self):
        url = reverse('update_resolved', kwargs={'thread_id': 1})
        self.assertEqual(resolve(url).func, update_resolved_status)

    def test_toggle_comment_selected_url_resolves(self):
        url = reverse('toggle_comment_selected', kwargs={'comment_id': 1})
        self.assertEqual(resolve(url).func, toggle_comment_selected)
        