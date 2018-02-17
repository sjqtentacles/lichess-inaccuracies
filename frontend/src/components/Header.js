import React from 'react';
import './Header.css';

class Header extends React.Component {
    render() {
        return (
            <div id="navbar">
              <ul>
                <li className='logo' id='navbar'>Tricky Knights</li>
            	<li><a href="/about">About</a></li>
            	<li><a href="/random_puzzle">Random</a></li>
              </ul>
            </div>
        );
    }
}

export default Header;
