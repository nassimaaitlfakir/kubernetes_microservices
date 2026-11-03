const express = require("express");

const app = express();

app.get("/", async (req, res) => {
    res.json([
        { "name": "Service C - Node" }
    ]);
});

app.listen(8080, "0.0.0.0");