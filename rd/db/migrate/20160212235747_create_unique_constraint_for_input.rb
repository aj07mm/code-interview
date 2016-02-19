class CreateUniqueConstraintForInput < ActiveRecord::Migration
  def change
    add_index :fields, :input, :unique => true
  end
end
