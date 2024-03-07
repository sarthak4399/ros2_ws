from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sarthak',
    maintainer_email='sarthakkhandare21@gmail.com',
    description='Guardian Robot:The Robot For The Industrial Purpose',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "my_first_node = my_robot_controller.my_first_node:main",
            "draw_circle = my_robot_controller.drawCircle:main",
            "pose_subcriber = my_robot_controller.pose_subcribe:main",
            "turtel_controller = my_robot_controller.turtel_controller:main"
        ],
    },
)
