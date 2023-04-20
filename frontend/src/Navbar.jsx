import React from 'react';
import {Link} from 'react-router-dom';

function Navbar() {
    return (
      <nav>
            <Link to="/">Dashboard</Link><span>|</span>
            <Link to="/login">Login</Link>
      </nav>
    );
  };

export default Navbar;