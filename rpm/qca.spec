# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26~git
# 

Name:       qca

# >> macros
# << macros

Summary:    Qt Cryptographic Architecture
Version:    2.0.3
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        http://quickgit.kde.org/?p=qca.git
Source0:    %{name}-%{version}.tar.gz
Source100:  qca.yaml
Requires:   ca-certificates
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(QtCore) < 5
BuildRequires:  pkgconfig(QtNetwork) < 5
BuildRequires:  pkgconfig(openssl)
BuildRequires:  ca-certificates
BuildRequires:  cmake
Obsoletes:   qca2 <= 2.0.3
Obsoletes:   qca-ossl

%description
The Qt Cryptographic Architecture (QCA) provides a straightforward and cross-
platform API for a range of cryptographic features, including SSL/TLS,
X.509 certificates, SASL, OpenPGP, S/MIME CMS, and smart cards.


%package devel
Summary:    Qt Cryptographic Architecture - development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Obsoletes:  qca2-devel <= 2.0.3

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
%{_libdir}/qt4/bin/qcatool2
%{_libdir}/libqca.so.*
%{_libdir}/qt4/plugins/qca/*
%{_datadir}/qt4/man/*/*
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/qt4/QtCrypto
%{_libdir}/libqca.so
%{_libdir}/pkgconfig/qca2.pc
%{_datadir}/qt4/mkspecs/features/crypto.prf
# << files devel
