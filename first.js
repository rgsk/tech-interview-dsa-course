const fs = require("fs");
const path = require("path");

// Change this to your target folder
const folderPath = "./src/02. Searching";

fs.readdir(folderPath, (err, files) => {
    if (err) {
        console.error("Error reading folder:", err);
        return;
    }

    const cleaned = files
        .filter((file) => file.endsWith(".ipynb"))
        .map((file) => {
            // Remove leading number (e.g., "01. ") and ".ipynb"
            return file.replace(/^\d+\.\s*/, "").replace(/\.ipynb$/, "");
        });

    console.log(cleaned);
});
