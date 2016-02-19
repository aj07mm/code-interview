// This is a manifest file that'll be compiled into application.js, which will include all the files
// listed below.
//
// Any JavaScript/Coffee file within this directory, lib/assets/javascripts, vendor/assets/javascripts,
// or any plugin's vendor/assets/javascripts directory can be referenced here using a relative path.
//
// It's not advisable to add code directly here, but if you do, it'll appear at the bottom of the
// compiled file.
//
// Read Sprockets README (https://github.com/rails/sprockets#sprockets-directives) for details
// about supported directives.
//
//= require jquery
//= require jquery_ujs
//= require_tree .

document.addEventListener("DOMContentLoaded", function(){
    var fieldInput = document.getElementById("field_input");
    var myDiv = document.getElementById("field-combo-box");
    var moreInputs = document.getElementById("more-inputs");


    fieldInput.addEventListener('change', function(evt){
      var comboSection = document.getElementById('field-combo-box-section');
      if(evt.target.value == 3){
        comboSection.classList.remove('hide');
      }else{
        comboSection.classList.remove('show');
        comboSection.classList.add('hide');
      }
    });
    moreInputs.addEventListener('click', function(){
      var divClone = myDiv.cloneNode(true); // the true is for deep cloning
      document.getElementById('field-combo-box-section').appendChild(divClone);
    })
 });