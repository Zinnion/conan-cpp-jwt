#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os

class CppJwtConan(ConanFile):
    name = "cpp-jwt"
    version = "1.1.2"
    url = "https://github.com/zinnion/conan-cpp-jwt"
    description = "A C++ library for handling JWT tokens"
    license = "https://github.com/maurodelazeri/cpp-jwt/blob/master/LICENSE"
    no_copy_source = True
    build_policy = "always"
    requires = "OpenSSL/1.1.1b@zinnion/stable", "jsonformoderncpp/3.6.1@zinnion/stable"

    def source(self):
        source_url = "https://github.com/maurodelazeri/cpp-jwt"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, "sources")

    def package_id(self):
        self.info.header_only()

    def package(self):
        self.copy(pattern="LICENSE")
        self.copy(pattern="*.[i|h]pp", dst="include", src="sources/include", keep_path=True)
