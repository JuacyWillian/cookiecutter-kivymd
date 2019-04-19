import unittest

from kivy.clock import Clock

from {{cookiecutter.repo_name}} import {{cookiecutter.main_class_name}}App


class Test{{cookiecutter.main_class_name}}App(unittest.TestCase):
    """TestCase for {{cookiecutter.main_class_name}}App."""

    def setUp(self):
        self.app = {{cookiecutter.main_class_name}}App()
        Clock.schedule_once(lambda *x: self.app.stop(), 0.000001)
        self.app.run()

    def test_name(self):
        self.assertEqual(
            self.app.get_application_name(), '{{ cookiecutter.project_name }}')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
