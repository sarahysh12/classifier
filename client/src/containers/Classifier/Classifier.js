import React, { Component } from "react";
import axios from 'axios';
import Prediction from '../../components/Prediction/Prediction';
import './Classifier.css';

class Classifier extends Component {
    state = {
        predictions : null
    }

    componentDidMount() {
        axios.get(process.env.REACT_APP_API_ADDR+'/api/history')
        .then(response => {
            this.setState({predictions: response.data.result});
        })
        .catch(err => {
            console.log(err)
        })
    }

    render() {
        let result = <p>Loading</p>;
        if (this.state.predictions !== null) {
            result = this.state.predictions.map(pred => {
                return <Prediction image={pred.image_path} predictions={pred.prediction_result}/>;
            })
        }

        return (
            <div className="Classifier">
                {result} 
            </div>
        );
    }
}
export default Classifier;