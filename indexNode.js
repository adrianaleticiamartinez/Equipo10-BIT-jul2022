// Importación de dependencias
const express = require("express");
const csv = require("csvtojson");

// Inicializamos express
const app = express();

// Inicialización de DB convirtiendo los CSV a JSON con ayuda de una libreria

// Creamos el JSON de clientes
let clients = {};
const convertCSV = async (route) => {
  const jsonArray = await csv().fromFile(route);
  clients = jsonArray;
};
convertCSV("assets/baseClientesHackaton2022.csv");

let usuarios = {};
// Creamos el JSON de usuarios
const convertCSVuser = async (route) => {
  const jsonArray = await csv().fromFile(route);
  usuarios = jsonArray;
};
convertCSVuser("assets/baseUsuarios.csv");

const authenticate = (user, auth) => {
  // esta funcion revisará en la BD de usuario para ver si este existe, ademas revisará que no tenga acceso restringido, este dato viene en perfil
  return usuarios.some((usr) => {
    return (
      usr.usuario === user && usr.auth === auth && usr.perfil !== "Restringido"
    );
  });
};

// Traer un cliente por su id
app.get("/getclientbyid", (req, res) => {
  // Primero verificamos que el usuario exista en la BD de usuario y no tenga acceso restringido
  if (!authenticate(req.query.usuario, req.query.auth)) {
    // Si no tiene acceso, regresaremos 403, el status HTTP de Prohibido
    res.sendStatus(403);
  } else {
    // Si si tiene acceso revisaremos la BD de cliente y regresaremos el dato
    const client_id = req.query.client;
    // Find nos ayuda a buscar rapidamente en la coleccion y regresa el dato con los parametros especificados si es que existe
    const client = clients.find((el) => {
      return el.idCliente === client_id;
    });
    // Si el cleinte no existe regresará "CLIENTE NO EXISTE" aunque tengamos permisos de pedir clientes al servidor
    res.json(client || "CLIENTE NO EXISTE");
  }
});

app.listen(3001, () => console.log("Example app listening on port 3000!"));

/* Ejemplos
Este usario no existe y no tiene acceso
http://localhost:3001/getclientbyid?usuario=usuarioimaginario&auth=contra&client=BF000002999

Este usario si tiene acceso
http://localhost:3001/getclientbyid?usuario=Gustavo_Moreno&auth=456098&client=BF000002999

Este usario si tiene acceso pero el cleinte no existe
http://localhost:3001/getclientbyid?usuario=Gustavo_Moreno&auth=456098&client=HHH

Este usuario si está registrado pero tiene acceso restringido
http://localhost:3001/getclientbyid?usuario=katy&auth=KatiaFlores&client=BF000002999
*/
