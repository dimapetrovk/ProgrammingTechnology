require "sax-machine"
require "rspec"

class Flower
  include SAXMachine
  element :flowerID
  element :name
  element :soil
  element :origin
  element :visualParameters
  element :growingTips
  element :multiplying

  def to_s
    @flowerID + " " + @name + " " + @multiplying
  end
end

text = File.read("Flower.xml")

class Wikihandler
  include SAXMachine
  elements :flower, :as => :flowers , :class => Flower
end

parser = Wikihandler.new
parser.parse text

sorted = parser.flowers.sort_by {|obj| obj.multiplying.to_s}
sorted.each {|flower|
  puts flower
}