require 'rubygems'
require 'nokogiri'

xsd = Nokogiri::XML::Schema(File.read('Flower.xsd'))
doc = Nokogiri::XML(File.read('Flower.xml'))

xsd.validate(doc).each do |error|
  puts error.message
end