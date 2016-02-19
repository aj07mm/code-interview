module FieldsHelper
	def get_input_name(input_number)
		Field.inputs.select { |x| x[:input] == input_number }[0][:name]
	end
end
