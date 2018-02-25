import React from 'react';
import axios from 'axios';

class Footer extends React.Component{

    constructor(props) {
        super(props);
        this.state = {};
    }

    componentWillMount() {
        axios.get('http://localhost:3000/api/puzzles/')
            .then((response) => {
                this.setState({count: response.data.count});
            });
    }

    render() {
        return (
            <div>
                <h3>Footer {this.state.count}</h3>
            </div>
        );
    }
}

export default Footer;