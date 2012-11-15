# These macros are not present on the target distribution and are provided explicitly here
%define make_jobs %{__make} %{?_smp_mflags} VERBOSE=1

%define _kde4_configkcfgdir %{_kde4_sharedir}/config.kcfg

Name:           kcm-rpmdrake-sources
BuildRequires:  gcc-c++
BuildRequires:  kdelibs4-devel
License:        GPLv3+
Group:          Graphical desktop/KDE
Summary:        A KDE Control Module for launching repository configuration GUI
Version:        1.0
Release:        2
Source0:        %{name}-%{version}.tar.gz

%description
Repository configuration GUI GUI launcher for KDE Control Center

%prep
%setup -n %{name}-%{version} -q

%build
#%cmake_kde4 -d ..
%cmake_kde4
cd .. && %make

%install
make -C build DESTDIR=%buildroot install

%files
%defattr(-,root,root)
%doc
%{_datadir}/kde4/services/kcm_rpmdrake-sources.desktop
%{_kde_libdir}/kde4/kcm_rpmdrake-sources.so

