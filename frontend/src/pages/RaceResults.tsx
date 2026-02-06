import { useLoaderData } from "react-router-dom";

const RaceResults = () => {
    const props = useLoaderData();
    return (
        <h2>Race {props.raceId}</h2>
    );
}

export default RaceResults;