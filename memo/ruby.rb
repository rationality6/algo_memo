class Calculator
  def initialize(left, right)
    @left = left
    @right = right
  end

  def sum
    @left + @right
  end
end

class User
  def initialize(right)
    @right = right
  end

  def my
    @right
  end
end

s = Calculator.new(1, 2)
puts s.sum

u = User.new(10_000)
puts u.my

nu = 1 / 2.0
nu01 = 1 / 4.0
puts nu * nu01
p 1 / 8.0
p 15 / 16.to_f
p 8**3
p 357 / 17

def mystery(n)
  return 1 if n <=0
  return mystery(n-1)
end

x = mystery(100)
p x

a = true
b = !a
c = (a && b) || (!a && !b)
p c
