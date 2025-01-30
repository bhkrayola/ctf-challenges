#!/usr/bin/nodejs

const express = require('express')
const app = express()
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('database.db');
app.set('view engine', 'ejs')
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static("static"));

app.get('/', function(req,res){
    res.render('form')
});

app.post('/form_handler', function (req, res) {
  const { username, password } = req.body;
  const sql = `SELECT * FROM users WHERE username='${username}' AND password='${password}'`;

  db.all(sql, (err, rows) => {
      if (err) throw err;
      if (rows.length > 0) {
          res.status(200).json({ success: true, message: 'Login successful! flag{fake_flag}' });
      } else {
          res.status(200).json({ success: false, message: 'Login failed - Invalid credentials' });
      }
  });
});

app.get('/thelibrary', function (req, res){
    res.render('library')
});

var listener = app.listen(process.env.PORT || 8080, process.env.HOST || "0.0.0.0", function() {
    console.log("Express server started");
});