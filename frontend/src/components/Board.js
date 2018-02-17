import React from 'react';
require('./chessboard/js/chessboard-0.3.0.js');

import $ from 'jquery';
window.jQuery = window.$ = $;

export default class Board extends React.Component {

    constructor() {
        super();

    }

    render() {
        return (
            <div>
                <div id='chessboard' style={{'width': '400px'}}></div>
            </div>
        );
    }

    componentDidMount() {
    }
}
