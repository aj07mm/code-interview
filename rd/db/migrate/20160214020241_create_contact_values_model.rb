class CreateContactValuesModel < ActiveRecord::Migration
  def change
    create_table :contact_values do |t|
      t.string :value
      t.string :field_name
      t.integer :contact_id
      t.integer :user_id

      t.timestamps null: false
    end
  end
end
