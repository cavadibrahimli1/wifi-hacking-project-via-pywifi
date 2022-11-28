# Wifi hacking via Pywifi library 
In this repository, I will use pywifi in order to get the password of the WIFI. Do not forget that this is a simple process.

## ⚠️ Caution
This code is made for educational purposes. Illegal use of the code is ethically wrong, and at this time all responsibility falls on the person using the code.

## Let's start with our library
### Pywifi

![](https://img.shields.io/pypi/pyversions/pywifi.svg)
[![Build Status](https://travis-ci.com/awkman/pywifi.svg?branch=master)](https://travis-ci.com/awkman/pywifi)
[![PyPI version](https://badge.fury.io/py/pywifi.svg)](https://badge.fury.io/py/pywifi)

pywifi provides a cross-platform Python module for manipulating wireless
interfaces.

* Easy to use
* Supports Windows and Linux
 

## Prerequisites

On Linux, you will need to run wpa_supplicant to manipulate the wifi devices,
and then pywifi can communicate with wpa_supplicant through socket.

On Windows, the [Native Wifi] component comes with Windows versions greater
than Windows XP SP2.

## Installation

After installing the prerequisites listed above for your platform, you can
use pip to install from source:

    cd pywifi/
    pip install .

## Documentation

For the details of pywifi, please refer to [Documentation].

## Example

    import time
    import pywifi
    from pywifi import const

    wifi = pywifi.PyWiFi()

    iface = wifi.interfaces()[0]

    iface.disconnect()
    time.sleep(1)
    assert iface.status() in\
        [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

    profile = pywifi.Profile()
    profile.ssid = 'testap'
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = '12345678'

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    iface.connect(tmp_profile)
    time.sleep(30)
    assert iface.status() == const.IFACE_CONNECTED

    iface.disconnect()
    time.sleep(1)
    assert iface.status() in\
        [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]



[Native Wifi]: https://msdn.microsoft.com/en-us/library/windows/desktop/ms706556.aspx
[MIT License]: https://opensource.org/licenses/MIT
[Documentation]: https://github.com/awkman/pywifi/blob/master/DOC.md


### After downloading Pywifi 
- You have to create a password list. I wrote a code that does thos work for you, but be careful. If code runs on background too much, your PC could be crush. 
- After you run password generator code, it will create pwd.txt file in your current repository. You will use that document in our main code breaker code. 

### After creating password list
- You have to run our main code - password breaker.

## Find me on social media:

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/cavadibrahimli/)



#### I wrote comments within my code as much as possible. If there is something you do not understand, feel free to write me. 

## Authors

- [@cavadibrahimli1](https://www.github.com/cavadibrahimli1)


