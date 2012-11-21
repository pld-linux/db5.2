#
# Conditional build:
%bcond_without	java		# don't build Java bindings
%bcond_without	tcl		# don't build Tcl bindings
%bcond_without	static_libs	# don't build static libraries
%bcond_with	sqlite3		# build Sqlite3 API libraries
%bcond_with	default_db	# use this db as default system db

%include	/usr/lib/rpm/macros.java

%define		major		5
%define		libver		%{major}.2
%define		ver		%{libver}.36
%define		patchlevel	0
Summary:	Berkeley DB database library for C
Summary(pl.UTF-8):	Biblioteka C do obsługi baz Berkeley DB
Name:		db5.2
Version:	%{ver}.%{patchlevel}
Release:	1
License:	BSD-like (see LICENSE)
Group:		Libraries
#Source0Download: http://www.oracle.com/technetwork/database/berkeleydb/downloads/index-082944.html
Source0:	http://download.oracle.com/berkeley-db/db-%{ver}.tar.gz
# Source0-md5:	88466dd6c13d5d8cddb406be8a1d4d92
URL:		http://www.oracle.com/technetwork/database/berkeleydb/downloads/index.html
BuildRequires:	automake
%if %{with java}
BuildRequires:	jdk
BuildRequires:	rpm-javaprov
%endif
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.426
BuildRequires:	sed >= 4.0
%{?with_tcl:BuildRequires:	tcl-devel >= 8.4.0}
Requires:	uname(release) >= 2.6.0
%if %{with default_db}
Provides:	db = %{version}-%{release}
Provides:	db = %{libver}
Obsoletes:	db4
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{without default_db}
%define		_includedir	%{_prefix}/include/db%{libver}
%endif

%description
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB is used by many applications,
including Python and Perl, so this should be installed on all systems.

%description -l pl.UTF-8
Berkeley Database (Berkeley DB) to zestaw narzędzi programistycznych
zapewniających obsługę baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley db jest używana w wielu aplikacjach, w tym w
Pythonie i Perlu.

%package devel
Summary:	Header files for Berkeley database library
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki Berkeley Database
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%if %{with default_db}
Provides:	db-devel = %{version}-%{release}
Obsoletes:	db-devel
Obsoletes:	db3-devel
Obsoletes:	db4-devel
%endif

%description devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains the header files, libraries, and documentation
for building programs which use Berkeley DB.

%description devel -l pl.UTF-8
Berkeley Database (Berkeley DB) to zestaw narzędzi programistycznych
zapewniających obsługę baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obsługuje dostęp do bazy przez B-drzewa i
funkcje mieszające ze stałą lub zmienną wielkością rekordu,
transakcje, kroniki, pamięć dzieloną i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera pliki nagłówkowe i dokumentację do budowania
programów używających Berkeley DB.

%package static
Summary:	Static libraries for Berkeley database library
Summary(pl.UTF-8):	Statyczne biblioteki Berkeley Database
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
%if %{with default_db}
Provides:	db-static = %{version}-%{release}
Obsoletes:	db-static
Obsoletes:	db3-static
Obsoletes:	db4-static
%endif

%description static
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains the static libraries for building programs which
use Berkeley DB.

%description static -l pl.UTF-8
Berkeley Database (Berkeley DB) to zestaw narzędzi programistycznych
zapewniających obsługę baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obsługuje dostęp do bazy przez B-drzewa i
funkcje mieszające ze stałą lub zmienną wielkością rekordu,
transakcje, kroniki, pamięć dzieloną i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera statyczne biblioteki do budowania programów
używających Berkeley DB.

%package cxx
Summary:	Berkeley database library for C++
Summary(pl.UTF-8):	Biblioteka baz danych Berkeley dla C++
Group:		Libraries
%if %{with default_db}
Provides:	db-cxx = %{version}-%{release}
Obsoletes:	db4-cxx
%endif

%description cxx
Berkeley database library for C++.

%description cxx -l pl.UTF-8
Biblioteka baz danych Berkeley dla C++.

