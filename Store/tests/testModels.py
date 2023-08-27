from django.test import TestCase

from Store.models import Category, Product

from django.contrib.auth.models import User

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name="Devops", slug="devops")

    def testCategoryModelEntry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def testCategoryModelEntry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'Devops')

class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name="DevOps", slug="devops")
        User.objects.create(username="Jamb")
        self.data1 = Product.objects.create(category_id=1, title='Docker', createdBy_id=1, slug="Devops", price=45.99, image="dockerImg")

    def testProductsModelEntry(self):
        """
        Test Product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "Docker")