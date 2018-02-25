import React from 'react';
import Header from '../components/Header/header.js';
import Footer from '../components/Footer/footer.js';
import 'bootstrap/dist/css/bootstrap.css';

class Template extends React.Component {
    render() {
        return (
            <div>
                <Header/>
                {this.props.children()}
                <Footer/>
            </div>
        );
    }
}

export default Template;