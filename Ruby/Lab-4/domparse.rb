require "happymapper"

XML_STRING = File.read("Flower.xml")

class Flower; end;              # fwd reference

class Flowers
  include HappyMapper
  tag 'flowers'

  attribute :xmlns, String
  has_many :flowers, Flower, :tag => 'flower'
end

class Flower
  include HappyMapper
  tag 'flower'

  element :flowerID, Integer
  element :name, String
  element :soil, String
  element :origin, String
  element :visualParameters, String
  element :growingTips, String
  element :multiplying, String

  def to_s
    @flowerID.to_s + " " + @name + " " + @multiplying
  end
end

def parseXML
  Flowers.parse(XML_STRING, :single => true)
end

parsed = parseXML
sorted = parsed.flowers.sort_by {|obj| obj.multiplying}
sorted.each {|flower|
  puts flower
}