%package cxx-devel
Summary:	Header files for db-cxx library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki db-cxx
Group:		Development/Libraries
Requires:	%{name}-cxx = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%if %{with default_db}
Provides:	db-cxx-devel = %{version}-%{release}
Obsoletes:	db-cxx-devel
%endif
Conflicts:	db-devel < 4.1.25-3

%description cxx-devel
Header files for db-cxx library.

%description cxx-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki db-cxx.

%package cxx-static
Summary:	Static version of db-cxx library
Summary(pl.UTF-8):	Statyczna wersja biblioteki db-cxx
Group:		Development/Libraries
Requires:	%{name}-cxx-devel = %{version}-%{release}
%if %{with default_db}
Provides:	db-cxx-static = %{version}-%{release}
Obsoletes:	db-cxx-static
%endif
Conflicts:	db-static < 4.2.50-1

%description cxx-static
Static version of db-cxx library.

%description cxx-static -l pl.UTF-8
Statyczna wersja biblioteki db-cxx.

%package java
Summary:	Berkeley database library for Java
Summary(pl.UTF-8):	Biblioteka baz danych Berkeley dla Javy
Group:		Libraries
Requires:	jpackage-utils
%if %{with default_db}
Provides:	db-java = %{version}-%{release}
Obsoletes:	db-java
%endif

%description java
Berkeley database library for Java.

%description java -l pl.UTF-8
Biblioteka baz danych Berkeley dla Javy.

%package java-devel
Summary:	Development files for db-java library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki db-java
Group:		Development/Languages/Java
Requires:	%{name}-java = %{version}-%{release}
%if %{with default_db}
Provides:	db-java-devel = %{version}-%{release}
Obsoletes:	db-java-devel
%endif
Conflicts:	db-devel < 4.1.25-3

%description java-devel
Development files for db-java library.

%description java-devel -l pl.UTF-8
Pliki programistyczne biblioteki db-java.

%package tcl
Summary:	Berkeley database library for Tcl
Summary(pl.UTF-8):	Biblioteka baz danych Berkeley dla Tcl
Group:		Development/Languages/Tcl
Requires:	tcl
%if %{with default_db}
Provides:	db-tcl = %{version}-%{release}
Obsoletes:	db4-tcl
%endif

%description tcl
Berkeley database library for Tcl.

%description tcl -l pl.UTF-8
Biblioteka baz danych Berkeley dla Tcl.

%package tcl-devel
Summary:	Development files for db-tcl library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki db-tcl
Group:		Development/Languages/Tcl
Requires:	%{name}-tcl = %{version}-%{release}
%if %{with default_db}
Provides:	db-tcl-devel = %{version}-%{release}
Obsoletes:	db-tcl-devel
%endif
Conflicts:	db-devel < 4.1.25-3

%description tcl-devel
Development files for db-tcl library.

%description tcl-devel -l pl.UTF-8
Pliki programistyczne biblioteki db-tcl.

%package sql
Summary:	SQL layer for Berkeley database library
Summary(pl.UTF-8):	Wartstwa SQL dla biblioteki baz danych Berkeley
Group:		Libraries
%if %{with default_bd}
Provides:	db-sql = %{version}-%{release}
%endif

%description sql
SQL layer for Berkeley database library.

%description sql -l pl.UTF-8
Warstwa SQL dla biblioteki baz danych Berkeley.

%package sql-devel
Summary:	Development files for db-sql library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki db-sql
Group:		Development/Libraries
Requires:	%{name}-sql = %{version}-%{release}
%if %{with default_bd}
Provides:	db-sql-devel = %{version}-%{release}
Obsoletes:	db-sql-devel
%endif

%description sql-devel
Development files for db-sql library.

%description sql-devel -l pl.UTF-8
Pliki programistyczne biblioteki db-sql.

%package stl
Summary:	STL API for Berkeley Database library
Summary(pl.UTF-8):	API STL dla biblioteki Berkeley Database
Group:		Libraries
%if %{with default_db}
Provides:	db-stl = %{version}-%{release}
%endif

