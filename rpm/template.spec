%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-rclpy
Version:        3.3.7
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rclpy package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-ament-index-python
Requires:       ros-humble-builtin-interfaces
Requires:       ros-humble-rcl
Requires:       ros-humble-rcl-action
Requires:       ros-humble-rcl-interfaces
Requires:       ros-humble-rcl-lifecycle
Requires:       ros-humble-rcl-logging-interface
Requires:       ros-humble-rcl-yaml-param-parser
Requires:       ros-humble-rmw
Requires:       ros-humble-rmw-implementation
Requires:       ros-humble-rosgraph-msgs
Requires:       ros-humble-rosidl-runtime-c
Requires:       ros-humble-rpyutils
Requires:       ros-humble-unique-identifier-msgs
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-pybind11-vendor
BuildRequires:  ros-humble-python-cmake-module
BuildRequires:  ros-humble-rcl
BuildRequires:  ros-humble-rcl-action
BuildRequires:  ros-humble-rcl-lifecycle
BuildRequires:  ros-humble-rcl-logging-interface
BuildRequires:  ros-humble-rcl-yaml-param-parser
BuildRequires:  ros-humble-rcpputils
BuildRequires:  ros-humble-rcutils
BuildRequires:  ros-humble-rmw
BuildRequires:  ros-humble-rmw-implementation
BuildRequires:  ros-humble-rmw-implementation-cmake
BuildRequires:  ros-humble-rosidl-runtime-c
BuildRequires:  ros-humble-unique-identifier-msgs
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-humble-ament-cmake-gtest
BuildRequires:  ros-humble-ament-cmake-pytest
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
BuildRequires:  ros-humble-rosidl-generator-py
BuildRequires:  ros-humble-test-msgs
%endif

%description
Package containing the Python client.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Fri Jan 13 2023 Shane Loretz <sloretz@openrobotics.org> - 3.3.7-1
- Autogenerated by Bloom

* Tue Jan 10 2023 Shane Loretz <sloretz@openrobotics.org> - 3.3.6-1
- Autogenerated by Bloom

* Mon Nov 07 2022 Shane Loretz <sloretz@openrobotics.org> - 3.3.5-1
- Autogenerated by Bloom

* Tue May 17 2022 Shane Loretz <sloretz@openrobotics.org> - 3.3.4-1
- Autogenerated by Bloom

* Wed May 11 2022 Shane Loretz <sloretz@openrobotics.org> - 3.3.3-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Shane Loretz <sloretz@openrobotics.org> - 3.3.2-2
- Autogenerated by Bloom

* Fri Apr 08 2022 Shane Loretz <sloretz@openrobotics.org> - 3.3.2-1
- Autogenerated by Bloom

* Thu Mar 24 2022 Shane Loretz <sloretz@openrobotics.org> - 3.3.1-1
- Autogenerated by Bloom

* Tue Mar 01 2022 Shane Loretz <sloretz@openrobotics.org> - 3.3.0-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Shane Loretz <sloretz@openrobotics.org> - 3.2.1-2
- Autogenerated by Bloom

