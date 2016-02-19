class Utils
	def self.trim_all(arr_strings)
		return arr_strings.collect{|x| x.strip || x }
	end
	def self.filter_array(arr_words, filter)
		return arr_words.select{ |word| !word.include? filter }
	end
	def self.strip_wrapper(string, wrapper)
		return string.tr(wrapper, '')
	end
	def self.check_order(string, arr_words)
		if arr_words.length > 1
			aux_pos = 0
			for word in arr_words
				pos = string.index(word)
				if pos >= aux_pos
					aux_pos = pos
				else
					return false
				end
			end
		end
		return true
	end
	def self.is_logic_operator(char)
		char.downcase() == 'and' or char.downcase() == 'or'
	end
	def self.has_logic_operator(arr)
		arr.include? 'and' or arr.include? 'or' or arr.include? 'AND' or arr.include? 'OR'
	end
end

class Search < Utils
	def initialize()
		@query = {}
	end
	def self.iterate(query, str)
		query.gsub! '(', ''
		query.gsub! ')', ' )'
		inner_query = []
		for word in query.split(' ')
			if word != ')'
				if inner_query.length == 0
					inner_query.push(self.evaluate(word, str))
				else
					if !self.has_logic_operator(inner_query)
						inner_query = [inner_query.all?]
					else
						inner_query = [eval(inner_query.join(' ').downcase())]
					end
				end
			end
			if word == ')'
				print inner_query
				if !self.has_logic_operator(inner_query)
					inner_query = [inner_query.all?]
				else
					inner_query = [eval(inner_query.join(' ').downcase())]
				end
				next
			end
		end
		if !self.has_logic_operator(inner_query)
			return inner_query.all?
		else
			return eval(inner_query.join(' ').downcase())
		end
	end
	def self.new(query)
		@query = query
		self
	end
	def self.check_presence_AND(string, arr_words)
		return arr_words.all?{ |word| string.include? self.strip_wrapper(word, '"') }
	end
	def self.check_presence_OR(string, arr_words)
		return arr_words.any?{ |word| string.include? self.strip_wrapper(word, '"') }
	end
	def self.check_negation_presence(string, arr_words)
		filtered_array = self.filter_array(arr_words, '-')
		return filtered_array.any?{ |word| string.include? self.strip_wrapper(word, '"') }
	end
	def self.evaluate(query, str)
		if query.include? '-'
			all_words = self.trim_all(query.split(' ').delete_if(&:empty?) )
			@query[:words] = self.filter_array(all_words, '-')
			@query[:notwords] = self.filter_array(all_words, '')
			return !self.check_negation_presence(str, @query[:words])
		end
		if query.include? '*'
			@query[:words] = self.trim_all(query.split('*').delete_if(&:empty?) )
			#all substrings are in the string
			case1 = self.check_presence_AND(str, @query[:words])
			#all substrings are in the correct order if middle
			case2 = self.check_order(str, @query[:words])
			return (case1 and case2)
		end
		if self.is_logic_operator(query)
			return query
		end
		return str.include? self.strip_wrapper(query, '"')
	end
	def self.test(str)
		return self.iterate(@query[:query], str)
	end
end