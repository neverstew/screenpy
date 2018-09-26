from selenium.webdriver.common.by import By
from unittest import TestCase

from ..page_objects import model_form, material_design_dropdown, material_design_dropdown_option


class TestDjangoLocators(TestCase):
    def test_field(self):
        locator = model_form.field("username")

        self.assertEqual(By.NAME, locator.strategy)
        self.assertEqual("username", locator.locator)

    def test_field_error(self):
        locator = model_form.field_error("username")

        self.assertEqual(By.CSS_SELECTOR, locator.strategy)
        self.assertTrue("#id_username_container" in locator.locator)


class TestDjangoMaterialLocators(TestCase):
    def test_material_design_dropdown(self):
        locator = material_design_dropdown("username")

        self.assertEqual(By.XPATH, locator.strategy)
        self.assertTrue("@id='id_username_container'" in locator.locator)
        self.assertTrue("//input" in locator.locator)

    def test_material_design_dropdown_option(self):
        locator = material_design_dropdown_option("username", "this_one")

        self.assertEqual(By.XPATH, locator.strategy)
        self.assertTrue("@id='id_username_container'" in locator.locator)
        self.assertTrue("//span[contains(., 'this_one')]" in locator.locator)
