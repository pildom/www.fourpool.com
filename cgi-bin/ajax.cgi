#!/usr/bin/env ruby

require "cgi"

cgi = CGI.new("html4")
cgi.out { Time.now.to_s }
