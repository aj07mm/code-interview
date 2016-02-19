<!DOCTYPE html>
<html>
    <head>
        <title>Laravel</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
        <style>
            html, body {
                height: 100%;
            }

            body {
                margin: 0;
                padding: 0;
                width: 100%;
                display: table;
                font-weight: 100;
                font-family: 'Lato';
            }

            .container {
                text-align: center;
                display: table-cell;
                vertical-align: middle;
            }

            .content {
                text-align: center;
                display: inline-block;
            }

            .title {
                font-size: 96px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="content">
                <div class="title">foo SPA</div>
            </div>
            <div id="alert-box" class="hide alert alert-success">
              <strong>Success!</strong> Indicates a successful or positive action.
            </div>
            <form action="foo/create" type="POST">
              <div class="form-group">
                <label for="exampleInputEmail1">Product Name</label>
                <input type="text" class="form-control" id="name" name="name" placeholder="name">
              </div>
              <div class="form-group">
                <label for="exampleInputPassword1">Quantity In stock</label>
                <input type="number" class="form-control" id="quantity" name="quantity" placeholder="quantity">
              </div>
              <div class="form-group">
                <label for="exampleInputPassword1">Price per item</label>
                <input type="number" class="form-control" id="price" name="price" placeholder="price">
              </div>

              <button type="submit" class="btn btn-default">Submit</button>
            </form>
        </div>
    </body>
    <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.4.min.js"></script>
    <script type="text/javascript">
        $("document").ready(function(){
            $("form").submit(function(e){
                e.preventDefault();
                var name = $("input#name").val();
                var quantity = $("input#quantity").val();
                var price    = $("input#price").val();
                $.ajax({
                    type: "POST",
                    url : "foo/create",
                    data : {
                        name: name,
                        quantity: quantity,
                        price: price
                    },
                    success : function(data){
                        if(data){
                            $('#alert-box').removeClass('hide').addClass('show').fadeOut('slow', function(){
                                $('#alert-box').removeClass('show').addClass('hide')
                            });
                        }
                    }
                },"json");
            });
        });

    </script>
</html>
