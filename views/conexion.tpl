<!DOCTYPE html>
<html lang="en">
<head>

  <!-- Basic Page Needs
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <meta charset="utf-8">
  <title>MOTOGP 2017</title>
  <meta name="description" content="">
  <meta name="author" content="">

  <!-- Mobile Specific Metas
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- FONT
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <link href="//fonts.googleapis.com/css?family=Raleway:400,300,600" rel="stylesheet" type="text/css">

  <!-- CSS
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <link rel="stylesheet" href="css/normalize.css">
  <link rel="stylesheet" href="css/skeleton.css">

  <!-- Favicon
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <link rel="icon" type="image/png" href="images/favicon.png">

</head>
</head>
<body>

  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <div class="container">
    <div class="row">
      <div class="one-half column" style="margin-top: 10%">
        <h4>Conexion</h4>
        <form action="/login" method="post">
          <fieldset>
            <legend>Personalia:</legend>
          <div class="row">
            <div class="six columns">
              <label for="UserInput">Usuario</label>
              <input class="u-full-width" name="UserInput" type="usuario">
            </div>
            <div class="six columns">
              <label for="PasswordInput">Contraseña</label>
              <input class="u-full-width" name="PasswordInput" type="password">
            </div>
          </div>
          <div class="row">
            <div class="six columns">
              <label for="DatabaseInput">Base de datos</label>
              <input class="u-full-width" name="DatabaseInput" type="conexion">
            </div>
            <div class="six columns">
              <label for="PasswordInput">Host</label>
              <input class="u-full-width" name="HostInput" type="host">
            </div>
          </div>
          <input class="button-primary" value="login" type="submit">
         </fieldset>
        </form>
      </div>
    </div>
  </div>

<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
</body>
</html>
