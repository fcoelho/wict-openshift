# coding: utf-8

from setuptools import setup

setup(
	name='WICT',
	version='0.1',
	description='Sistema de revisão para o VII WICT',
	author='Felipe Bessa Coelho',
	author_email='fcoelho.9@gmail.com',
	url='http://bitbucket.org/fcoelho/wict',
	install_requires=[
		'greenlet',
		'gevent',
		'Django==1.5.1',
		'Unipath==1.0',
		'django-debug-toolbar==0.9.4',
		'django-sendfile==0.3.0',
		'pyPdf==1.13',
		'django-signup==0.1',
	],
	dependency_links = [
		'https://bitbucket.org/fcoelho/django-signup/get/tip.zip#egg=django-signup-0.1'
	]
)
