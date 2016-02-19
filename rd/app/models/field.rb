class Field < ActiveRecord::Base
	validates :name, uniqueness: true
	validates :input, uniqueness: { scope: :user_id,
    message: "one type of input per user" }

	def self.inputs
		[
			{ :name => 'text',      :input => 1 },
			{ :name => 'text_area', :input => 2 },
			{ :name => 'combo_box', :input => 3 }
		]
	end
end