%description stl
STL API for Berkeley database library.

%description stl -l pl.UTF-8
API STL dla biblioteki Berkeley Database.

%package stl-devel
Summary:	Development files for db-stl library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki db-stl
Group:		Development/Libraries
Requires:	%{name}-stl = %{version}-%{release}
%if %{with default_db}
Provides:	db-stl-devel = %{version}-%{release}
Obsoletes:	db-stl-devel
%endif

%description stl-devel
Development files for db-stl library.

%description stl-devel -l pl.UTF-8
Pliki programistyczne biblioteki db-stl.

%package sqlite3
Summary:	Sqlite3 API for Berkeley Database library
Summary(pl.UTF-8):	API Sqlite3 dla biblioteki Berkeley Database
Group:		Libraries
%if %{with default_db}
Provides:	db-sqlite3 = %{version}-%{release}
%endif

%description sqlite3
Sqlite3 API for Berkeley database library.

%description sqlite3 -l pl.UTF-8
API Sqlite3 dla biblioteki Berkeley Database.

%package sqlite3-devel
Summary:	Development files for db-sqlite3 library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki db-sqlite3
Group:		Development/Libraries
Requires:	%{name}-sqlite3 = %{version}-%{release}
%if %{with default_db}
Provides:	db-sqlite3-devel = %{version}-%{release}
Obsoletes:	db-sqlite3-devel
%endif

%description sqlite3-devel
Development files for db-sqlite3 library.

%description sqlite3-devel -l pl.UTF-8
Pliki programistyczne biblioteki db-sqlite3.

%package utils
Summary:	Command line tools for managing Berkeley DB databases
Summary(pl.UTF-8):	Narzędzia do obsługi baz Berkeley DB z linii poleceń
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-sql = %{version}-%{release}
%if %{with default_db}
Provides:	db-utils = %{version}-%{release}
Obsoletes:	db-utils
Obsoletes:	db3-utils
Obsoletes:	db4-utils
%endif

%description utils
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains command line tools for managing Berkeley DB
databases.

%description utils -l pl.UTF-8
Berkeley Database (Berkeley DB) to zestaw narzędzi programistycznych
zapewniających obsługę baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obsługuje dostęp do bazy przez B-drzewa i
funkcje mieszające ze stałą lub zmienną wielkością rekordu,
transakcje, kroniki, pamięć dzieloną i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera narzędzia do obsługi baz Berkeley DB z linii
poleceń.

%prep
%setup -q -n db-%{ver}

%build
cp -f /usr/share/automake/config.sub dist

JAVACFLAGS="-source 1.5 -target 1.5"
export JAVACFLAGS

%if %{with static_libs}
cp -a build_unix build_unix.static

cd build_unix.static

CC="%{__cc}"
CXX="%{__cxx}"
CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags} -fno-implicit-templates"
LDFLAGS="%{rpmcflags} %{rpmldflags}"
export CC CXX CFLAGS CXXFLAGS LDFLAGS

../dist/%configure \
	--disable-shared \
	--enable-static \
	--enable-compat185 \
	--enable-cxx \
	--enable-dbm \
	--enable-build_dbm \
	--enable-posixmutexes

# (temporarily?) disabled because of compilation errors:
#	--enable-dump185 \

%{__make} library_build
cd ..
%endif

cd build_unix

../dist/%configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--enable-shared \
	--disable-static \
	--enable-compat185 \
	--enable-cxx \
	--enable-dbm \
	--enable-build_dbm \
	--enable-posixmutexes \
	--enable-sql \
	%{?with_sqlite3:--enable-sql_compat} \
	--enable-sql_codegen \
	--enable-stl \
	%{?with_java:--enable-java} \
	%{?with_tcl:--enable-tcl --with-tcl=/usr/lib}

%{__make} library_build \
	TCFLAGS='-I$(builddir) -I%{_includedir}' \
	LIBSO_LIBS="\$(LIBS)" \
	LIBTSO_LIBS="\$(LIBS) -ltcl"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_bindir}}
