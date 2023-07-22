from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='Clean and sort folders',
      url='http://github.com/dummy_user/useful',
      author='Serhii Zub',
      author_email='05hello.world11@gmail.com',
      license='MIT',
      classifiers = [
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"],
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:start_prog']})