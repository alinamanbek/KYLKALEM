import React from 'react';
import './App.css'; // Import your CSS file for styling
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

function App() {
  return (
    <div className="App">
      <header className="navbar">
        <img className="navbar-logo" src="/img/LOGO.png" alt="Logo" />
        <div>KYLKALEM</div>
        <div className="navbar-links">
          <a href="#about">About</a>
          <a href="#artist">Artist</a>
          <a href="#login">Log in</a>
          <a href="#logout">Sign in</a>
        </div>
      </header>

      <div className="carousel-container">
        <div id="carouselExampleCaptions" className="carousel slide" data-bs-ride="carousel" style={{ width: '60%', margin: '0 auto' }}>
          <div className="carousel-inner">
            <div className="carousel-item active">
              <img src="/img/KYLKALEM1.png" className="d-block w-100" alt="Slide 1" />
              <div className="carousel-caption d-none d-md-block">
                <h5>First slide label</h5>
                <p>Some representative placeholder content for the first slide.</p>
              </div>
            </div>
            <div className="carousel-item">
              <img src="/img/2.png" className="d-block w-100" alt="Slide 2" />
              <div className="carousel-caption d-none d-md-block">
                <h5>Second slide label</h5>
                <p>Some representative placeholder content for the second slide.</p>
              </div>
            </div>
            <div className="carousel-item">
              <img src="/img/3.png" className="d-block w-100" alt="Slide 3" />
              <div className="carousel-caption d-none d-md-block">
                <h5>Third slide label</h5>
                <p>Some representative placeholder content for the third slide.</p>
              </div>
            </div>
          </div>
          <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
            <span className="carousel-control-prev-icon" aria-hidden="true"></span>
            <span className="visually-hidden">Previous</span>
          </button>
          <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
            <span className="carousel-control-next-icon" aria-hidden="true"></span>
            <span className="visually-hidden">Next</span>
          </button>
        </div>
      </div>

      
      <div className="container">
        <div className="row row-cols-0 row-cols-md-0 g-0">
          <div className="col">
            <div className="card ih-100\\\">
              <img src="/img/kyl.png" className="card-img-top" alt="Card" />
              <div className="card-body">
                <h5 className="card-title">Card title</h5>
                <p className="card-text">Author: Author name</p>
                <p className="card-text">Cost: $10</p>
              </div>
              <div className="card-footer">
                <button className="btn btn-outline-danger me-2">
                  <i className="bi bi-heart"></i> Like
                </button>
                <button className="btn btn-outline-primary">
                  <i className="bi bi-basket"></i> Add to cart
                </button>
              </div>
            </div>
          </div>
          {/* Add more cards here */}
        </div>
      </div>




      <footer className="footer">
        &copy; 2024 Your Website. All rights reserved.
      </footer>
    </div>
  );
}

export default App;