%if %{with java}
install -d $RPM_BUILD_ROOT%{_javadir}
%endif

%if %{with static_libs}
%{__make} -C build_unix.static library_install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/db-%{version}-docs \
	includedir=%{_includedir}
%endif

%{__make} -C build_unix library_install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIB_INSTALL_FILE_LIST="" \
	docdir=%{_docdir}/db-%{version}-docs \
	includedir=%{_includedir}

%if %{with default_db}
install -d $RPM_BUILD_ROOT/%{_lib}
mv $RPM_BUILD_ROOT%{_libdir}/libdb-%{libver}.so $RPM_BUILD_ROOT/%{_lib}
%endif

cd $RPM_BUILD_ROOT%{_libdir}
%if %{with static_libs}
mv -f libdb.a libdb-%{libver}.a
mv -f libdb_cxx.a libdb_cxx-%{libver}.a
%endif
%if %{with java}
mv -f $RPM_BUILD_ROOT%{_libdir}/db.jar $RPM_BUILD_ROOT%{_javadir}/db-%{libver}.jar
%endif
%if %{with default_db}
ln -sf /%{_lib}/libdb-%{libver}.so libdb.so
ln -sf /%{_lib}/libdb-%{libver}.so libdb-%{libver}.so
ln -sf /%{_lib}/libdb-%{libver}.so libndbm.so
ln -sf libdb-%{libver}.la libdb.la
ln -sf libdb-%{libver}.la libndbm.la
ln -sf libdb_cxx-%{libver}.so libdb_cxx.so
ln -sf libdb_cxx-%{libver}.la libdb_cxx.la
%if %{with java}
ln -sf libdb_java-%{libver}.la libdb_java.la
ln -sf db-%{libver}.jar $RPM_BUILD_ROOT%{_javadir}/db.jar
%endif
%if %{with tcl}
ln -sf libdb_tcl-%{libver}.so libdb_tcl.so
ln -sf libdb_tcl-%{libver}.la libdb_tcl.la
%endif
%if %{with static_libs}
ln -sf libdb-%{libver}.a libdb.a
ln -sf libdb-%{libver}.a libndbm.a
ln -sf libdb_cxx-%{libver}.a libdb_cxx.a
%endif
%endif

sed -i "s/old_library=''/old_library='libdb-%{libver}.a'/" libdb-%{libver}.la
sed -i "s/old_library=''/old_library='libdb_cxx-%{libver}.a'/" libdb_cxx-%{libver}.la

cd -

cd $RPM_BUILD_ROOT%{_bindir}
mv dbsql dbsql-%{libver}
%{?with_default_db:ln -sf dbsql-%{libver} dbsql}
for F in db_*; do
  Fver=$(echo $F|sed 's/db_/db%{libver}_/')
  mv $F $Fver
  %{?with_default_db:ln -sf $Fver $F}
done
cd -

