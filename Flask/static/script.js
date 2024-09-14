function mostrar(id,nombre,apellido,telefono){
    document.getElementById("nombre").value = nombre;
    document.getElementById("apellido").value = apellido;
    document.getElementById("telefono").value = telefono;
    document.getElementById("id").value = id;
}
 function updateContact(){
    const id = document.getElementById("id").value;
    const nombre = document.getElementById("nombre").value;
    const apellido = document.getElementById("apellido").value;
    const telefono = document.getElementById("telefono").value;
    if(id==""){
      alert("Error al actualizar");
    }
    else{
        fetch('/actualizar',{
            method: 'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body: JSON.stringify({
                "id": id,
                "nombre": nombre,
                "apellido": apellido,
                "telefono": telefono
            })
        })
        .then(response => response.json())
        .then(data=>{
            if(data.status === 'success'){
                alert('Contacto actualizado')
                window.location.reload();
            }
            else {
                alert('Error al actualizar el contacto.');
            }
        })
        .catch(error => console.error('Error:', error));

    }

 }