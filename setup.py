from setuptools import setup

setup(name='Image To Video',
      version='0.1',
      description='Convert a set of images to a video',
      url='https://github.com/1llusion/imagetovideo',
      author='Christopher Darlington',
      author_email='chris.darlington.music@gmail.com',
      license='MIT',
      packages=['imagetovideo'],
      install_requires=[
          'opencv',
      ],
      zip_safe=False)