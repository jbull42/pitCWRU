import React from "react";

interface RaceProps {
    raceId: number;
}

const RaceResults: React.FC<RaceProps> = (props) => {
    return <h2>Race {props.raceId}</h2>;
}

export default RaceResults;