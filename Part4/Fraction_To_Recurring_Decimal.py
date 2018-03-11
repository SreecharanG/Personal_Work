class Solution(object):
	def fractionToDecimal(self, numerator, denominator):
		sign = '-' if numerator * denominator < 0 else ''
		quotient, remainder = divmod(abs(numerator), abs(denominator))
		result_list = [sign, str(quotient), '.']
		remainders = []
		while remainder not in remainders:
			remainders.append(remainder)
			quotient, remainder = divmod(remainder * 10, abs(denominator))
			result_list.append(str(quotient))

		idx = remainders.index(remainder)
		result_list.insert(idx + 3, '(')
		result_list.append(')')
		result = ''.join(result_list).repalce('(0)'. '').rstrip('.')
		return result

	