#!/usr/bin/env ruby

require "cgi"

cgi = CGI.new("html4")
s = cgi["s"]
r = cgi["r"]

m = s.match(Regexp.new(r))

  cgi.out {
    CGI.pretty(
      cgi.html {
        cgi.head {
          cgi.title("RE") { "Regular Expressions Online" } +
          "<link rel=\"stylesheet\" type=\"text/css\" href=\"../css/regexp.css\">"
        } +
        cgi.body {
          cgi.div({"id"=>"wrapper"}) {
            cgi.div({"id"=>"header"}) {
             # cgi.img("../img/regexp_owl.gif") +
             # cgi.span("id"=>"orly") {"orly?"} +
              cgi.h1 { "Try Regular Expressions" }
            } +
            cgi.div({"id"=>"content"}) {
              cgi.form {
                cgi.p({"class"=>"textfield_name"}) { "String" } +
                cgi.textarea({"name"=>"s", "value"=>s, "cols"=>"80", "rows"=>"20"}) +
                cgi.p({"class"=>"textfield_name"}) { "Regular Expression" } +
                cgi.text_field({"name"=>"r", "value"=>r, "size"=>"40"}) +
                cgi.submit({"value"=>"do it"})
              } +
              cgi.div({"id"=>"formatted_string"}) {
                cgi.p { "=> " + 
                  if m == nil
                    "no match found"
                  else
                    m.pre_match +
                    cgi.span({"id"=>"regexp_text"}) { m.to_s } +
                    m.post_match
                  end
                }
              }
            }
          }
        }
      }
    )
  }
