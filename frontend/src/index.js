import { checkHealth } from './api.js';

console.log("ERP System Frontend Initialized");

document.addEventListener('DOMContentLoaded', async () => {
    const root = document.getElementById('root');
    root.innerHTML = '<h1>Welcome to the ERP System</h1><p>Loading status...</p>';

    const status = await checkHealth();
    if (status) {
        root.innerHTML += `<p>Status: ${status.status}</p>`;
    } else {
        root.innerHTML += `<p>Status: Backend unreachable</p>`;
    }
});
