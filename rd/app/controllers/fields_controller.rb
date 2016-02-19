class FieldsController < ApplicationController
  before_action :set_field, only: [:show, :edit, :update, :destroy]
  before_action :authenticate_user!

  # GET /fields
  # GET /fields.json
  def index
    fields = Field.where(user_id: current_user.id)
    if fields == nil
      fields = []
    end
    @fields = fields
  end

  # GET /fields/1
  # GET /fields/1.json
  def show
  end

  # GET /fields/new
  def new
    @field = Field.new
  end

  # GET /fields/1/edit
  def edit
  end

  # POST /fields
  # POST /fields.json
  def create
    @field = Field.new(field_params)
    @field.user_id = current_user.id
    @field.combo_box_option = params[:field][:combo_box_option].join(',')

    respond_to do |format|
      if @field.save
        format.html { redirect_to @field, notice: 'Field was successfully created.' }
        format.json { render :show, status: :created, location: @field }
      else
        format.html { render :new }
        format.json { render json: @field.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /fields/1
  # PATCH/PUT /fields/1.json
  def update

    old_name = @field.name
    new_name = field_params[:new_name]

    ContactValue.where({ 
      :field_name => old_name,
      :user_id => current_user.id
    }).update_all({ :field_name => new_name })

    if params[:field][:input] == '3' #maldito ruby formente tipado
      params[:field][:combo_box_option] = params[:field][:combo_box_option].join(',')
    end

    respond_to do |format|
      if @field.update(params[:field])
        format.html { redirect_to @field, notice: 'Field was successfully updated.' }
        format.json { render :show, status: :ok, location: @field }
      else
        format.html { render :edit }
        format.json { render json: @field.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /fields/1
  # DELETE /fields/1.json
  def destroy
    @field.destroy
    respond_to do |format|
      format.html { redirect_to fields_url, notice: 'Field was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_field
      @field = Field.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def field_params
      params.require(:field).permit!
    end
end
