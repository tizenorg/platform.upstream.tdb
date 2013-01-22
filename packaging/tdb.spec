Name:           tdb
Version:        1.2.10
Release:        0
Summary:        Samba Trivial Database
License:        GPLv3.0+
Group:          System/Libraries
Url:            http://tdb.samba.org/
Source:         http://www.samba.org/ftp/tdb/tdb-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(python)

%description
TDB is a Trivial Database. In concept, it is very much like GDBM, and BSD's DB
except that it allows multiple simultaneous writers and uses locking
internally to keep writers from trampling on each other. TDB is also extremely
small.

%package -n libtdb
Summary:        Libraries and Header Files to Develop Programs with tdb Support
Group:          System/Libraries
Requires:       pkg-config
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

%description -n libtdb
TDB is a Trivial Database. In concept, it is very much like GDBM, and BSD's DB
except that it allows multiple simultaneous writers and uses locking
internally to keep writers from trampling on each other. TDB is also extremely
small.

This package contains the tdb library.
%package -n libtdb-devel
Summary:        Libraries and Header Files to Develop Programs with tdb Support
Group:          Development/Libraries/C and C++
Requires:       libtdb = %{version}
Requires:       pkg-config

%description -n libtdb-devel
TDB is a Trivial Database. In concept, it is very much like GDBM, and BSD's DB
except that it allows multiple simultaneous writers and uses locking
internally to keep writers from trampling on each other. TDB is also extremely
small.

This package contains libraries and header files need for development.

%package tools
Summary:        Tools to manipulate tdb files
Group:          Development/Libraries/C and C++

%description tools
TDB is a Trivial Database. In concept, it is very much like GDBM, and BSD's DB
except that it allows multiple simultaneous writers and uses locking
internally to keep writers from trampling on each other. TDB is also extremely
small.

This package contains tools to manage Tdb files.

%package -n python-tdb
Summary:        Python bindings to Develop Programs with tdb Support

%description -n python-tdb
TDB is a Trivial Database. In concept, it is very much like GDBM, and BSD's DB
except that it allows multiple simultaneous writers and uses locking
internally to keep writers from trampling on each other. TDB is also extremely
small.

This package contains python language support.



%prep
%setup -n tdb-%{version} -q

%build
%configure 
#--disable-python

%{__make} %{?jobs:-j%jobs}

%install
%make_install


%post -n libtdb -p /sbin/ldconfig

%postun -n libtdb -p /sbin/ldconfig

%files -n libtdb
%defattr(-,root,root)
%{_libdir}/libtdb.so.*

%files -n libtdb-devel
%defattr(-,root,root)
%{_includedir}/tdb.h
%{_libdir}/libtdb.so
%{_libdir}/pkgconfig/tdb.pc

%files tools
%defattr(-,root,root)
%{_bindir}/tdbbackup
%{_bindir}/tdbdump
%{_bindir}/tdbrestore
%{_bindir}/tdbtool

%files -n python-tdb
%defattr(-,root,root)
%{python_sitearch}/tdb.so
