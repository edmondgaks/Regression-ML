const sqlite3 = require('sqlite3').verbose();

const dbFile = 'health_data.db';
const db = new sqlite3.Database(dbFile);

const query = 'SELECT * FROM health_records';

const features = [];
const labels = [];

db.all(query, [], (err, rows) => {
    if (err) {
      throw err;
    }
  
    // Display the retrieved data
    rows.forEach(row => {
      console.log(row);
    });
  
    // Close the database connection
    db.close();
  });