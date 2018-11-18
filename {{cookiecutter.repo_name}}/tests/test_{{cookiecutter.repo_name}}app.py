#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from kivy.clock import Clock
from {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}}app import {{cookiecutter.repo_name | capitalize}}App


class Test{{cookiecutter.repo_name | capitalize}}App(unittest.TestCase):
    """TestCase for {{cookiecutter.repo_name|capitalize}}App.
    """

    def setUp(self):
        self.app = {{cookiecutter.repo_name | capitalize}}App()
        Clock.schedule_once(lambda *x: self.app.stop(), 0.000001)
        self.app.run()

    def test_name(self):
        self.assertEqual(self.app.get_application_name(), '{{ cookiecutter.project_name }}')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
