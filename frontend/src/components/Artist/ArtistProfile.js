import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ArtistProfile = () => {
    const [artistInfo, setArtistInfo] = useState(null);

    useEffect(() => {
        // Fetch artist profile data from the backend
        axios.get('/api/artist/profile')
            .then(response => {
                setArtistInfo(response.data);
            })
            .catch(error => {
                console.error('Error fetching artist profile:', error);
            });
    }, []);

    return (
        <div className="container">
            <div className="row">
                {/* Left Half */}
                <div className="col-md-8">
                    <div className="profile-info">
                        <h2>Edit Personal Information</h2>
                        <img src="/Users/alina/Desktop/Kyl-Kalem/front_app/public/20230823_181704.jpg" alt="Artist Photo" className="artist-photo" />
                        <form>
                            <div className="mb-3">
                                <label htmlFor="pseudonym" className="form-label">Pseudonym</label>
                                <input type="text" className="form-control" id="pseudonym" defaultValue="YourPseudonym" />
                            </div>
                            {/* Include other form inputs */}
                            <button type="submit" className="btn btn-primary">Save Changes</button>
                        </form>
                    </div>
                </div>
                {/* Right Half */}
                <div className="col-md-4">
                    <div className="btn-group-horizontal">
                        <button type="button" className="btn btn-primary">Pictures</button>
                        <button type="button" className="btn btn-success">Create</button>
                        <button type="button" className="btn btn-info">Clients</button>
                    </div>
                    <div className="text-center mt-4">
                        <a href="#" className="btn btn-danger">Logout</a>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ArtistProfile;
