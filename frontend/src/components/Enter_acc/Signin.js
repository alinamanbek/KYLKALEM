import React, { useState } from 'react';

const SignIn = () => {
    // State variables to store the user's email and password
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    // Function to handle form submission
    const handleSubmit = (event) => {
        event.preventDefault();
        
        // Here you would typically make an HTTP request to your backend for authentication
        // For simplicity, let's just log the email and password for now
        console.log('Email:', email);
        console.log('Password:', password);

        // After authentication, you can redirect the user or perform other actions
    };

    return (
        <div className="container">
            <h2>Sign in</h2>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="email" className="form-label">Email</label>
                    <input type="email" className="form-control" id="email" value={email} onChange={(e) => setEmail(e.target.value)} />
                </div>
                <div className="mb-3">
                    <label htmlFor="password" className="form-label">Password</label>
                    <input type="password" className="form-control" id="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                </div>
                <button type="submit" className="btn btn-primary">Sign in</button>
            </form>
        </div>
    );
};

export default SignIn;
