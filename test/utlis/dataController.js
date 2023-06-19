const sequelize = require('../../config/database.config');
const fs = require('fs');

const createData = async () => {
    // await sequelize.sync({force: true});
    let ddl = fs.readFileSync('./resource/DDL.sql', 'utf8');
    await sequelize.query(ddl,{ raw: true }).catch(err => {
        console.log(err)
    });
    console.log('DDL done')


    const dml = fs.readFileSync('./resource/DML.sql', 'utf8');
    await sequelize.query(dml,{ raw: true }).catch(err => {
        console.log(err)
    });
    console.log('DML done')

}
const clearData = async () => {
    const truncate = fs.readFileSync('./resource/TRUNCATE.sql', 'utf8');
    await sequelize.query(truncate);
    console.log('truncate done')
}
module.exports = {createData,clearData}