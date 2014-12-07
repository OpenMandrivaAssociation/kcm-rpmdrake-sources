# These macros are not present on the target distribution and are provided explicitly here
%define make_jobs %{__make} %{?_smp_mflags} VERBOSE=1

Name:           kcm-rpmdrake-sources
BuildRequires:  kdelibs4-devel
License:        GPLv3+
Group:          Graphical desktop/KDE
Summary:        A KDE Control Module for launching repository configuration GUI
Version:        1.0
Release:        17
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz

%description
Repository configuration GUI GUI launcher for KDE Control Center

%prep
%setup -q

%build
%cmake_kde4

%install
%makeinstall_std -C build

#fix run programm
sed -e 's/edit-urpm-sources.pl/drakrpm-edit-media/' -i %{buildroot}%{_datadir}/kde4/services/kcm_rpmdrake-sources.desktop

%files
%defattr(-,root,root)
%doc
%{_datadir}/kde4/services/kcm_rpmdrake-sources.desktop

