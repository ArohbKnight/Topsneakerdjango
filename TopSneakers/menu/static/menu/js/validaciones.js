
// BOTON CREAR CUENTA DE REGISTRARSE
function crearcuenta() {
    // Obtenemos los valores de los campos del formulario
    var nombre = document.getElementById("nombre").value;
    var rut = document.getElementById("rut").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    // Expresiones regulares para validar los campos
    var regexNombreCompleto = /^[a-zA-Z\s]+$/;
    var regexRUT = /^\d{7,8}-[\dkK]$/;
    var regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    var regexContrasena = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/;

    // Validación del campo de nombre completo
    if (nombre == "") {
        alert("El campo de nombre completo no puede estar vacío");
        return false;
    } else if (!regexNombreCompleto.test(nombre)) {
        alert("El campo de nombre completo sólo puede contener letras y espacios");
        return false;
    }

    // Validación del campo de RUT
function verificarRUT(rut) {
    // Eliminar puntos y guión del RUT y convertir a mayúsculas
    rut = rut.replace(/[.-]/g, '').toUpperCase();
  
    // Validar el formato del RUT
    if (!/^(\d{1,2})(\d{3})(\d{3})(\d|K)$/.test(rut)) {
      alert("El campo de RUT debe tener el formato 12345678-9");
      return false;
    }
  
    // Obtener el cuerpo y dígito verificador del RUT
    const cuerpo = rut.slice(0, -1);
    const digitoVerificador = rut.slice(-1);
  
    // Calcular el dígito verificador esperado
    let suma = 0;
    let factor = 2;
    for (let i = cuerpo.length - 1; i >= 0; i--) {
      suma += parseInt(cuerpo.charAt(i)) * factor;
      factor = factor === 7 ? 2 : factor + 1;
    }
    const digitoVerificadorEsperado = 11 - (suma % 11);
    const digitoVerificadorCalculado = digitoVerificadorEsperado === 11 ? '0' : digitoVerificadorEsperado === 10 ? 'K' : digitoVerificadorEsperado.toString();
  
    // Verificar si el dígito verificador es válido
    if (digitoVerificador !== digitoVerificadorCalculado) {
      alert("El RUT ingresado no es válido");
      return false;
    }
  
    // El RUT es válido
  
    return true;
  }
  
  // Ejemplo de uso en tu código existente
  if (rut === "") {
    alert("El campo de RUT no puede estar vacío");
    return false;
  } else {
    verificarRUT(rut);
  }
  
    // Validación del campo de correo
    if (email == "") {
        alert("El campo de correo no puede estar vacío");
        return false;
    } else if (!regexCorreo.test(email)) {
        alert("El campo de correo debe tener un formato válido");
        return false;
    }

    // Validación del campo de contraseña
    if (password == "") {
        alert("El campo de contraseña no puede estar vacío");
        return false;
    } else if (!regexContrasena.test(password)) {
        alert("La contraseña debe contener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número");
        return false;
    }

    // Si todos los campos son válidos, el formulario se envía
    alert("Creacion de cuenta de manera exitosa");
    return true;
}





// BOTON ENTRAR 
function entrar() {
    // Obtenemos el valor del campo de correo del formulario
    var correo = document.getElementById("correo").value;

    // Expresión regular para validar el campo de correo
    var regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Validación del campo de correo
    if (correo == "") {
        alert("El campo de correo no puede estar vacío");
        return false;
    } else if (!regexCorreo.test(correo)) {
        alert("El campo de correo debe tener un formato válido");
        return false;
    }
}





 //BOTON ENVIAR DE CONTACTANOS Y CONTACTANOS ADMIN
function Enviar() {
    // Obtenemos los valores de los campos del formulario
    var nombre = document.getElementById("nombre").value;
    var correo = document.getElementById("correo").value;
    var mensaje = document.getElementById("mensaje").value;

    // Expresión regular para validar el campo de correo
    var regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Validación de los campos
    if (nombre == "") {
        alert("El campo de nombre completo no puede estar vacío");
        return false;
    } else if (correo == "") {
        alert("El campo de correo electrónico no puede estar vacío");
        return false;
    } else if (!regexCorreo.test(correo)) {
        alert("El campo de correo electrónico debe tener un formato válido");
        return false;
    } else if (mensaje == "") {
        alert("El campo de mensaje no puede estar vacío");
        return false;
    }

    // Si los campos son válidos, el formulario se envía
    alert("Mensaje enviado correctamente");
    return true;
}





//CONFIRMAR CAMBIO DE DATOS DE PERFIL
function confirmar() {
    // Obtiene los valores de los campos
    var rut = document.getElementById('rut').value;
    var nombre = document.getElementById('nombre').value;
    var apellido = document.getElementById('apellido').value;

    // Valida el RUT
    if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rut)) {
      alert("El campo de RUT no puede estar vacío");
      return false;
    }

    // Valida el nombre
    if (nombre.length == 0) {
      alert("El campo de nombre no puede estar vacío");
      return false;
    }

    // Valida el apellido
    if (apellido.length == 0) {
      alert("El campo de apellido no puede estar vacío");
      return false;
    }

    // Si todo está correcto, se envía el formulario
    alert("Se han actualizado los datos correctamente");
    return true;
  }






  
  // BOTON PRIVACIDAD
  function confirmarpriv(){
        //  valores de los campos del formulario
    var contraseñaac = document.getElementById('contraseñaac').value;

    var contraseñan = document.getElementById('contraseñan').value;

    var contraseñac = document.getElementById('contraseñac').value;

    var correo = document.getElementById("correo").value;

       // Expresión regular para validar el campo de correo
       var regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
       if (correo == "") {
        alert("El campo de correo no puede estar vacío");
        return false;
    } else if (!regexCorreo.test(correo)) {
        alert("El campo de correo debe tener un formato válido");
        return false;
    }
    if (contraseñaac.length == 0) {
        alert("El campo de contraseña actual no puede estar vacío");
        return false;
      }
      if (contraseñan.length == 0) {
        alert("El campo de nueva contraseña no puede estar vacío");
        return false;
      }
  
      if (contraseñac.length == 0) {
        alert("El campo de confirmar contraseña no puede estar vacío");
        return false;
      }
    }