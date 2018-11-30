#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostFusionConan(base.BoostBaseConan):
    name = "boost_fusion"
    url = "https://github.com/bincrafters/conan-boost_fusion"
    lib_short_names = ["fusion"]
    header_only_libs = ["fusion"]
    b2_requires = [
        "boost_config",
        "boost_container_hash",
        "boost_core",
        "boost_function_types",
        "boost_mpl",
        "boost_preprocessor",
        "boost_static_assert",
        "boost_tuple",
        "boost_type_traits",
        "boost_typeof",
        "boost_utility"
    ]
