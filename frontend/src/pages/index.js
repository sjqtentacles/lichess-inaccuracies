import React from 'react'
import Link from 'gatsby-link'

class IndexPage extends React.Component {
  render() {
    return (
      <div>
        <h1>Hi people</h1>
        <Link to="/about/">Go to About Page</Link>
      </div>
    );
  }
}

export default IndexPage;
