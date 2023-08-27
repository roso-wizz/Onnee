from unittest import skip

from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User

from django.urls import reverse

from django.http import HttpRequest

from Store.views import allProducts

from Store.models import Category, Product


#@skip("demonstrating skipping")
#class TestSkip(TestCase):
#    def test_skip_example(self):
#        pass

class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name="DevOps", slug="devops")
        User.objects.create(username="Jamb")
        self.data1 = Product.objects.create(category_id=1, title='Docker', createdBy_id=1, slug="DevOps", price=45.99, image="dockerImg")
    
    def testUrlAllowedHosts(self):
        """
        Test Allowed Hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def testProductDetailUrl(self):
        """
        Test Product response status
        """
        response = self.c.get(reverse('store:product_detail', args=['DevOps']))
        self.assertEqual(response.status_code, 200)

    def testCategoryDetailUrl(self):
        """
        Test Category response status
        """
        response = self.c.get(reverse('store:category_list', args=['devops']))
        self.assertEqual(response.status_code, 200)

    def testHomePageHtml(self):
        request = HttpRequest()
        response = allProducts(request)
        html = response.content.decode("utf8")
        print(html)
        self.assertIn('<title>Home</title>', html)
        #self.assertTrue(html.startswith('{% extends "../base.html" %}'))
        self.assertEqual(response.status_code, 200)


    def testViewFunction(self):
        request = self.factory.get('/item/laravel')
        response = allProducts(request)
        html = response.content.decode("utf8")
        self.assertIn('<title>Home</title>', html)
        self.assetEqual(response.status_code, 200)
        