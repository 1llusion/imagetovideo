from setuptools import setup

setup(name='imagetovideo',
      version='0.2.1',
      description='Convert a set of images to a video',
      url='https://github.com/1llusion/imagetovideo',
      author='Christopher Darlington',
      author_email='chris.darlington.music@gmail.com',
      license='MIT',
      packages=['imagetovideo'],
      install_requires=[
          'opencv-python',
      ],
      zip_safe=False)