import React, { Component } from 'react';

class SearchForm extends Component {
    constructor() {
        super();
        this.state = {
            id: ""
        };

        this.onChange = this.onChange.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
    }

    onChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        });
    }

    onSubmit(event) {
        event.preventDefault();
        fetch(`/stats?id=${this.state.id}`)
            .then(res => res.json());
        //.then(data => this.props.data.updateInfo(data));

        // onSubmit(event) {
        //     event.preventDefault();
        //     fetch(`/api/stats?id=${this.state.id}`)
        //         .then(res => res.json())
        //         .then(data => this.props.data.updateInfo(data));
        // }
    }

    render() {
        return (
            <div className="search-bar">
                <form onSubmit={this.onSubmit}>
                    <div className="form-row align-items-center">
                        <div className="col-sm-3">
                            <input type="text" name="id" value={this.state.id} onChange={this.onChange} className="form-control" placeholder="id"></input>
                        </div>
                        <div className="col-auto">
                            <button type="button" onClick={this.onSubmit} className="btn btn-primary">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        );
    }
}

export default SearchForm;