install -d $RPM_BUILD_ROOT%{_examplesdir}/db-%{version}
cp -a examples/c/* $RPM_BUILD_ROOT%{_examplesdir}/db-%{version}

install -d $RPM_BUILD_ROOT%{_examplesdir}/db-cxx-%{version}
cp -a examples/cxx/* $RPM_BUILD_ROOT%{_examplesdir}/db-cxx-%{version}

%if %{with java}
install -d $RPM_BUILD_ROOT%{_examplesdir}/db-java-%{version}
cp -a examples/java/* $RPM_BUILD_ROOT%{_examplesdir}/db-java-%{version}
%endif

# in %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/db-%{version}-docs/{index.html,license/license_db.html}

# don't have csharp subpackages yet
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/db-%{version}-docs/csharp

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	tcl -p /sbin/ldconfig
%postun	tcl -p /sbin/ldconfig

%post	cxx -p /sbin/ldconfig
%postun	cxx -p /sbin/ldconfig

%post	sql -p /sbin/ldconfig
%postun	sql -p /sbin/ldconfig

%post	stl -p /sbin/ldconfig
%postun	stl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README docs/index.html docs/license
%if %{with default_db}
%attr(755,root,root) /%{_lib}/libdb-%{libver}.so
%else
%attr(755,root,root) %{_libdir}/libdb-%{libver}.so
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/db%{libver}_sql_codegen
%{_libdir}/libdb-%{libver}.la
%if %{with default_db}
%attr(755,root,root) %{_bindir}/db_sql_codegen
%attr(755,root,root) %{_libdir}/libdb-%{libver}.so
%attr(755,root,root) %{_libdir}/libdb-%{major}.so
%attr(755,root,root) %{_libdir}/libdb.so
%attr(755,root,root) %{_libdir}/libndbm.so
%{_libdir}/libdb.la
%{_libdir}/libndbm.la
%else
%dir %{_includedir}
%endif
%{_includedir}/db.h
%{_includedir}/db_185.h
%dir %{_docdir}/db-%{version}-docs
%dir %{_docdir}/db-%{version}-docs/api_reference
%{_docdir}/db-%{version}-docs/api_reference/C
%{_docdir}/db-%{version}-docs/articles
%dir %{_docdir}/db-%{version}-docs/gsg
%{_docdir}/db-%{version}-docs/gsg/C
%dir %{_docdir}/db-%{version}-docs/gsg_txn
%{_docdir}/db-%{version}-docs/gsg_txn/C
%dir %{_docdir}/db-%{version}-docs/gsg_db_rep
%{_docdir}/db-%{version}-docs/gsg_db_rep/C
%{_docdir}/db-%{version}-docs/installation
%{_docdir}/db-%{version}-docs/porting
%{_docdir}/db-%{version}-docs/programmer_reference
%{_docdir}/db-%{version}-docs/upgrading
%{_examplesdir}/db-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdb-%{libver}.a
%if %{with default_db}
%{_libdir}/libdb.a
%{_libdir}/libndbm.a
%endif
%endif

%files cxx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_cxx-%{libver}.so

%files cxx-devel
%defattr(644,root,root,755)
%{_libdir}/libdb_cxx-%{libver}.la
%if %{with default_db}
%attr(755,root,root) %{_libdir}/libdb_cxx-%{major}.so
%attr(755,root,root) %{_libdir}/libdb_cxx.so
%{_libdir}/libdb_cxx.la
%endif
%{_includedir}/db_cxx.h
%{_docdir}/db-%{version}-docs/api_reference/CXX
%{_docdir}/db-%{version}-docs/api_reference/STL
%{_docdir}/db-%{version}-docs/gsg/CXX
%{_docdir}/db-%{version}-docs/gsg_txn/CXX
%{_docdir}/db-%{version}-docs/gsg_db_rep/CXX
%{_examplesdir}/db-cxx-%{version}

%if %{with static_libs}
%files cxx-static
%defattr(644,root,root,755)
%{_libdir}/libdb_cxx-%{libver}.a
%if %{with default_db}
%{_libdir}/libdb_cxx.a
%endif
%endif

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_java-%{libver}.so
%attr(755,root,root) %{_libdir}/libdb_java-%{libver}_g.so
%{_javadir}/db-%{libver}.jar
%if %{with default_db}
%{_javadir}/db.jar
%endif

%files java-devel
%defattr(644,root,root,755)
%{_libdir}/libdb_java-%{libver}.la
%if %{with default_db}
%attr(755,root,root) %{_libdir}/libdb_java.so
%attr(755,root,root) %{_libdir}/libdb_java-%{major}.so
%{_libdir}/libdb_java.la
%endif
%{_docdir}/db-%{version}-docs/collections
%{_docdir}/db-%{version}-docs/gsg/JAVA
%{_docdir}/db-%{version}-docs/gsg_txn/JAVA
%{_docdir}/db-%{version}-docs/gsg_db_rep/JAVA
%{_docdir}/db-%{version}-docs/java
%{_examplesdir}/db-java-%{version}
%endif

%if %{with tcl}
%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_tcl-%{libver}.so

%files tcl-devel
%defattr(644,root,root,755)
%{_libdir}/libdb_tcl-%{libver}.la
%if %{with default_db}
%attr(755,root,root) %{_libdir}/libdb_tcl.so
%attr(755,root,root) %{_libdir}/libdb_tcl-%{major}.so
%{_libdir}/libdb_tcl.la
%endif
%{_docdir}/db-%{version}-docs/api_reference/TCL
%endif

%files sql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_sql-%{libver}.so

%files sql-devel
%defattr(644,root,root,755)
%{_libdir}/libdb_sql-%{libver}.la
%if %{with default_db}
%attr(755,root,root) %{_libdir}/libdb_sql.so
%attr(755,root,root) %{_libdir}/libdb_sql-%{major}.so
%endif
%{_includedir}/dbsql.h
%{_docdir}/db-%{version}-docs/bdb-sql

%files stl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_stl-%{libver}.so

%files stl-devel
%defattr(644,root,root,755)
%{_libdir}/libdb_stl-%{libver}.la
%if %{with default_db}
%attr(755,root,root) %{_libdir}/libdb_stl.so
%attr(755,root,root) %{_libdir}/libdb_stl-%{major}.so
%endif
%{_includedir}/dbstl_base_iterator.h
%{_includedir}/dbstl_common.h
%{_includedir}/dbstl_container.h
%{_includedir}/dbstl_dbc.h
%{_includedir}/dbstl_dbt.h
%{_includedir}/dbstl_element_ref.h
%{_includedir}/dbstl_exception.h
%{_includedir}/dbstl_inner_utility.h
%{_includedir}/dbstl_map.h
%{_includedir}/dbstl_resource_manager.h
%{_includedir}/dbstl_set.h
%{_includedir}/dbstl_utility.h
%{_includedir}/dbstl_vector.h

%if %{with sqlite3}
%files sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sqlite3
%attr(755,root,root) %{_libdir}/libsqlite3.so

%files sqlite3-devel
%defattr(644,root,root,755)
%{_libdir}/libsqlite3.la
%{_includedir}/sqlite3.h
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/db%{libver}_archive
%attr(755,root,root) %{_bindir}/db%{libver}_checkpoint
%attr(755,root,root) %{_bindir}/db%{libver}_deadlock
%attr(755,root,root) %{_bindir}/db%{libver}_dump
%attr(755,root,root) %{_bindir}/db%{libver}_hotbackup
%attr(755,root,root) %{_bindir}/db%{libver}_load
%attr(755,root,root) %{_bindir}/db%{libver}_log_verify
%attr(755,root,root) %{_bindir}/db%{libver}_printlog
%attr(755,root,root) %{_bindir}/db%{libver}_recover
%attr(755,root,root) %{_bindir}/db%{libver}_replicate
%attr(755,root,root) %{_bindir}/db%{libver}_stat
%attr(755,root,root) %{_bindir}/db%{libver}_tuner
%attr(755,root,root) %{_bindir}/db%{libver}_upgrade
%attr(755,root,root) %{_bindir}/db%{libver}_verify
%attr(755,root,root) %{_bindir}/dbsql-%{libver}
%if %{with default_db}
%attr(755,root,root) %{_bindir}/db_archive
%attr(755,root,root) %{_bindir}/db_checkpoint
%attr(755,root,root) %{_bindir}/db_deadlock
%attr(755,root,root) %{_bindir}/db_dump
%attr(755,root,root) %{_bindir}/db_hotbackup
%attr(755,root,root) %{_bindir}/db_load
%attr(755,root,root) %{_bindir}/db_log_verify
%attr(755,root,root) %{_bindir}/db_printlog
%attr(755,root,root) %{_bindir}/db_recover
%attr(755,root,root) %{_bindir}/db_replicate
%attr(755,root,root) %{_bindir}/db_stat
%attr(755,root,root) %{_bindir}/db_tuner
%attr(755,root,root) %{_bindir}/db_upgrade
%attr(755,root,root) %{_bindir}/db_verify
%attr(755,root,root) %{_bindir}/dbsql
%endif
