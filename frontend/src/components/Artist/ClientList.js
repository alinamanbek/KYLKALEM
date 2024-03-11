import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ClientList = () => {
    const [clients, setClients] = useState([]);

    useEffect(() => {
        // Fetch list of clients from the backend
        axios.get('/api/clients')
            .then(response => {
                setClients(response.data);
            })
            .catch(error => {
                console.error('Error fetching clients:', error);
            });
    }, []);

    return (
        <div>
            <h2>Clients</h2>
            <ul>
                {clients.map(client => (
                    <li key={client.id}>
                        {client.name} - {client.email} - {client.phone}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ClientList;
