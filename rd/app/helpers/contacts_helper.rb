module ContactsHelper
	def get_input(field_object, contact_object)
		if(field_object.input == 3)
			get_combo_box(field_object)
		else
			value = get_field_value(field_object, contact_object)
			if(field_object.input == 1)
				return text_field_tag("contact[#{field_object.name}]", value)
			end
			if(field_object.input == 2)
				return text_area_tag("contact[#{field_object.name}]", value, size: "24x6")
			end
		end
	end

	def get_combo_box(field_object)
		select_options = field_object.combo_box_option.split(',')
		return select_tag("contact[#{field_object.name}]", options_for_select(select_options))
	end

	def custom_fields
		current_user.custom_fields
	end

	def get_field_value(field_object, contact_object)
		res = ContactValue.find_by({
			:field_name => field_object.name,
			:contact_id => contact_object.id,
			:user_id => current_user.id
		})
		if res != nil
			res.value
		end
	end
end
