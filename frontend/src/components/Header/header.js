import React from 'react';
import {Navbar, Nav, NavItem, Brand, Header} from 'react-bootstrap';
import './header.css';

export default class HeaderIndex extends React.Component {
    render() {
        return (
            <div>
                <Navbar>
                    <Navbar.Header>
                        <Navbar.Brand>
                            <a href="/">TrickyKnights</a>
                        </Navbar.Brand>
                    </Navbar.Header>
                    <Nav>
                        <NavItem eventKey={1} href="/about">
                            About
                        </NavItem>
                    </Nav>
                </Navbar>
            </div>
        );
    }
}