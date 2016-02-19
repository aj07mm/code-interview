<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateFoosTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('foos', function(Blueprint $table)
        {
            $table->increments('id');

            $table->string('name', 255);
            $table->integer('quantity');
            $table->float('price');

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::table('nerds', function (Blueprint $table) {
            Schema::drop('nerds');
        });
    }
}
