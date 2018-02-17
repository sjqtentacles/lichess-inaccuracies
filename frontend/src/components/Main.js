import React from 'react';
import Board from './Board';
import './Main.css';

class Main extends React.Component {
    render() {
        return (
            <div className="mainContainer">
                <h1>Main</h1>
                <Board />
            </div>
        );
    }
}

export default Main;
