// Importación de dependencias
const express = require('express');
const csv = require("csvtojson");

// Inicializamos express
const app = express();

// Inicialización de DB
let clients = {};
const convertCSV = async(route) => {
    const jsonArray = await csv().fromFile(route);
    clients = jsonArray;
};
convertCSV('assets/baseClientesHackaton2022.csv');


let usuarios = {};
const convertCSVuser = async(route) => {
    const jsonArray = await csv().fromFile(route);
    usuarios = jsonArray;
};
convertCSVuser('assets/baseUsuarios.csv');


// Hello world
app.get('/', (req, res) => res.send('Hello World!'));

// Traer todos los clientes
app.get('/getclients', (req, res) => {
    res.json(clients);
});

// Traer un cliente por su id
app.get('/getclientbyid', (req, res) => {
    const id = req.query.id || 'sin id'
    const client = clients.find(el => {
        return el.idCliente === id;
    })
    res.json(client);
});

// Traer un usuario por su id
app.get('/getuserby', (req, res) => {
    const id = req.query.id || 'sin id'
    const user = usuarios.find(el => {
        return el.usuario === user;
    })
    res.json(user);
});

app.listen(3000, () => console.log('Example app listening on port 3000!'));