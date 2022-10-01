function validar_formulario()
{
   
    console.log("Inicio validar formulario.");

    
    var nombre = document.formRegistro.userName.value;
    var email = document.formRegistro.userMail.value;
    var password = document.formRegistro.password.value;

    if(nombre.length == 0 || nombre.length < 8)
    {
        alert("Debe escrir un nombre con minimo 8 carateres.");
        document.formRegistro.userName.focus();
        return false;
    }

    var formato_email = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;

    if(!email.match(formato_email))
    {
        alert("Escriba un correo por favor.");
        return false;
    }

    if(password.length == 0 || password.length < 8)
    {
        alert("Debe escrir una clave con minimo 8 carateres.");
        return false;
    } 
   
    
    return true;
}

function mostrarClave()
{
   var campoClave = document.getElementById("password");
   var tipo = campoClave.type;

   if(tipo == "password")
   {
     campoClave.type="text";
   }
   else
   {
    campoClave.type="password";
   }



}