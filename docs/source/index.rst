iot-automator
=============
..
    |pypi-v| |pypi-pyversions| |pypi-l| |pypi-wheel| |tests|

    .. |pypi-v| image:: https://img.shields.io/pypi/v/websockets.svg
        :target: https://pypi.python.org/pypi/websockets

    .. |pypi-pyversions| image:: https://img.shields.io/pypi/pyversions/websockets.svg
        :target: https://pypi.python.org/pypi/websockets

    .. |pypi-l| image:: https://img.shields.io/pypi/l/websockets.svg
        :target: https://pypi.python.org/pypi/websockets
..

|tests|  

.. |tests| image:: https://github.com/mitchterrell/iot-automator/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/mitchterrell/iot-automator/actions/workflows/tests.yml
   

``iot-automator`` is a library for building complex IoT device automations using Python
with an emphasis on simplicity, robustness and scalability.

Here's how the library is used to control an IoT device environment:

.. literalinclude:: _examples/basic_start.py

``iot-automator`` works with many common, off the shelf hubs and devices, but introduces infinite freedom to automate any device or environment.
The library abstracts a number of popular IoT automation solutions, like WebThings Gateway, Samsung Smart Things,
Home Assistant, Amazon Alexa, OpenHAB, and more in the future.
The library provides a simple, object-oriented interface for building automation solutions that spans across these hubs and devices,
introducing a new level of flexibility and scalability to IoT automation.

An **execution engine** that runs on a variety of compute nodes and handles the execution of the automation modules. This engine emphasizes scheduled and proximity triggers (RFID) for running modules across multiple rooms in the enterprise environment. 
The engine supports per-user and per-device security levels to operate in secure, multi-user environments. 
The engine also provides scalability across the framework by offloading module execution to other Dense IoT nodes within a network. 


.. toctree::
   :hidden:
   :maxdepth: 2

   tutorials/index
   api/index
   user_guide/index
   topic_overview/index
   developer_docs/index
   about/index
