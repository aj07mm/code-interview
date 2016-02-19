require './search.rb'

describe 'foobar' do
	it "is true if true" do
		expect(true).to eq(true)
	end

	# AND

	it "Search.new(query: 'bananas AND apples').test(str) #=> true" do
		str = "I really like bananas, apples not so much"
		query = 'bananas AND apples'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	it "Search.new(query: 'bananas AND apples AND oranges').test(str) #=> true" do
		str = "I really like bananas, apples, oranges not so much"
		query = 'bananas AND apples AND oranges'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	# OR

	it "Search.new(query: 'bananas OR apples').test(str) #=> true" do
		str = "I really like bananas, apples not so much"
		query = 'bananas OR apples'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	# - , negative token

	it "Search.new(query: 'bananas -apples').test(str) #=> true" do
		str = "I really like bananas not so much"
		query = 'bananas -apples'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	it "Search.new(query: 'bananas -apples').test(str) #=> true" do
		str = "I really like bananas, oranges not so much"
		query = 'bananas -apples'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	it "Search.new(query: '-bananas -apples oranges').test(str) #=> true" do
		str = "I really like oranges not so much"
		query = '-bananas -apples oranges'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	it "Search.new(query: '-bananas -apples oranges').test(str) #=> true" do
		str = "I really like oranges not so much"
		query = '-bananas -apples oranges -strawberry'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	# phrase wrapper ex: '"not so much"'

	it 'Search.new(query: '"not so much"').test(str) #=> true' do
		str = "I really like bananas, apples not so much"
		query = '"not so much"'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	# phrase wrapper ex: '"not so much"' with AND

	it 'Search.new(query: '"not so much"').test(str) #=> true' do
		str = "I really like bananas, apples not so much"
		query = '"not so much" AND "like bananas"'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	# phrase wrapper ex: '"not so much"' with OR

	it 'Search.new(query: '"not so much"').test(str) #=> true' do
		str = "I really like bananas, apples not so much"
		query = '"not so much" OR "like bananas"'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	# *

	it "Search.new(query: 'bananas').test(str) #=> true" do
		str = "I really like bananas, apples not so much"
		query = 'bananas'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	it "wildcard * at the end: query = 'bana*'" do
		str = "I really like bananas, apples not so much"
		query = 'bana*'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	it "wildcard * at the beginning: query = '*bana'" do
		str = "I really like bananas, apples not so much"
		query = '*bana'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	it "wildcard * at the middle: query = 'ba*na'" do
		str = "I really like bananas, apples not so much"
		query = 'ba*na'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	it "wildcard * at the middle: query = 'bananas*like' changing position of splitted words" do
		str = "I really like bananas, apples not so much"
		query = 'bananas*like'
		expect(Search.new(query: query).test(str)).to eq(false)
	end

	# To perform a single character wildcard search use the "?" symbol. NOT LISTED!
	# it "wildcard ? at the middle: query = 'bananas?like' changing position of splitted words" do
	# 	str = "I really like bananas, apples not so much"
	# 	query = 'bananas?like'
	# 	expect(Search.new(query: query).test(str)).to eq(false)
	# end

	# signal of precedence '(xxx)'

	it "signal of precedence on query: '(bananas)'" do
		str = "I really like bananas, apples not so much"
		query = '(bananas)'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	it "signal of precedence on query: '(bananas OR mangos)'" do
		str = "I really like bananas, apples not so much"
		query = '(bananas OR mangos)'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	it "signal of precedence on query: '(bananas OR mangos OR oranges)'" do
		str = "I really like bananas, apples not so much"
		query = '(bananas OR mangos OR oranges)'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	# signal of precedence '((xxx) AND yyy)'

	it "signal of precedence on query: '(bananas OR mangos) AND much'" do
		str = "I really like bananas, apples not so much"
		query = '((bananas OR mangos) AND much)'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	it "signal of precedence on query: '(bananas OR mangos) AND much'" do
		str = "I really like bananas, apples not so much"
		query = '((bananas OR mangos) OR much)'
		expect(Search.new(query: query).test(str)).to eq(true)
	end

	# it "signal of precedence on query: '(bananas OR mangos) AND foo'" do
	# 	str = "I really like bananas, apples not so much"
	# 	query = '((bananas OR mangos) AND foo)'
	# 	expect(Search.new(query: query).test(str)).to eq(false)
	# end

