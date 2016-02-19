class AddUserIdToField < ActiveRecord::Migration
  def change
  	add_column :fields, :user_id, :integer
  end
end
