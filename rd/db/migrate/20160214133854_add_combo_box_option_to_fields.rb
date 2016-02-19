class AddComboBoxOptionToFields < ActiveRecord::Migration
  def change
  	add_column :fields, :combo_box_option, :text
  end
end
