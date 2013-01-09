Name:           tdb
Version:        1.2.10
Release:        0
Summary:        Samba Trivial Database
License:        GPL-3.0+
Group:          System/Libraries
Url:            http://tdb.samba.org/

Source:         http://www.samba.org/ftp/tdb/tdb-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  pkg-config
BuildRequires:  python-devel

%define libtdb_name libtdb1

%description
TDB is a Trivial Database. In concept, it is very much like GDBM, and BSD's DB
except that it allows multiple simultaneous writers and uses locking
internally to keep writers from trampling on each other. TDB is also extremely
small.

%prep
%setup -n tdb-%{version} -q

%build
%configure --disable-python
%{__make} %{?jobs:-j%jobs}

%install
%make_install

%package -n %{libtdb_name}
Summary:        Libraries and Header Files to Develop Programs with tdb1 Support
Group:          System/Libraries
Requires:       pkg-config
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

%description -n %{libtdb_name}
TDB is a Trivial Database. In concept, it is very much like GDBM, and BSD's DB
except that it allows multiple simultaneous writers and uses locking
internally to keep writers from trampling on each other. TDB is also extremely
small.

This package contains the tdb1 library.

%post -n %{libtdb_name} -p /sbin/ldconfig

%postun -n %{libtdb_name} -p /sbin/ldconfig

%files -n %{libtdb_name}
%defattr(-,root,root)
%{_libdir}/libtdb.so.*


%package -n libtdb-devel
Summary:        Libraries and Header Files to Develop Programs with tdb1 Support
Group:          Development/Libraries/C and C++
Requires:       %{libtdb_name} = %{version}
Requires:       pkg-config

%description -n libtdb-devel
TDB is a Trivial Database. In concept, it is very much like GDBM, and BSD's DB
except that it allows multiple simultaneous writers and uses locking
internally to keep writers from trampling on each other. TDB is also extremely
small.

This package contains libraries and header files need for development.

%files -n libtdb-devel
%defattr(-,root,root)
%{_includedir}/tdb.h
%{_libdir}/libtdb.so
%{_libdir}/pkgconfig/tdb.pc

%package -n tdb-tools
Summary:        Tools to manipulate tdb files
Group:          Development/Libraries/C and C++

%description -n tdb-tools
TDB is a Trivial Database. In concept, it is very much like GDBM, and BSD's DB
except that it allows multiple simultaneous writers and uses locking
internally to keep writers from trampling on each other. TDB is also extremely
small.

This package contains tools to manage Tdb files.

%files -n tdb-tools
%defattr(-,root,root)
%{_bindir}/tdbbackup
%{_bindir}/tdbdump
%{_bindir}/tdbrestore
%{_bindir}/tdbtool


