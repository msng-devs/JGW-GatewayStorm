const app = require("../app");

const {createData,clearData} = require("./utlis/dataController");
const request = require("supertest")

beforeEach(async () => {
    await createData();
});

afterEach(async () => {
    await clearData();
});

test('find single', async () => {
    const response = await request(app)
        .get('/api/v1/apiRoute/1')
        .expect(200);

    console.log(response.body);
    // expect(response.body.name).toBe('Alice');
    // expect(response.body.email).toBe('alice@example.com');
});