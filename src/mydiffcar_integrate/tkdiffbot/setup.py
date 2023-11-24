from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'tkdiffbot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name, "launch"), glob("launch/*.launch.py")),
        (os.path.join("share", package_name, "urdf"), glob("urdf/*.urdf")),
        (os.path.join("share", package_name, "urdf"), glob("urdf/*.urdf.xacro")),
        (os.path.join("share", package_name, "mesh/diff_2w"), glob("mesh/diff_2w/*.STL")),
        (os.path.join("share", package_name, "worlds"), glob("worlds/*.world")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ctk',
    maintainer_email='blairan121122885@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
