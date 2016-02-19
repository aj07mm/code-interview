class ContactsController < ApplicationController
  before_action :set_contact, only: [:show, :edit, :update, :destroy]
  before_action :authenticate_user!
  # before_action :reset_schema

  # GET /contacts
  # GET /contacts.json
  def index
    contacts = Contact.where(user_id: current_user.id)
    if contacts == nil
      contacts = []
    end
    @contacts = contacts
  end

  # GET /contacts/1
  # GET /contacts/1.json
  def show
    @current_user = current_user
  end

  # GET /contacts/new
  def new
    @current_user = current_user
    @contact = Contact.new
  end

  # GET /contacts/1/edit
  def edit
    @current_user = current_user
  end

  # POST /contacts
  # POST /contacts.json
  def create
    @contact = Contact.new
    @contact.set_default_values(contact_params, current_user)

    respond_to do |format|
      if @contact.save
        Contact.save_custom_values(contact_params, @contact, current_user)
        format.html { redirect_to @contact, notice: 'Contact was successfully created.' }
        format.json { render :show, status: :created, location: @contact }
      else
        format.html { render :new }
        format.json { render json: @contact.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /contacts/1
  # PATCH/PUT /contacts/1.json
  def update
    respond_to do |format|
      @contact.set_default_values(contact_params, current_user)
      if Contact.update_custom_values(contact_params, @contact, current_user)
        format.html { redirect_to @contact, notice: 'Contact was successfully updated.' }
        format.json { render :show, status: :ok, location: @contact }
      else
        format.html { render :edit }
        format.json { render json: @contact.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /contacts/1
  # DELETE /contacts/1.json
  def destroy
    @contact.destroy
    respond_to do |format|
      format.html { redirect_to contacts_url, notice: 'Contact was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_contact
      @contact = Contact.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def contact_params
      params.require(:contact).permit(current_params)
    end

    def current_params
      custom_fields = Field.where(user_id: current_user.id)

      if custom_fields
        custom_fields = custom_fields.map { |x| x.name.to_sym }
      else
        custom_fields = []
      end
      Contact.column_names + custom_fields
    end
end
