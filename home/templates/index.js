var React = require('react');
var ReactDOM = require('react-dom');

var SplashPage = React.createClass({
    render: function() {
        return (
            <div class="container">
                <div class="row">
                    <div class="col-lg-offset-4">
                        <h1>Welcome to my first app!</h1>
                        <h2>This app uses Electron, Django, and React!</h2>
                        <a href="http://127.0.0.1:8000">
                            <button class="btn btn-default">
                                <h4>Click here!</h4>
                            </button>
                        </a>
                    </div>
                </div>
            </div>
        );
    }
});

ReactDOM.render(<SplashPage />, document.getElementById('app'));