end

describe 'testing single methods' do

	#check_order

	it "check_order with arr = ['a', 'b', 'c']" do
		arr = ['a', 'b', 'c']
		a = 'abc'
		expect(Search.check_order(a, arr)).to eq(true)
	end
	it "check_order with arr = ['a', 'c', 'b']" do
		arr = ['a', 'c', 'b']
		a = 'abc'
		expect(Search.check_order(a, arr)).to eq(false)
	end
	it "check_order with arr = ['a']" do
		arr = ['a']
		a = 'abc'
		expect(Search.check_order(a, arr)).to eq(true)
	end
	it "check_order with arr = ['a']" do
		arr = ['bananas', 'like']
		a = "I really like bananas, apples not so much"
		expect(Search.check_order(a, arr)).to eq(false)
	end

	# check_presence_AND

	it "check_presence_AND with arr = ['banana','apples']" do
		arr = ['bananas', 'apples']
		str = "I really like bananas, apples not so much"
		expect(Search.check_presence_AND(str, arr)).to eq(true)
	end
	it "check_presence_AND with arr = ['banana','oranges']" do
		arr = ['bananas', 'oranges']
		str = "I really like bananas, apples not so much"
		expect(Search.check_presence_AND(str, arr)).to eq(false)
	end

	# check_presence_OR

	it "check_presence_OR with arr = ['banana','apples']" do
		arr = ['bananas', 'apples']
		str = "I really like bananas"
		expect(Search.check_presence_OR(str, arr)).to eq(true)
	end

	it "check_presence_OR with arr = ['banana','apples']" do
		arr = ['bananas', 'apples']
		str = "I really like apples"
		expect(Search.check_presence_OR(str, arr)).to eq(true)
	end

	# filter_array

	it "filter_array with arr = ['banana','-apples']" do
		arr = ['bananas', '-apples']
		expect(Search.filter_array(arr, '-')).to eq(['bananas'])
	end

	it "filter_array with arr = ['banana','-apples']" do
		arr = ['-bananas', '-apples']
		expect(Search.filter_array(arr, '-')).to eq([])
	end

	it "filter_array with arr = ['banana', '-apples', 'oranges']" do
		arr = ['-bananas', '-apples', 'oranges']
		expect(Search.filter_array(arr, '-')).to eq(['oranges'])
	end

	#Don't need this, need to evaluate while iterating

	# # iterate_query

			# it "iterate_query on query (bananas OR mangos)" do
			# 	str = "I really like bananas, apples not so much"
			# 	query = '(bananas OR mangos)'
			# 	expect(Search.iterate_query(query)).to eq('bananas OR mangos')
			# end

			# it "iterate_query on query (bananas OR mangos AND oranges)" do
			# 	str = "I really like bananas, apples not so much"
			# 	query = '(bananas OR mangos AND oranges)'
			# 	expect(Search.iterate_query(query)).to eq('bananas OR mangos AND oranges')
			# end

			# it "iterate_query on query (bananas OR mangos AND oranges)" do
			# 	str = "I really like bananas, apples not so much"
			# 	query = '((bananas OR mangos) AND oranges)'
			# 	expect(Search.iterate_query(query)).to eq('(bananas OR mangos) AND oranges')
			# end

	# #check trim words
	# it "check_presence_OR with arr = ['banana', ' apples']" do
	# 	arr = ['bananas', ' apples']
	# 	str = "I really like bananas, apples not so much"
	# 	expect(Search.check_presence_OR(str, arr)).to eq(true)
	# end
end