#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os

class CppJWTConan(ConanFile):
    name = "cpp-jwt"
    version = "1.1.2"
    description = "JSON Web Token library for C++"
    topics = ("conan", "cpp-jwt", "auth" )
    url = "https://github.com/zinnion/cpp-jwt"
    homepage = "https://github.com/maurodelazeri/cpp-jwt"
    author = "Zinnion <mauro@zinnion.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    settings = "os", "compiler", "build_type", "arch"
    short_paths = True
    generators = "cmake"
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"
    options = {}
    default_options = ()

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def requirements(self):
        self.requires.add("gtest/1.8.1@zinnion/stable")
        self.requires.add("OpenSSL/1.1.1b@zinnion/stable")

    def configure(self):
        del self.settings.compiler.libcxx

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions['OPENSSL_ROOT_DIR'] = self.deps_cpp_info["OpenSSL"].rootpath
        cmake.definitions['GTEST_ROOT'] = self.deps_cpp_info["gtest"].rootpath
        cmake.configure(source_folder=self.source_subfolder, build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE.txt", dst="license", src=self.source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
