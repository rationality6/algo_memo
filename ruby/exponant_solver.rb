def solver(linear_value, line_add, exponential_value, expo_times)
  count = 1
  while exponential_value < linear_value
    linear_value += line_add
    p linear_value
    exponential_value *= expo_times
    p exponential_value
    count += 1
    p count
  end
  return count
end

p solver(40, 60, 20, 1.8)



for i in "babdc".split("").sort() do
  puts i
end


sorted_input = "babdc".split('').sort().join('')

p sorted_input.chars.group_by(&:chr)

.map { |k, v| "#{k}#{v.size}" } .join('')

def adder(i)
  if i<0
    return 0
  else
    return i += adder(i-1)
  end
end
p adder(10)

result = 0
for i in 0..10 do
  result += i
end
p result
