class User < ActiveRecord::Base
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :trackable, :validatable

  def custom_fields
    custom_fields = Field.where(user_id: self.id)
    if custom_fields == nil
      custom_fields = []
    end
    custom_fields
  end

end
