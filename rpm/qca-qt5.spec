# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26~git
# 

Name:       qca-qt5

# >> macros
# << macros

Summary:    Qt Cryptographic Architecture
Version:    2.0.3
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        http://quickgit.kde.org/?p=qca.git
Source0:    %{name}-%{version}.tar.gz
Source100:  qca-qt5.yaml
Requires:   ca-certificates
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  ca-certificates
BuildRequires:  cmake

%description
The Qt Cryptographic Architecture (QCA) provides a straightforward and cross-
platform API for a range of cryptographic features, including SSL/TLS,
X.509 certificates, SASL, OpenPGP, S/MIME CMS, and smart cards.


%package devel
Summary:    Qt Cryptographic Architecture - development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The Qt Cryptographic Architecture (QCA) provides a straightforward and cross-
platform API for a range of cryptographic features, including SSL/TLS,
X.509 certificates, SASL, OpenPGP, S/MIME CMS, and smart cards.

This package contains development files for building software that uses the
Qt Cryptographic Architecture.


%prep
%setup -q -n %{name}-%{version}/qca

# >> setup
# << setup

%build
# >> build pre
%cmake -D BUILD_TESTS:BOOL=OFF -D QCA_INSTALL_IN_QT_PREFIX:BOOL=ON .
sed -i -e /strip/d Makefile
# << build pre


make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%doc COPYING README TODO
%{_bindir}/qcatool2-qt5
%{_libdir}/libqca-qt5.so.*
%{_libdir}/plugins/qca-qt5/*
%{_mandir}/*/*
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/qt5/QtCrypto
%{_libdir}/libqca-qt5.so
%{_libdir}/pkgconfig/qca2-qt5.pc
%{_datadir}/qt5/mkspecs/features/crypto.prf
# << files devel
