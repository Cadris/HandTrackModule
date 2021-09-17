from setuptools import setup, find_packages

classifiers = [
	'Development Status :: 5 - Production/Stable',
	'Intended Audience :: Education',
	'Operating System :: Microsoft :: Windows :: Windows 10',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 3'
]

setup(
	name='Silver-HandTrackingModule',
	version='1.0.0',
	description='Track the Hands from Web Cam as default',
	long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
	url='https://github.com/Cadris/HandTrackModule',
	author='Sayan Dasgupta',
	author_email='cadrissilver@gmail.com',
	license='MIT',
	classifiers=classifiers,
	keywords='hand handtracker handtrackermodule',
	packages=find_packages(),
	install_requires=['opencv-python', 'mediapipe']
)