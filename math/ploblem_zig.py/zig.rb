# 문제
# "ab2v9bc13j5jf4jv21" => 9^2 + 13^2 + 5^2 + 21^2 = 716
# 찾을수있는 가능한 패턴
# 1.숫자를 추출한다
# 2.짝수를 제외한 숫자들을 제곱한뒤 더한다

class Test
  def self.assign_equal(left, right)
    left == right
  end
end

secret_string = 'ab2v9bc13j5jf4jv21'

def find_pattern(l)
  subset = l.gsub(/\D+/, ' ').split(' ')
  subset.each do |x|
    p(x.to_i**2) if x.to_i.odd?
  end
end

puts(Test.assign_equal(3, 3))
p(find_pattern(secret_string))
