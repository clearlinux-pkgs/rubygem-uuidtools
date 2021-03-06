#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-uuidtools
Version  : 2.1.5
Release  : 4
URL      : https://rubygems.org/downloads/uuidtools-2.1.5.gem
Source0  : https://rubygems.org/downloads/uuidtools-2.1.5.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : ruby
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-launchy
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-yard

%description
# UUIDTools
<dl>
<dt>Homepage</dt><dd><a href="https://github.com/sporkmonger/uuidtools">sporkmonger/uuidtools</a></dd>
<dt>Author</dt><dd><a href="mailto:bob@sporkmonger.com">Bob Aman</a></dd>
<dt>License</dt><dd>Apache 2.0</dd>
</dl>

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n uuidtools-2.1.5
gem spec %{SOURCE0} -l --ruby > rubygem-uuidtools.gemspec

%build
gem build rubygem-uuidtools.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
uuidtools-2.1.5.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/uuidtools-2.1.5
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/uuidtools-2.1.5.gem
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/CHANGELOG
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/README.md
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/lib/compat/securerandom.rb
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/lib/uuidtools.rb
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/lib/uuidtools/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/spec/spec.opts
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/spec/uuidtools/mac_address_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/spec/uuidtools/utility_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/spec/uuidtools/uuid_creation_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/spec/uuidtools/uuid_parsing_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/tasks/benchmark.rake
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/tasks/gem.rake
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/tasks/git.rake
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/tasks/metrics.rake
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/tasks/rspec.rake
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/tasks/yard.rake
/usr/lib64/ruby/gems/2.3.0/gems/uuidtools-2.1.5/website/index.html
/usr/lib64/ruby/gems/2.3.0/specifications/uuidtools-2.1.5.gemspec
