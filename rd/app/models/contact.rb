class Contact < ActiveRecord::Base
	validates_presence_of :email

	def self.default_fields
		[:name, :email]
	end

	def set_default_values(contact_params, current_user)
	    self.name = contact_params[:name]
	    self.email = contact_params[:email]
	    self.user_id = current_user.id
	    self.save
	end

	def self.save_custom_values(contact_params, contact_object, user_object)
		contact_params.each do |field_name, value|
          contact_values = ContactValue.new
          contact_values.value = value
          contact_values.field_name = field_name
          contact_values.contact_id = contact_object.id
          contact_values.user_id = user_object.id
          contact_values.save
        end
	end

	def self.update_custom_values(contact_params, contact_object, user_object)
		contact_params.each do |field_name, value|
			if not self.default_fields.include?(field_name)
				contact_values = ContactValue.find_by({
					:field_name => field_name,
					:contact_id => contact_object.id,
					:user_id => user_object.id
				})
				if contact_values
					contact_values.value = value
					contact_values.field_name = field_name
					contact_values.contact_id = contact_object.id
					contact_values.user_id = user_object.id
					contact_values.save
				else
					self.save_custom_values(contact_params, contact_object, user_object)
				end
			end
        end
	end

end
