# [Racher API](http://rancher-api.hive.pt)

The Python Rancher API client.

## Reference

The Rancher API projects takes most of its reference implementation from the [Official Rancher API Documentation](http://docs.rancher.com/rancher/api/).

## Configuration

| Name | Type | Description |
| ----- | ----- | ----- |
| **RANCHER_BASE_URL** | `str` | The base URL to the rancher server of target (eg: `http://rancher.domain.com:8080/v2-beta/`) (defaults to `None`). |
| **RANCHER_USERNAME** | `str` | The username to be used for API authentication (defaults to `None`). |
| **RANCHER_PASSWORD** | `str` | The password to be used for API authentication (defaults to `None`). |

## License

Rancher API is currently licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/).

## Build Automation

[![Build Status](https://travis-ci.org/hivesolutions/rancher_api.svg?branch=master)](https://travis-ci.org/hivesolutions/rancher_api)
[![Coverage Status](https://coveralls.io/repos/hivesolutions/rancher_api/badge.svg?branch=master)](https://coveralls.io/r/hivesolutions/rancher_api?branch=master)
[![PyPi Status](https://img.shields.io/pypi/v/rancher_api.svg)](https://pypi.python.org/pypi/rancher_api)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/)
