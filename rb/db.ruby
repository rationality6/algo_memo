class Test
  def self.assert_equals(a, b)
    puts(a == b)
  end
end

def dBScale(i)
  10 * Math.log10(i / 10**-12)
end

puts(dBScale(10**9))

Test.assert_equals(dBScale(10**-9).round, 30)
Test.assert_equals(dBScale(10**-5).round, 70)
Test.assert_equals(dBScale(10).round, 130)
Test.assert_equals(dBScale(100).round, 140)
Test.assert_equals(dBScale(2.48794569 * 10**173).round, 1854)
