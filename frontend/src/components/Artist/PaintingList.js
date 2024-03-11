import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PaintingList = () => {
    const [paintings, setPaintings] = useState([]);

    useEffect(() => {
        // Fetch list of paintings from the backend
        axios.get('/api/paintings')
            .then(response => {
                setPaintings(response.data);
            })
            .catch(error => {
                console.error('Error fetching paintings:', error);
            });
    }, []);

    return (
        <div>
            <h2>Paintings</h2>
            <ul>
                {paintings.map(painting => (
                    <li key={painting.id}>
                        {painting.name} - {painting.date}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default PaintingList;
