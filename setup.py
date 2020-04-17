from setuptools import setup

setup(name='imagetovideo',
      version='0.2.1',
      description='Convert a set of images to a video',
      url='https://github.com/1llusion/imagetovideo',
      author='Christopher Darlington',
      author_email='chris.darlington.music@gmail.com',
      license='mit',
      packages=['imagetovideo'],
      install_requires=[
          'opencv-python',
      ],
      download_url = 'https://github.com/1llusion/imagetovideo/archive/v_0.2.1.tar.gz',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
        ],
)