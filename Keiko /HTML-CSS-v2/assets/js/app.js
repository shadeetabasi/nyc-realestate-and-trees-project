//import dependencies 
const fs = require('fs');
const csv = require('csvtojson');
const Parser = require('json2csv');

(async () => {
    //load csv
    const rs_data = await csv().fromFile('./data/nyc_real_estate_building_final_use_this.csv');

    console.log(rs_data);

})();