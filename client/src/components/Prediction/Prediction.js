import React from 'react';
import './Prediction.css';

const prediction = (props) => {
    let classes = null;
    classes = props.predictions.map(pred => {
        return <p><span>{pred.type}</span> : {pred.score}</p>
    })
    return (
        <div className="Prediction">
            <img src={props.image}/>
            {classes}
        </div>
    );
}

export default prediction;