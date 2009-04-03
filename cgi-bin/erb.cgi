#!/usr/bin/env ruby
# run ruby using the --debug flag for more descriptive errors

require "cgi"
require "erb"

# This cgi object is available in your RHTML files
cgi = CGI.new

# Optionally, enable using gems you've installed per http://forum.dreamhosters.com/programming/43221-gem-install-broken.htm#Post43228
ENV['GEM_PATH'] = "#{ENV['GEM_PATH']}:/home/YOUR_NAME/.gems"
# Optionally, require stuff here so you don't need to do this in each RHTML file
require "rubygems"

begin
path = nil
if (ENV['PATH_TRANSLATED'])
path = ENV['PATH_TRANSLATED']
else
file_path = ENV['REDIRECT_URL'].include?(File.basename(__FILE__)) ? ENV['SCRIPT_URL'] : ENV['REDIRECT_URL']
path = File.expand_path(ENV['DOCUMENT_ROOT'] + '/' + file_path)
raise "Attempt to access invalid path: #{path}" unless path.index(ENV['DOCUMENT_ROOT']) == 0
end

# So that working directory is not here but where the .rhtml is:
Dir.chdir(File.dirname(path))

  erb = File.open(path) { |f| ERB.new(f.read) }
print cgi.header + erb.result(binding)

  rescue Exception

  print "Content-Type: text/html\n\n"  
  if $DEBUG
# print out more descriptive errors while debugging
  print "<h1>Script Error</h1>"
  print "<pre>#{ $! }</pre>"
  print "<h2>Backtrace</h2>"
  print "<pre>#{$!.backtrace.join("\n")}</pre>"
  print "<h2>Environment</h2>"
  print "<pre>#{ENV.keys.map { |key| key + ' = ' + ENV[key] + "\n"} }</pre>"
  else 
  print "<h1>ERB error</h1><p>#{ $! }</p>"
  end

  end

