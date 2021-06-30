const DEV_API_URL = 'http://127.0.0.1:5000/api/calculate?function=';
const API_URL = '';

async function calculateFunction(formula) {
    if (formula) {
        const response = await postFunction(formula);
        console.log(response);
        return response.queryresult;
    }
    return {};
}

async function postFunction(func) {
    const response = await fetch(DEV_API_URL + encodeURI(func), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
    });
    return response.json();
}