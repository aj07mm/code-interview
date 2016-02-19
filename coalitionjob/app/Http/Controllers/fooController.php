<?php

namespace App\Http\Controllers;

use App\Foo;

use Illuminate\Http\Request;

use App\Http\Requests;
use App\Http\Controllers\Controller;

class fooController extends Controller
{
    public function create()
    {
    	$data = \Request::all();
    	if($data){
    		$foo = new Foo;
			$foo->name = $data['name'];
			$foo->quantity = $data['quantity'];
			$foo->price = $data['price'];
			$foo->save();
    		return (String)$foo->save();
    	}
    	return (String)false;
    }
}