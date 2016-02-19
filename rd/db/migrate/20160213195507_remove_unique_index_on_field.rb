class RemoveUniqueIndexOnField < ActiveRecord::Migration
  def change
  	remove_index :fields, :input
  end
end
