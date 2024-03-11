import React from 'react';

const ClientProfile = () => {
    return (
        <div className="container">
            <div className="row">
                {/* Left Half */}
                <div className="col-md-8">
                    <div className="profile-info">
                        <h2>Edit Personal Information Clients</h2>
                        <img src="/Users/alina/Desktop/Kyl-Kalem/front_app/public/20230823_181704.jpg" alt="Client Photo" className="artist-photo" />
                        <form>
                            <div className="mb-3">
                                <label htmlFor="name" className="form-label">Name</label>
                                <input type="text" className="form-control" id="name" value="John" />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="surname" className="form-label">Surname</label>
                                <input type="text" className="form-control" id="surname" value="Doe" />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="email" className="form-label">Email</label>
                                <input type="email" className="form-control" id="email" value="example@example.com" />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="phone" className="form-label">Phone</label>
                                <input type="text" className="form-control" id="phone" value="+1234567890" />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="newPassword" className="form-label">Password</label>
                                <input type="password" className="form-control" id="newPassword" />
                            </div>
                            <button type="submit" className="btn btn-primary">Save Changes</button>
                        </form>
                    </div>
                </div>
                {/* Right Half */}
                <div className="col-md-4">
                    <div className="btn-group-horizontal">
                        <button type="button" className="btn btn-primary">Basket</button>
                    </div>
                    <div className="card mt-4">
                        <div className="card-body">
                            {/* Additional content here */}
                        </div>
                    </div>
                    <div className="text-center mt-4">
                        <a href="#" className="btn btn-danger">Logout</a>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ClientProfile;
